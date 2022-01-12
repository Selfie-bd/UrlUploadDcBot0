from database.access import db


async def AddUser(bot, update):
    if not await bd.is_user_exist(update.from_user.id):
           await db.add_user(update.from_user.id)
