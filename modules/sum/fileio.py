import json
from pathlib import Path

his_pth = Path(__file__, "..", "..","..", "data", "history.json").resolve()

# get history file
def get():
    try:
        his = json.loads(his_pth.read_text(encoding="utf-16"))
    except:
        return {}
    return his

# get number of group's history
def get_group_his_num(group: str):
    allst = get()
    try:
        his_len = len(allst[group])
        return his_len
    except:
        return 0

# get history of a group
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

# write group history to file
def write(msg: str, group: str):
    if check_msg(msg) != "":
        his = get()

        try:
            his[group].append(msg)
        except(KeyError):
            his[group] = [msg]

        his_pth.write_text(json.dumps(his), encoding="utf-16")

# clear the history of a group
def clear(group: str):
    his = get()
    try:
        his[group] = []
    except(KeyError):
        return 0

    his_pth.write_text(json.dumps(his), encoding="utf-16")
    return 0

# clear the history of a group before count
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

    his_pth.write_text(json.dumps(his), encoding="utf-16")
    return 0

# check whether msg is legal
def check_msg(msg: str) -> str:
    """
    过滤无用消息
     - 截断为前30个字符
     - 字母数 > 20忽略
     - 含有关键词忽略
     - 过滤少于4个字符的消息
    """
    
    # clip
    if len(msg) > 30:
        msg = msg[: 30]

    # alnum
    alnum = 0
    for char in msg:
        if char.isalnum() or char.isnumeric():
            alnum += 1
    if alnum > 20:
        return ""
    
    # key word detection
    try:
        f = open("keywords.txt")
        filt_texts = f.read().split("\n")
        f.close()

        for key in filt_texts:
            if msg.find(key) != -1:
                return ""
    except:
        pass

    # len detection
    if len(msg) <= 4:
        return ""

    return msg