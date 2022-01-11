
from sample_config import Config
from plugins.database.database import Database

client = Database(Config.DS_URL, "URL-Uploader")
