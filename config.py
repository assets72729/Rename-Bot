import os



# Required Variables Config
API_ID = int(os.environ.get("API_ID", "24890303"))
API_HASH = os.environ.get("API_HASH", "94cf78d1e6883ecb10f32e31fc23cfe0")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", "7289855833"))


# Premium 4GB Renaming Client Config
STRING_SESSION = os.environ.get("STRING_SESSION", "")


# Log & Force Channel Config
FORCE_SUBS = os.environ.get("FORCE_SUBS", "-1002449677578")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002561114141"))


# Mongo DB Database Config
DATABASE_URL = os.environ.get("DATABASE_URL", "")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")


# Other Variables Config
START_PIC = os.environ.get("START_PIC", "https://graph.org/file/ada3f739fed7efdbe7b08.jpg")
