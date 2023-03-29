import pkgutil
import yaml
from pathlib import Path
from creart import create
from graia.ariadne.app import Ariadne
from graia.ariadne.connection.config import (
    config,
)
from graia.ariadne.event.message import GroupMessage
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.model import Group
from graia.broadcast import Broadcast
from graia.saya import Saya


saya = create(Saya)
bcc = create(Broadcast)
app = Ariadne(
    connection = config(
        2873234285,
        "LDDMiao",
    ),
)
config_path = Path(__file__, "config.yaml").resolve()
with open(str(config_path), "r") as stream:
    bot_config = yaml.safe_load(stream)

with saya.module_context():
    for module in pkgutil.iter_modules(["modules"]):
        if module.name in bot_config["unloaded_plugins"]:
            continue
        saya.require(f"modules.{module.name}")

app.launch_blocking()