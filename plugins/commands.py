import os
import os
import time
import psutil
import shutil
import string
import asyncio


if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

#############################################################





from client import Client
from database.access import db
from helper_funcs.display_progress import humanbytes
from plugins.broadcast import broadcast_handler

###############################################################

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
    

@Client.on_message(filters.command(["help"]) & filters.private)
async def help_user(bot, update):
    await update.reply_text(
        text=Translation.HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=Translation.HELP_BUTTONS
    )

@Client.on_message(filters.command(["about"]) & filters.private)
async def get_me_info(bot, update):
    await update.reply_text(
        text=Translation.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=Translation.ABOUT_BUTTONS
    )


####################################################################################################################

@Client.on_message(filters.command(["status"]) & filters.user(Config.OWNER_ID) & ~filters.edited)
async def status_handler(_, m: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await m.reply_text(
        text=f"**Total Disk Space:** {total} \n"
             f"**Used Space:** {used}({disk_usage}%) \n"
             f"**Free Space:** {free} \n"
             f"**CPU Usage:** {cpu_usage}% \n"
             f"**RAM Usage:** {ram_usage}%\n\n"
             f"**Total Users in DB:** `{total_users}`",
        parse_mode="Markdown",
        quote=True
    )


@Client.on_message(filters.command(["broadcast"]) & filters.user(Config.OWNER_ID) & filters.reply & ~filters.edited)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)    
