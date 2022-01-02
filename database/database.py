import datetime
import motor.motor_asyncio
import threading

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

def start() -> scoped_session:
    engine = create_engine(Config.MONGODB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()


class Database(BASE):
    __tablename__ = "database"
    id = Column(Integer, primary_key=True)
    msg_id = Column(Integer)
    
    def __init__(self, uri, database_name, id, msg_id):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.clinton = self._client[database_name]
        self.col = self.clinton.USERS
        self.id = id
        self.msg_id = msg_id
        
    def new_user(self, id):
        return dict(id=id, thumbnail=None)


    async def add_user(self, id):
        user = self.new_user(id)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({'id': int(id)})
        return True if user else False

    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        all_users = self.col.find({})
        return all_users

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_thumbnail(self, id, thumbnail):
        await self.col.update_one({'id': id}, {'$set': {'thumbnail': thumbnail}})

    async def get_thumbnail(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('thumbnail', None)
    
    async def df_thumb(id, msg_id):
        msg = SESSION.query(Thumbnail).get(id)
        if not msg:
            msg = Thumbnail(id, msg_id)
            SESSION.add(msg)
            SESSION.flush()
        else:
            SESSION.delete(msg)
            file = Thumbnail(id, msg_id)
            SESSION.add(file)
        SESSION.commit()
    
    async def del_thumb(id):
        msg = SESSION.query(Thumbnail).get(id)
        SESSION.delete(msg)
        SESSION.commit()

   async def thumb(id):
        try:
            t = SESSION.query(Thumbnail).get(id)
            return t
        finally:
            SESSION.close()
