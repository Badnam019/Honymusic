import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from AnonXMusic import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://files.catbox.moe/tr0myp.jpg",
    "https://files.catbox.moe/tr0myp.jpg",
    "https://files.catbox.moe/pxuxmd.jpg",
    "https://files.catbox.moe/tr0myp.jpg",
    "https://files.catbox.moe/tr0myp.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"🚩 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗔𝗗𝗗𝗘𝗗 𝗡𝗘𝗪 𝗚𝗥𝗢𝗨𝗣\n\n"
                f"____________________________________\n\n"
                f"🚩 𝗖𝗛𝗔𝗧 𝗡𝗔𝗠𝗘: {chat.title}\n"
                f"🚩 𝗖𝗛𝗔𝗧 𝗜𝗗: {chat.id}\n"
                f"🚩 𝗖𝗛𝗔𝗧 𝗨𝗦𝗘𝗥 𝗡𝗔𝗠𝗘: @{chat.username}\n"
                f"🚩 𝗖𝗛𝗔𝗧 𝗟𝗜𝗡𝗞: [ᴄʟɪᴄᴋ]({link})\n"
                f"🚩 𝗖𝗢𝗨𝗡𝗧 𝗠𝗘𝗠𝗕𝗘𝗥: {count}\n"
                f"🚩 𝗔𝗗𝗗 𝗕𝗬𝗬 𝗔𝗗𝗠𝗜𝗡: {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝗨𝗡𝗢𝗪𝗢𝗡 𝗨𝗦𝗘𝗥"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝗣𝗥𝗜𝗩𝗔𝗧𝗘 𝗖𝗛𝗔𝗧"
        chat_id = message.chat.id
        left = f"✫ <b><u>#𝗟𝗘𝗙𝗧 𝗚𝗥𝗢𝗨𝗣 𝗢𝗪𝗡𝗘𝗥 𝗣𝗔𝗚𝗔𝗟 𝗛𝗔𝗜</u></b> ✫\n\n𝐂ʜᴀᴛ 𝐓ɪᴛʟᴇ : {title}\n\n𝗖𝗛𝗔𝗧 𝗜𝗗 : {chat_id}\n\n𝗥𝗘𝗢𝗠𝗩𝗘 : {remove_by}\n\n𝗕𝗢𝗧 : @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
