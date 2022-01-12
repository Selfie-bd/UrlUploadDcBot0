
from sample_config import Config
from database.database import Database

db = Database(Config.MONGODB_URI, "Url-Bot")
