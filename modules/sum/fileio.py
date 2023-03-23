import json
from pathlib import Path

his_pth = Path(__file__, "..", "..","..", "data", "history.json").resolve()
def get():
    try:
        his = json.loads(his_pth.read_text(encoding="utf-8"))
    except Exception as e:
        raise e
    return his

def get_group_his(group: str, max_num: int = 100, step: int = 1):
    allst = get()
    try:
        group_his = allst[group]
    except(KeyError):
        return []
    if len(group_his) <= max_num * step:
        return group_his
    else:
        cnt = 0
        step_his= []
        while cnt <= max_num * step:
            step_his.append(group_his[cnt])
            cnt += step
        return step_his


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
     - 截断为前30个字符
     - 字母数 > 20忽略
     - 含有关键词忽略
     - 过滤少于4个字符的消息
    """
    
    # 字符截断
    if len(msg) > 30:
        msg = msg[: 30]

    # 字母数
    alnum = 0
    for char in msg:
        if char.isalnum():
            alnum += 1
    if alnum > 20:
        return ""
    
    # 关键词检测
    try:
        f = open("keywords.txt")
        filt_texts = f.read().split("\n")
        f.close()

        for key in filt_texts:
            if msg.find(key) != -1:
                return ""
    except:
        pass

    # 过滤
    if len(msg) <= 4:
        return ""

    return msg