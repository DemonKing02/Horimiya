from envparse import env

from Flare_Robot import LOGGER
import os

INFOPIC = bool(os.environ.get("INFOPIC", False))
EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
ERROR_LOGS = os.environ.get("ERROR_LOGS", None)
WEBHOOK = bool(os.environ.get("WEBHOOK", False))
URL = os.environ.get("URL", "")
# Does not contain token PORT = int(os.environ.get("PORT", 5000))
CERT_PATH = os.environ.get("CERT_PATH")
ARQ_API_URL = "https://thearq.tech"
API_ID = os.environ.get("API_ID", None)
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", True)
API_HASH = os.environ.get("API_HASH", None)
DB_URL = os.environ.get("DATABSE_URL", "postgresql://eptbyege:0TbLe5xjHocel_1kPTXvKyOi54oV8ywf@tyke.db.elephantsql.com/eptbyege")
DONATION_LINK = os.environ.get("DONATION_LINK") LOAD = os.environ.get("LOAD", "").split()
NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
WORKERS = int(os.environ.get("WORKERS", 8))
MONGO_DB = "Flare"
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", "-1001527971671")
ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
AI_API_KEY = os.environ.get("AI_API_KEY", None)
API_WEATHER = os.environ.get("API_OPENWEATHER", None)
WALL_API = os.environ.get("WALL_API", None)
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
REDIS_URL = os.environ.get("REDIS_URL", None)
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
BOT_ID = os.environ.get ("BOT_ID", None) ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
FLARE_PHOTO = os.environ.get("FLARE_PHOTO", "https://telegra.ph/file/3883fe16c3e776625a97b.jpg")
BOT_NAME = os.environ.get("BOT_NAME", None) STRING_SESSION = os.environ.get("STRING_SESSION", None)
BOT_API_URL = os.environ.get("BOT_API_URL", "https://api.telegram.org/bot")
TOKEN = os.environ.get("TOKEN", None)

DEFAULTS = {
    "LOAD_MODULES": True,
}


def get_str_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.str(name, default=default)) and not required:
        LOGGER.warn("No str key: " + name)
        return None
    elif not data:
        LOGGER.critical("No str key: " + name)
        sys.exit(2)
    else:
        return data


def get_int_key(name, required=False):
    if name in DEFAULTS:
        default = DEFAULTS[name]
    else:
        default = None
    if not (data := env.int(name, default=default)) and not required:
        LOGGER.warn("No int key: " + name)
        return None
    elif not data:
        LOGGER.critical("No int key: " + name)
        sys.exit(2)
    else:
        return data
