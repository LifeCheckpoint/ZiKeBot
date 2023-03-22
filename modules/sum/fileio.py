import json
from pathlib import Path

his_pth = Path(__file__, "..", "..","..", "data", "history.json").resolve()
def get():
    try:
        his = json.loads(his_pth.read_text(encoding="utf-8"))
    except Exception as e:
        raise e
    return his

def get_group_his(group: str):
    allst = get()
    try:
        return allst[group]
    except(KeyError):
        return []

def write(msg: str, group: str):
    if check_msg(msg) != "":
        his = get()

        try:
            his[group].append(msg)
        except(KeyError):
            his[group] = [msg]

        his_pth.write_text(json.dumps(his), encoding="utf-8")
    return 0

def clear(group: str):
    his = get()
    try:
        his[group] = []
    except(KeyError):
        return 0

    his_pth.write_text(json.dumps(his), encoding="utf-8")
    return 0

def clear_from_count(group: str, count: int):
    """
    删除最后第count消息前的所有消息记录
    """
    his = get()
    try:
        if len(his[group]) > count:
            his[group] = his[group][- count - 1: -1]
    except(KeyError):
        return 0

    his_pth.write_text(json.dumps(his), encoding="utf-8")
    return 0

def check_msg(msg: str) -> str:
    """
    过滤无用消息
    过滤少于4个字符的消息，截断为前30个字符
    """
    
    if len(msg) <= 4:
        return ""
    
    if len(msg) > 30:
        msg = msg[: 30]

    alnum = 0
    for char in msg:
        if char.isalnum():
            alnum += 1
    if alnum > 20:
        return ""
    
    # 关键词检测与替换
    f = open("keywords.txt")
    filt_texts = f.read().split("\n")
    f.close()

    for key in filt_texts:
        if msg != msg.replace(key, ""):
            return ""
    
    if len(msg) <= 4:
        return ""

    return msg