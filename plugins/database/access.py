from sample_config import Config
from plugins.database.database import Database

clinton = Database(Config.DB_URI, Config.SESSION_NAME)
