from iLBaReD.core.bot import Omar
from iLBaReD.core.dir import dirr
from iLBaReD.core.git import git
from iLBaReD.core.userbot import Userbot
from iLBaReD.misc import dbb, heroku, sudo
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = Omar()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

async def AdRenalen_SubScRip(message):
    if not message.from_user: return
    try:
            await message._client.get_chat_member("WA_ADRENALEN", message.from_user.id)
    except UserNotParticipant:
                await message.reply(
                    f"يجب ان تشترك في القناة لستخدام الامر 😋♥️ ،\n\n- قناة البوت : « https://t.me/WA_ADRENALEN »",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("اضفط هنا للاشتراك في القناة 😋♥️ ،", url=f"https://t.me/WA_ADRENALEN"),
                            ],
                         ] 
                      ) 
                   )
                return True
    except:
        pass
