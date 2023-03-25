import random as ran

msg_dict = {
    # help
    "help.ping": [
        "在！使用/help zike加载帮助",
        "不在！使用/help zike加载帮助",
        "嗯？",
        "鳖载着理发店"
    ],
    "help.help": ["""梓刻Bot By. LDD
提示：方括号为可选参数
------------
/help zike - 本页面
zike 或 hi zike - Ping
-----------
/sum [stp]
- 总结最多100条消息内容
- 每stp条消息摘取一次内容，默认为1
- 1 ≤ stp ≤ 3
/set_api API_KEY | clear - 设置或清除API Key
/get_api - 获取当前的API Key
/err - 获取最后发生的错误"""],
    
    # ran_re
    "ran_re.water": [
        "水个群",
        "冒个泡"
    ],

    # sum
    "sum.api_failed": [
        "API加载失败了...可能是未设置API Key，使用/err查看可能的其他原因",
        "w(ﾟДﾟ)w API加载失败，没设置API Key嘛？使用/err查看可能的其他原因"
    ],
    "sum.msg_limit": [
        "还没聊够三十条(o-ωｑ)).oO",
        "至少要新聊30条才能调用oωo"
    ],
    "sum.reply": [
        "最近至多%d条消息总结：\n（o(TヘTo)没钱交电费，珍惜调用次数）\n",
        "最近%d条，群友聊了...\n（o(TヘTo)没钱交电费，珍惜调用次数）\n"
    ],
    "sum.api_calling_failed": [
        "API调用失败了...使用/err查看原因",
        "X﹏X API调用失败，使用/err查看原因"
    ],
    "sum.no_err": [
        "偷着乐吧，还没错误( •̀ ω •́ )",
        "没有错误！（震声）"
    ],
    "sum.api_key_missing": [
        "没找到API Key...",
        "老是乱丢API Key，找不见了吧~"
    ],
    "sum.api_setting": [
        "API Key设置好了❤",
        "已设置API Key！"
    ],
    "sum.api_setting_illegal": [
        "这不是API Key吧...？",
        "API Key不长这样啊(。Д。)"
    ],
    "sum.api_setting_clear": [
        "洒扫庭除，清除OK！",
        "删掉API Key咯！"
    ]
}

def msg(msg_type: str) -> str:
    try:
        return ran.choice(msg_dict[msg_type])
    except:
        return ""