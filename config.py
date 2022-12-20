import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "25394191")) #optional
API_HASH = getenv("API_HASH", "256fcc3280c94ecda7dee238a08c02c7") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5430528255").split()))
OWNER_ID = int(getenv("OWNER_ID", "5697261678"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Yatoo99:Yatoo99@cluster0.3gj7zms.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5888020629:AAGrGHbIV4lO_25ti6KGcNdy12Atm3X62as")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQAg6gSl7th0nqokOTATzeBgln4x2Cul2Y2mdmKfQiIxXmAJoiWqQ64EkiQ27U4ASVYQsN-UeCphJaA21_7Uu36b7YFXjMtJ1rUZeq7KYAI5ludi2OznC_aPyLjT0Xx3g83B_275JfJl-DG4B8cgJ41Ul-zDieBRFvEXC4C1OXliOY4qjJxsCkaEqwEJ23uZuItbvUQru0WH0Xx7jvJ9QffciafgYCsrgkGTnmUmCYwgV36FdmwcJ16FC6p9rTccbqrG1L5tJ2Q7CeBtDDPOFzQEeHHQUmB92WmoNDOhEibJWXVjfTabF8rb5HmDWM8vaE-1OfyTCE2MzwgRz5NxcFopAAAAAVOVUG4A")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
