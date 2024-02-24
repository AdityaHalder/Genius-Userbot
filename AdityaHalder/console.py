import os
import time
import logging

from os import getenv
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


logging.basicConfig(
    format="[%(asctime)s]:[%(levelname)s]:[%(name)s]:: %(message)s",
    level=logging.INFO,
    datefmt="%H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "logs.txt", maxBytes=(1024 * 1024 * 5), backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)


if os.path.exists("Internal"):
   load_dotenv("Internal")


API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", None)
BOT_TOKEN = getenv("BOT_TOKEN", None)
STRING_SESSION = getenv("STRING_SESSION", None)
MONGO_DB_URL = getenv("MONGO_DB_URL", None)
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", 0))


# OPTIONAL VARIABLES
SESSION_STRING = getenv("SESSION_STRING", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", ". !").split())



# OTHERS VARIABLES

# PM GUARD VARS
PM_GUARD = bool(getenv("PM_GUARD", True))
PM_GUARD_TEXT = getenv("PM_GUARD_TEXT", "**◄⏤𝆺𝅥⃝⃪⃜🌿♡𝐇ҽʅʅσ 𝐃ҽαɾ 𝐖ҽʅƈσɱҽ 𝐇σɯ 𝐂αɳ 𝐈 𝐇ҽʅρ 𝐘συ. 𝐏ʅҽαʂҽ 𝐋ҽαʋҽ 𝐘συɾ 𝐌ҽʂʂαɠҽ...┽🌌⍣\n\n◄⏤𝆺𝅥⃝⃪⃜🌿♡𝐈 𝐖ιʅʅ 𝐑ҽρʅყ 𝐓σ 𝐘συɾ 𝐂σɱɱҽɳƚ 𝐖ԋҽɳ 𝐈 𝐂σɱҽ 𝐎ɳʅιɳҽ. 𝐏ʅҽαʂҽ 𝐃σ 𝐍σƚ 𝐒ҽɳԃ 𝐌ҽʂʂαɠҽʂ.─‌⃛☯─‌⃛‌⃝❤️\n\n◄⏤‌𝆺𝅥⃝⃪⃜🌿♡𝐌σɾҽ 𝐓ԋαɳ 𝐓ҽɳ 𝐓ιɱҽʂ 𝐎ƚԋҽɾɯιʂҽ 𝐘συ 𝐌αყ 𝐆ҽƚ 𝐁ʅσƈƙҽԃ, 𝐒σɾɾყ 𝐅σɾ 𝐓ԋαƚ.─‌⃛☯─‌⃛‌⃝🌹**")
PM_GUARD_LIMIT = int(getenv("PM_GUARD_LIMIT", 10))



# USERBOT DEFAULT IMAGE
USERBOT_PICTURE = getenv("USERBOT_PICTURE", "https://telegra.ph/file/c4d98ff413f0cdb2c44ed.jpg")



# Don't Edit This Codes From This Line

LOGGER = logging.getLogger("Genius")
runtime = time.time()

FLOODXD = {}
OLD_MSG = {}
PM_LIMIT = {}
PLUGINS = {}
SUDOERS = []


COMMAND_HANDLERS = []
for x in COMMAND_PREFIXES:
    COMMAND_HANDLERS.append(x)
COMMAND_HANDLERS.append('')

