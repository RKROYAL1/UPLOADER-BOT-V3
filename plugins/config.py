import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6433432360:AAFeEliSERYSYayxJ5Tdubd42DyoEN9SoS8")

    API_ID = int(os.environ.get("API_ID", 28196161))

    API_HASH = os.environ.get("API_HASH" , "7d82be62e09edfc6b7742e88499fb29b" )

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "-1001855426601").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001855426601")

    MAX_FILE_SIZE = 14194304000

    TG_MAX_FILE_SIZE = 14194304000

    FREE_USER_MAX_FILE_SIZE = 14194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @Filmy4capLinktoFile_bot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://filmy4cap:filmy4cap@movies@cluster0.r1ijvlv.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "LinkToFileBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001903071184"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1151303496"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001855426601")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Filmy4capLinktoFile_bot")
