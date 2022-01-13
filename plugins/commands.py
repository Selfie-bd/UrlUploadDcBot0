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


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(bot, update):
    await update.reply_text(
        text=Translation.HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=Translation.HELP_BUTTONS
    )

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(bot, update):
    await update.reply_text(
        text=Translation.ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=Translation.ABOUT_BUTTONS
    )

@Client.on_message(filters.command(["donate"]) & filters.private)
async def dobate(bot, update):
        await update.message.edit_text(
            text=Translation.DONATE_TEXT,
            reply_markup=Translation.DONATE_BUTTONS,
            disable_web_page_preview=True
    )
