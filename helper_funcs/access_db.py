from sample_config import Config
from helper_funcs.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
