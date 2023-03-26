from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
import random as ran

import modules.const_msg as cm

channel = Channel.current()
channel.name("ran_re")
channel.description("随机回复")
channel.author("LDD")

@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def random_repeator(app: Ariadne, group: Group, message: MessageChain):
    k = ran.randint(1, 400)
    if(k == 114):
        await app.send_message(
            group,
            message.as_sendable()
        )

@channel.use(ListenerSchema(listening_events = [GroupMessage]))
async def water(app: Ariadne, group: Group, message: MessageChain):
    k = ran.randint(1, 500)
    if(k == 114):
        await app.send_message(
            group,
            cm.msg("ran_re.water")
        )