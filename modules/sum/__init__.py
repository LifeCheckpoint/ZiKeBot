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
async def get_sum(app: Ariadne, group: Group, message: Annotated[MessageChain, MentionMe()]):
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
                    "API加载失败...用/err看看吧"
                )
        
        # read history & summon
        his = sumio.get_group_his(str(group), 100, step)
        if his != []:
            res = api.get_sum(his)
            if res != ""

        
        return await app.send_message(
            group,
            "developing..."
        )
    
    else:
        pass
