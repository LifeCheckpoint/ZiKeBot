# ZiKeBot
A personal bot.

now still in developing

project bases on AFLeartLey

## Configuration
如果使用poetry，则通过设置虚拟环境配置pyproject.toml
conda类似

## Launch
  1. 使用 `poetry` 或 `conda` ，以及 `python 3.8` 安装对应的库（虽然我用3.9）
  2. 在 `.\data\api_key.txt` 配置OpenAI的API
  3. 打开 `mcl` （版本需高于2.0）
  4. 使用poetry，运行 `poetry run python main.py` ，conda则进入虚拟环境后直接 `python main.py`

## Application
目前主要指令 / 功能：
  1. `zike` 或 `hi zike` Ping
  2. 随机水群
  3. `/sum [stp | ?]` 完成群聊自动总结