import tiktoken
import openai
import os
from pathlib import Path

last_err = Exception()

def get_api_key():
    api_pth = Path(__file__, "..", "..","..", "data", "api.txt").resolve()
    api_key = api_pth.read_text()
    return api_key

def api_init():
    # 设置代理以访问 api
    # from clash
    os.environ["HTTP_PROXY"] = "http://127.0.0.1:7890"
    os.environ["HTTPS_PROXY"] = "http://127.0.0.1:7890"
    openai.api_key = get_api_key()

def get_sum(msg_his: str):
    msg = "\n".join(msg_his)
    try:
        rsp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "文本分析师"},
                    {"role": "user", "content": "这是一段聊天群内容，归纳它的主题与可能发生的事件：\n" + msg}
                ]
        )
        return rsp.get("choices")[0]["message"]["content"]
    except Exception as e:
        global last_err
        last_err = e
        return ""

def get_last_err():
    return str(last_err)