from logging.config import listen
from typing import Annotated
from graia.ariadne.app import Ariadne
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.ariadne.message.parser.base import MatchContent

from graia.saya import Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema

channel = Channel.current()

helpmessage = """
梓刻Bot By. LDD
------------
提示：方括号为可选参数
------------
/help zike
 - 本页面
zike
 - Ping
/err
 - 获取最后发生的错误
 -----------
/sum [stp]
 - 总结最多100条消息内容
 - 每stp条消息摘取一次内容，默认为1
 - 1 ≤ stp ≤ 3
/set_api API_KEY | clear
 - 设置或清除API Key
/get_api
 - 获取当前的API Key
"""
@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def get_help(app:Ariadne, group:Group, message: MessageChain):
    if str(message).lower() == "/help zike":
        return await app.send_message(
            group,
            MessageChain(helpmessage)
        )
