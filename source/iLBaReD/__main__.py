import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from iLBaReD import LOGGER, app, userbot
from iLBaReD.core.call import Omar
from iLBaReD.misc import sudo
from iLBaReD.plugins import ALL_MODULES
from iLBaReD.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("iLBaReD.plugins" + all_module)
    LOGGER("iLBaReD.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Omar.start()
    try:
        await Omar.stream_call("https://telegra.ph/file/a982187bd0641ac430c78.jpg")
    except NoActiveGroupCall:
        LOGGER("AdRenalen").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Omar.decorators()
    LOGGER("AdRenalen").info("Dev.SuoRce @DEV_ADRENALEN The.SouRce.AdRenalen @WA_ADRENALEN @BAR_ADRENALEN"
            )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("AdRenalen").info("يتم طنشيط البوت الان 💘 ⋅")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
