from logging.config import listen
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.message.parser.base import MatchContent

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

import modules.const_msg as cm

channel = Channel.current()

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def get_help(app:Ariadne, group:Group, message: MessageChain):
    if str(message).lower() == "/help zike":
        return await app.send_message(
            group,
            MessageChain(cm.msg("help.help"))
        )

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def messageProcessor(app: Ariadne,group: Group,message: MessageChain):
    if str(message).lower() in ["zike", "hi zike"]:
        await app.send_message(
            group,
            MessageChain(cm.msg("help.ping"))
        )