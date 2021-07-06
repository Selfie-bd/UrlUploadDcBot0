import sqlite3
import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )

@Client.on_message(filters.command(["upgrade"]) & filters.private)
async def upgrade(bot, update):
    await update.reply_text(
        text=Translation.UPGRADE_TEXT,
        disable_web_page_preview=True
    )

@Client.on_message(filters.command(["about"]) & filters.private)
async def get_me_info(bot, update):
        await update.message.edit_text(
            text=Translation.ABOUT_TEXT,
            reply_markup=Translation.ABOUT_BUTTONS,
            disable_web_page_preview=True
    )

@Client.on_message(filters.command(["help"]) & filters.private)
async def help_user(bot, update):
        await update.message.edit_text(
            text=Translation.HELP_TEXT,
            reply_markup=Translation.HELP_BUTTONS,
            disable_web_page_preview=True
    )