from pyrogram import Client, filters
from pyrogram.types import (
    Message
)
from sample_config import Config
from helper_funcs.client import Client
from helper_funcs.database import db
from plugins.broadcast import broadcast_handler



@Client.on_message(filters.command(["broadcast"]) & filters.user(Config.OWNER_ID) & filters.reply & filters.edited)
async def broadcast_in(_, m: Message):
    await broadcast_handler(m)
