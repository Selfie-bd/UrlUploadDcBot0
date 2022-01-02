from sample_config import Config
from database.database.database import Database

clinton = Database(Config.MONGODB_URI, "url_bot")
