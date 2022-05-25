import logging
import os
import sys
import time
import spamwatch
import httpx
import aiohttp
import telegram.ext as tg

from pyrogram import Client, errors
from pyrogram.errors.exceptions.bad_request_400 import PeerIdInvalid, ChannelInvalid
from telethon import TelegramClient
from telethon.sessions import MemorySession
from telethon.sessions import StringSession
from motor import motor_asyncio
from odmantic import AIOEngine
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from redis import StrictRedis
from Python_ARQ import ARQ
from aiohttp import ClientSession
from telegraph import Telegraph
from telegram import Chat

StartTime = time.time()

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

# if version < 3.6, stop bot.
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error(
        "You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.",
    )
    quit(1)

ENV = bool(os.environ.get("ENV", False))

if ENV:
    TOKEN = os.environ.get("TOKEN", None)

    try:
        OWNER_ID = int(os.environ.get("OWNER_ID", "5202917395"))
    except ValueError:
        raise Exception("Your OWNER_ID env variable is not a valid integer.")

    JOIN_LOGGER = os.environ.get("JOIN_LOGGER", None)
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", None)

    try:
        DRAGONS = set(int(x) for x in os.environ.get("DRAGONS", "").split())
        DEV_USERS = set(int(x) for x in os.environ.get("DEV_USERS", "").split())
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in os.environ.get("DEMONS", "").split())
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in os.environ.get("WOLVES", "").split())
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in os.environ.get("TIGERS", "").split())
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    INFOPIC = bool(os.environ.get("INFOPIC", False))
    EVENT_LOGS = os.environ.get("EVENT_LOGS", None)
    ERROR_LOGS = os.environ.get("ERROR_LOGS", None)
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))
    URL = os.environ.get("URL", "")  # Does not contain token
    PORT = int(os.environ.get("PORT", 5000))
    CERT_PATH = os.environ.get("CERT_PATH")
    ARQ_API_URL = "https://thearq.tech"
    API_ID = os.environ.get("API_ID", None)
    YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY", True)
    API_HASH = os.environ.get("API_HASH", None)
    DB_URL = os.environ.get(
        "DATABSE_URL",
        "postgresql://cossaojk:apEf76LRIlm0RL_SUngGreMghS7Bm5fb@castor.db.elephantsql.com/cossaojk",
    )
    DONATION_LINK = os.environ.get("DONATION_LINK")
    LOAD = os.environ.get("LOAD", "").split()
    NO_LOAD = os.environ.get("NO_LOAD", "translation").split()
    DEL_CMDS = bool(os.environ.get("DEL_CMDS", False))
    STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False))
    WORKERS = int(os.environ.get("WORKERS", 8))
    MONGO_DB = "Flare"
    TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")
    BAN_STICKER = os.environ.get("BAN_STICKER", "CAADAgADOwADPPEcAXkko5EB3YGYAg")
    MESSAGE_DUMP = os.environ.get("MESSAGE_DUMP", "-1001643635068")
    ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)
    CASH_API_KEY = os.environ.get("CASH_API_KEY", None)
    TIME_API_KEY = os.environ.get("TIME_API_KEY", None)
    AI_API_KEY = os.environ.get("AI_API_KEY", None)
    API_WEATHER = os.environ.get("API_OPENWEATHER", None)
    WALL_API = os.environ.get("WALL_API", None)
    MONGO_DB_URI = os.environ.get("MONGO_DB_URI", None)
    REDIS_URL = os.environ.get(
        "REDIS_URL",
        "redis://Asta:Asta_123@redis-11259.c277.us-east-1-3.ec2.cloud.redislabs.com:11259/Asta",
    )
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", None)
    SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    BOT_ID = os.environ.get("BOT_ID", None)
    ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", None)
    FLARE_PHOTO = os.environ.get(
        "FLARE_PHOTO", "https://telegra.ph/file/2a171330f0ad1fc02465c.jpg"
    )
    BOT_NAME = os.environ.get("BOT_NAME", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    BOT_API_URL = os.environ.get("BOT_API_URL", "https://api.telegram.org/bot")

    try:
        BL_CHATS = set(int(x) for x in os.environ.get("BL_CHATS", "").split())
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")

else:
    from Flare_Robot.config import Development as Config

    TOKEN = Config.TOKEN

    try:
        OWNER_ID = int(Config.OWNER_ID)
    except ValueError:
        raise Exception("Your OWNER_ID variable is not a valid integer.")

    JOIN_LOGGER = Config.JOIN_LOGGER
    OWNER_USERNAME = Config.OWNER_USERNAME
    ALLOW_CHATS = Config.ALLOW_CHATS
    try:
        DRAGONS = set(int(x) for x in Config.DRAGONS or [])
        DEV_USERS = set(int(x) for x in Config.DEV_USERS or [])
    except ValueError:
        raise Exception("Your sudo or dev users list does not contain valid integers.")

    try:
        DEMONS = set(int(x) for x in Config.DEMONS or [])
    except ValueError:
        raise Exception("Your support users list does not contain valid integers.")

    try:
        WOLVES = set(int(x) for x in Config.WOLVES or [])
    except ValueError:
        raise Exception("Your whitelisted users list does not contain valid integers.")

    try:
        TIGERS = set(int(x) for x in Config.TIGERS or [])
    except ValueError:
        raise Exception("Your tiger users list does not contain valid integers.")

    EVENT_LOGS = Config.EVENT_LOGS
    ERROR_LOGS = Config.EVENT_LOGS
    WEBHOOK = Config.WEBHOOK
    URL = Config.URL
    PORT = Config.PORT
    CERT_PATH = Config.CERT_PATH
    API_ID = Config.API_ID
    API_HASH = Config.API_HASH

    DB_URI = Config.SQLALCHEMY_DATABASE_URI
    DONATION_LINK = Config.DONATION_LINK
    LOAD = Config.LOAD
    MESSAGE_DUMP = Config.MESSAGE_DUMP
    APP_ID = Config.APP_ID
    APP_HASH = Config.APP_HASH
    NO_LOAD = Config.NO_LOAD
    DEL_CMDS = Config.DEL_CMDS
    TEMP_DOWNLOAD_DIRECTORY = Config.TEMP_DOWNLOAD_DIRECTORY
    STRICT_GBAN = Config.STRICT_GBAN
    WORKERS = Config.WORKERS
    BAN_STICKER = Config.BAN_STICKER
    MONGO_DB = Config.MONGO_DB
    ALLOW_EXCL = Config.ALLOW_EXCL
    CASH_API_KEY = Config.CASH_API_KEY
    TIME_API_KEY = Config.TIME_API_KEY
    ARQ_API_URL = Config.ARQ_API_URL
    AI_API_KEY = Config.AI_API_KEY
    API_WEATHER = Config.API_OPENWEATHER
    WALL_API = Config.WALL_API
    SUPPORT_CHAT = Config.SUPPORT_CHAT
    SPAMWATCH_SUPPORT_CHAT = Config.SPAMWATCH_SUPPORT_CHAT
    SPAMWATCH_API = Config.SPAMWATCH_API
    INFOPIC = Config.INFOPIC
    YOUTUBE_API_KEY = Config.YOUTUBE_API_KEY
    BOT_USERNAME = Config.BOT_USERNAME
    FLARE_PHOTO = Config.FLARE_PHOTO
    DB_URL = Config.DB_URI
    BOT_NAME = Config.BOT_NAME
    STRING_SESSION = Comfig.STRING_SESSION
    BOT_API_URL = Config.BOT_API_URL

    try:
        BL_CHATS = set(int(x) for x in Config.BL_CHATS or [])
    except ValueError:
        raise Exception("Your blacklisted chats list does not contain valid integers.")


DRAGONS.add(OWNER_ID)
DEV_USERS.add(OWNER_ID)
DEMONS.add(1470075895)


if not SPAMWATCH_API:
    sw = None
    LOGGER.warning("SpamWatch API key missing! recheck your config.")
else:
    try:
        sw = spamwatch.Client(SPAMWATCH_API)
    except:
        sw = None
        LOGGER.warning("Can't connect to SpamWatch!")


REDIS = StrictRedis.from_url(REDIS_URL, decode_responses=True)
try:
    REDIS.ping()
    LOGGER.info(" Your redis server is now alive!")
except BaseException:
    raise Exception("Your redis server is not alive, please check again.")
finally:
    REDIS.ping()
    LOGGER.info(" Your redis server is now alive!")


telegraph = Telegraph()
telegraph.create_account(short_name="Freiaa")
print("TELETHON CLIENT STARTING")
telethn = TelegramClient(MemorySession(), API_ID, API_HASH)
updater = tg.Updater(
    TOKEN,
    workers=min(32, os.cpu_count() + 4),
    request_kwargs={"read_timeout": 10, "connect_timeout": 10},
)
dispatcher = updater.dispatcher
print("PYROGRAM CLIENT STARTING")
session_name = TOKEN.split(":")[0]
client = TelegramClient(MemorySession(), API_ID, API_HASH)
pbot = Client(
    session_name,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN,
)
mongodb = MongoClient(MONGO_DB_URI, 27017)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI)
db = motor[MONGO_DB]
engine = AIOEngine(motor, MONGO_DB)
print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()
# ARQ Client
print("[INFO]: INITIALIZING ARQ CLIENT")
arq = ARQ("https://thearq.tech", "YIECCC-NAJARO-OLLREW-SJSRIP-ARQ", aiohttpsession)
ubot = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
timeout = httpx.Timeout(40)
http = httpx.AsyncClient(http2=True, timeout=timeout)


async def get_entity(client, entity):
    entity_client = client
    if not isinstance(entity, Chat):
        try:
            entity = int(entity)
        except ValueError:
            pass
        except TypeError:
            entity = entity.id
        try:
            entity = await client.get_chat(entity)
        except (PeerIdInvalid, ChannelInvalid):
            for pbot in apps:
                if pbot != client:
                    try:
                        entity = await pbot.get_chat(entity)
                    except (PeerIdInvalid, ChannelInvalid):
                        pass
                    else:
                        entity_client = pbot
                        break
            else:
                entity = await pbot.get_chat(entity)
                entity_client = pbot
    return entity, entity_client


apps = [pbot]
DRAGONS = list(DRAGONS) + list(DEV_USERS)
DEV_USERS = list(DEV_USERS)
WOLVES = list(WOLVES)
DEMONS = list(DEMONS)
TIGERS = list(TIGERS)

# Load at end to ensure all prev variables have been set
from Flare_Robot.modules.helper_funcs.handlers import (
    CustomCommandHandler,
    CustomMessageHandler,
    CustomRegexHandler,
)

# make sure the regex handler can take extra kwargs
tg.RegexHandler = CustomRegexHandler
tg.CommandHandler = CustomCommandHandler
tg.MessageHandler = CustomMessageHandler
