import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Flare_Robot.events import register
from Flare_Robot import telethn as tbot


PHOTO = "https://telegra.ph/file/f732dde7b81f7d29a2973.jpg"


@register(pattern=("/alive"))
async def awake(event):
    TEXT = "**♡ I,m ᴋᴀᴡᴀɪ ᴘʀᴏʙᴏᴛ 愛** \n\n"
    TEXT += f"**♡ I'm Working With sᴇxʏ Speed** \n\n"
    TEXT += f"**♡ ᴋᴀᴡᴀɪɪ: LATEST Version** \n\n"
    TEXT += f"**♡ My Creator: [ ᴀsᴛᴀ](http://t.me/Asta_silva02)** \n\n"
    TEXT += f"**♡ ᴀɴʏ ɪssᴜᴇs ᴄᴏɴᴛᴀᴄᴛ ʜᴇʀᴇ @Freia_Support** \n\n"
    TEXT += "**♡ ᴛʜᴀɴᴋ ʏᴏᴜ ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ 💘💘💘**"
    BUTTON = [
        [
            Button.url("📢 Updates", "https://t.me/Freia_Updates"),
            Button.url("🚑 Support", "https://t.me/Freia_Support"),
        ]
    ]
    await tbot.send_file(event.chat_id, PHOTO, caption=TEXT, buttons=BUTTON)
