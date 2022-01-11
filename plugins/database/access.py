
from sample_config import Config
from database.database import Database

clinton = Database(Config.MONGODB_URI, "URL-Uploader")
