from pyrogram.enums import ParseMode

from iLBaReD import app
from iLBaReD.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>━━━━━━━━━━━━━━━</b>
<b>◍ [⌞ 𝘾𝙍 𖢻 ⌯ 𝙈𝙐𝙎𝙄𝘾 ⌯ 🎧𝄞</b>
<b>━━━━━━━━━━━━━━━</b>
<b>⇓  𝙒 : 𝙀 : 𝙇 : 𝘾 : 𝙊 : 𝙈 : 𝙀  ⇓</b>
<b>━━━━━━━━━━━━━━━<b>
<b>- الاسم :</b> {message.from_user.mention}
<b>- اليوزر :</b> @{message.from_user.username}
<b>- ايدي المستخدم :</b> <code>{message.from_user.id}</code>
<b>━━━━━━━━━━━━━━━<b>
<b>- اسم المجموعة :</b> {message.chat.title}
<b>- يوزر المجموعة :</b> @{message.chat.username}
<b>- ايدي المجموعة :</b> <code>{message.chat.id}</code>
<b>━━━━━━━━━━━━━━━<b>
<b>- الطلب :</b> {message.text.split(None, 1)[1]}
<b>━━━━━━━━━━━━━━━<b>
<b>- نوع التشغيل :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
