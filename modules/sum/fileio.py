import json
from pathlib import Path

data_dir = Path(__file__, "..", "..", "..", "data").resolve()

# extract group number from group name
def to_group_number(group_name: str) -> str:
    try:
        left_index = group_name.rfind("(")
        right_index = group_name.rfind(")")
        return group_name[left_index + 1: right_index]
    except:
        return ""

# get group history file
def get_group_file(group: str) -> Path:
    return data_dir / ("his_" + group + ".json")

# get number of group history
def get_group_his_num(group: str) -> int:
    return len(get_group_his(group))

# get group history
def get_group_his(group: str, max_num: int = 100, step: int = 1):
    his_file = get_group_file(group)
    try:
        with his_file.open(encoding = "utf-16") as f:
            group_his = json.load(f)
    except FileNotFoundError:
        return []

    if len(group_his) <= max_num * step:
        return group_his
    else:
        cnt = 0
        step_his = []
        while cnt <= max_num * step:
            step_his.append(group_his[cnt])
            cnt += step
        return step_his

# write group history to file
def write(msg: str, group: str):
    if check_msg(msg) != "":
        his_file = get_group_file(group)
        try:
            with his_file.open(encoding = "utf-16") as f:
                his = json.load(f)
        except FileNotFoundError:
            his = []

        his.append(msg)

        with his_file.open(mode = "w", encoding = "utf-16") as f:
            json.dump(his, f)

# clear the history of a group
def clear(group: str):
    his_file = get_group_file(group)
    try:
        his_file.unlink()
    except FileNotFoundError:
        return

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