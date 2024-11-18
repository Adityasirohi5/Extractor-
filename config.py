import os
from os import getenv


API_ID = int(getenv("API_ID", "7044734"))
API_HASH = getenv("API_HASH", "3042441d631955272db1358e1d37fefb")
BOT_TOKEN = getenv("BOT_TOKEN", "7273977359:AAHQk4e4r4OOdoG_7jW-C_jp3UQaC3xYJhY")
OWNER_ID = int(getenv("OWNER_ID", "1849310921"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1849310921").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://daxxop:daxxop@daxxop.dg3umlc.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001952953160"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1001952953160"))


#



"""
# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

"""
