from sample_config import Config
from plugins.database.database import Database

clinton = Database(Config.MONGODB_URI, Config.SESSION_NAME)
