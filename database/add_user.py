from pyrogram import Client
from database.database import db
from pyrogram.types import Message


async def AddUser(bot, update):
    if not await db.is_user_exist(update.from_user.id):
           await db.add_user(update.from_user.id)
