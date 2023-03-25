import openai
import os
from pathlib import Path

last_err = Exception()
is_init = False

def set_api_key(key: str):
    try:
        api_pth = Path(__file__, "..", "..","..", "data", "api_key.txt").resolve()
        api_pth.write_text(key)
    except Exception as e:
        global last_err
        last_err = e

def get_api_key():
    try:
        api_pth = Path(__file__, "..", "..","..", "data", "api_key.txt").resolve()
        api_key = api_pth.read_text()
        return api_key
    except Exception as e:
        global last_err
        last_err = e
        return ""

def api_init():
    # set proxy to access api
    # from clash

    # IMPORTANT: DO NOT USE HK / TW SERVER OR THE ACCOUNT WILL BE BAN 

    os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"

    try:
        openai.api_key = get_api_key()
    except Exception as e:
        global last_err, is_init
        last_err = e
        is_init = False

    is_init = not (get_api_key() == "")
    
    return is_init

def get_sum(msg_his: list):
    msg = "\n".join(msg_his)
    try:
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "文本分析师"},
                    {"role": "user", "content": "这是一个聊天群聊天内容，归纳其主题与可能发生的事件：\n" + msg}
                ]
        )
        return rsp.get("choices")[0]["message"]["content"]
    except Exception as e:
        global last_err
        last_err = e
        return ""

def get_last_err():
    return str(last_err)

def is_initia():
    return is_init

def get_last_err():
    return last_err