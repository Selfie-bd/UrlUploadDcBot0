import os
import logging
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    # The Telegram API things
    # Get these values from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")
    
    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
    
    DATABASE_URI = environ.get('DATABASE_URI', "")
    DATABASE_NAME = environ.get('DATABASE_NAME', "Rajappan")

    #Session Name
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    
    #Owner ID
    BOT_OWNER = os.environ.get("BOT_OWNER", "1307550350")
    
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    
    #OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split())

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    #CHUNK_SIZE = 128

    # Generate screenshots for file after uploading
    # Defaults to True
    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
    
    # Log channel for banning spammers
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100"))
    
    LOGGER = logging

    # maximum message length in Telegram
    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = int(os.environ.get("TIME_LIMIT"))
    
    # dict to hold the ReQuest queue
    ADL_BOT_RQ = {}

    # watermark file
    DEF_WATER_MARK_FILE = ""

    # Sql Database url
    DB_URI = os.environ.get("DATABASE_URL", "")
    
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    # Banned Unwanted Members..
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
    
    #Broadcast
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
