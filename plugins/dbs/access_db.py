# (c) @Satyamurthi

from sample_config import Config
from plugind.dbs.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
