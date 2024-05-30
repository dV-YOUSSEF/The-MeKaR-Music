from pyrogram import filters
from pyrogram.types import Message
from iLBaReD.__init__ import (AdRenalen_SubScRip)
from iLBaReD import app
from iLBaReD.core.call import Omar
from iLBaReD.utils.database import set_loop
from iLBaReD.utils.decorators import AdminRightsCheck
from iLBaReD.utils.inline import close_markup
from config import BANNED_USERS

@app.on_message(filters.command(["انها","ايقاف","انهاء", "اسكت"],"") & ~BANNED_USERS)

@app.on_message(filters.command(["end", "stop", "cend", "cstop"]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if await AdRenalen_SubScRip(message):
            return
    if not len(message.command) == 1:
        return
    await Omar.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_5"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
