import re
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group, Member
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import modules.sum.fileio as sumio
import modules.sum.api as api
import modules.const_msg as cm

channel = Channel.current()
channel.name("sum")
channel.description("使用OpenAI接口进行消息整合")
channel.author("LDD")

# summary
@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def get_sum(app: Ariadne, group: Group, message: MessageChain):
    g_number = sumio.to_group_number(str(group))

    if str(message)[0: 4] == "/sum":
        # get step
        try:
            step = int(str(message).replace("/sum ", "").replace("/sum", ""))
            step = 1 if step not in range(1, 4) else step 
        except:
            step = 1

        # check init
        if not api.api_init():
            return await app.send_message(
                group,
                cm.msg("sum.api_failed")
            )
        
        # check history num
        if sumio.get_group_his_num(g_number) < 30:
            return await app.send_message(
                group,
                cm.msg("sum.msg_limit")
            )

        # read history & summon
        his = sumio.get_group_his(g_number, 100, step)

        # get summary
        res = api.get_sum(his)

        # check whether result is avilable
        if res != "":
            sumio.clear(g_number)
            return await app.send_message(
                group,
                cm.msg("sum.reply").replace("%d", str(step * 100)) + res
            )
        else:
            return await app.send_message(
                group,
                cm.msg("sum.api_calling_failed")
            )
    
    # common msg
    else:
        sumio.write(str(message), g_number)

# getting last error
@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def get_err(app: Ariadne, group: Group, message: MessageChain):
    if str(message) == "/err":
        err_text = str(api.get_last_err())
        if err_text == "":
            return await app.send_message(
            group,
            cm.msg("sum.no_err")
        )
        else:
            return await app.send_message(
                group,
                err_text
            )
    
@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def get_api(app: Ariadne, group: Group, message: MessageChain):
    if str(message) == "/get_api":
        api_key = api.get_api_key()
        if api_key == "":
            return await app.send_message(
                group,
                cm.msg("sum.api_key_missing")
            )
        else:
            return await app.send_message(
                group,
                "API KEY：" + api_key.replace(api_key[-11: -1], "******")
            )

@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def set_api(app: Ariadne, group: Group, message: MessageChain):
    if str(message).find("/set_api") != -1:
        api_key = str(message).replace("/set_api ", "")
        if len(api_key) == "clear":
            api.set_api_key("")
            return await app.send_message(
                group,
                cm.msg("sum.api_setting_clear")
            )
        
        elif len(api_key) < 3:
            return await app.send_message(
                group,
                cm.msg("sum.api_setting_illegal")
            )

        else:
            api.set_api_key(api_key)
            return await app.send_message(
                group,
                cm.msg("sum.api_setting")
            )
            