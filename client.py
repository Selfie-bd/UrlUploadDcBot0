from typing import Union
from pyromod import listen
from pyrogram import Client
from pyrogram.storage import Storage
from sample_config import Config
from plugins.new import New

LOGGER = Config.LOGGER
log = LOGGER.getLogger(__name__)


class Client(Client, New):
    """ Custom Bot Class """

    def __init__(self, session_name: Union[str, Storage] = "Url-Bot"):
        super().__init__(
            session_name,
            api_id=Config.APP_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(
                root="plugins"
            )
        )

    async def start(self):
        await super().start()
        log.info("Bot Started!")

    async def stop(self, *args):
        await super().stop()
        log.info("Bot Stopped!")
