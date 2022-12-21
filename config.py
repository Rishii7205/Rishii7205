import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "23043800")) #optional
API_HASH = getenv("API_HASH", "611013e1151a9b80deed3359e53ac853") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5430528255").split()))
OWNER_ID = int(getenv("OWNER_ID", "5662440819"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Yatoo99:Yatoo99@cluster0.3gj7zms.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5862385277:AAHJ_pleWdwUYQtE1aoxC25YVhGQV20hCJI")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQCNO6VbqVsnaunUYIFeIb2Fmt2fMRxstjZ0ysLzIZBfacNHt6B8bNAJlrFnTiZjFGcnCjFiiiWCyXQmNqDuP8wq-juUxsbEtBrsnyIaC4j13Fh_U0Iu-JmeAf0VDle-ZysbHA4JQyAKTHasS7JlDXB85SNGP15v5kwlq5B1DED0RiYNKYgHY3Xfinwzvzuw4qM-7bSmGPJi2H15xhQ6Dg83saSEpx6I4oeErrthZOhfx_GLVMrq0G2KMeXARfeMV8VdyGKy1tyI63GiOyRz33Jqb5OFg_JfEMQTDwdWFL-T7sVyU0Oghv3kejDAhCEiJg5F37SxWd8ZyqhajJVy7YZoAAAAAVGB_XMA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
