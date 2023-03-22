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

@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def get_sum(app: Ariadne, group: Group, message: Annotated[MessageChain, MentionMe()]):
    if message.display in ["群友聊了啥", "聊了啥"]:

        return await app.send_message(
            group,
            "developing..."
        )

