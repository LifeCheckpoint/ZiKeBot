import re
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group, Member
from graia.ariadne.message.parser.base import MentionMe
from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import modules.sum.fileio as sumio
import modules.sum.api as api

from random import choice
from typing import Annotated

channel = Channel.current()
channel.name("Sum")
channel.description("消息整合")
channel.author("LDD")


@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def get_sum(app: Ariadne, group: Group, message: MessageChain):
    # summary
    if str(message)[0: 5] == "/sum ":
        # get step
        try:
            step = int(str(message).replace("/sum ", ""))
            step = 1 if step not in range(1, 4) else step 
        except:
            step = 1

        # check init
        if not api.is_initia():
            if not api.api_init():
                return await app.send_message(
                    group,
                    "API加载失败...可能是未设置API Key，使用/err查看可能的其他原因"
                )
        
        # check history num
        if sumio.get_group_his_num(str(group)) < 30:
            return await app.send_message(
                group,
                "多于30条有效消息时才能调用"
            )

        # read history & summon
        his = sumio.get_group_his(str(group), 100, step)

        # get summary
        res = api.get_sum(his)

        # check whether result is avilable
        if res != "":
            sumio.clear(str(group))
            reply = [t.replace("%d", str(step * 100)) for t in ["最近至多%d条消息总结："]]
            return await app.send_message(
                group,
                choice(reply)  + "\n（没钱交电费，请少点调用）\n" + res
            )
        else:
            return await app.send_message(
                group,
                "调用API失败，使用/err查看原因"
            )
    
    # common msg
    else:
        sumio.write(str(message), str(group))

@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def get_err(app: Ariadne, group: Group, message: MessageChain):
    if str(message) == "/err":
        err_text = str(api.get_last_err())
        if err_text == "":
            return await app.send_message(
            group,
            "还没有错误"
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
                "没找到API KEY..."
            )
        else:
            return await app.send_message(
                group,
                "API KEY：" + api_key.replace(api_key[-6, -1], "******")
            )

@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def set_api(app: Ariadne, group: Group, message: MessageChain):
    if str(message)[0: 7] == "/set_api":
        api_key = str(message).replace("/set_api", "")
        if len(api_key) == "clear":
            api.set_api_key("")
            return await app.send_message(
                group,
                "已清除API KEY"
            )
        
        elif len(api_key) < 3:
            return await app.send_message(
                group,
                "API KEY不合法"
            )

        else:
            api.set_api_key(api_key)
            return await app.send_message(
                group,
                "已设置API KEY"
            )
            