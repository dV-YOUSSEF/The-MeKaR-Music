import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

OWNER = ["DEV_ADRENALEN"]
OWNER_NAME = "Omar AdRenalen"
BOT_TOKEN = getenv("BOT_TOKEN")
DATABASE = getenv("MONGO_DB_URI", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
CHANNEL = "https://t.me/WA_ADRENALEN"
GROUP = "https://t.me/WA_ADRENALEN"
VID_SO = "https://t.me/SOURCE_BOYKA/41"
PHOTO = "https://telegra.ph/file/a982187bd0641ac430c78.jpg"
LOGS = "gbbbbbbol"
