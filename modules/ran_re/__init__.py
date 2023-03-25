from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from random import randint

channel = Channel.current()
channel.name("ran_re")
channel.description("随机回复")
channel.author("LDD")

@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def randomRepeator(app: Ariadne,group: Group,message: MessageChain):
    k = randint(1, 200)
    if(k == 114):
        await app.send_message(
            group,
            message.as_sendable()
        )