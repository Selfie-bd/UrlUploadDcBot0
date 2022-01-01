from sample_config import Config
from database.database import Database

clinton = Database(Config.DB_URI, Config.SESSION_NAME)
