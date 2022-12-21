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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQFfntgAFQ-B3tQm_DSGhubPLZih0ztSlXrpjczIYIxzZNIHjYNvYDBBLmxjT5GDoQAV4QDuVHlKMzQEt1Nd2WlhCjgzKvG3357fxHgFO5HK4uVgEEv5HpmVP4qzRjVRWQXQD4Cza58nkA0gBtsb0OAJCkCnkw5VnIl6hbkYWMUP3vKZ7VxF_-AxLftoKsWEUHZYRUyMwYnXJFJrBny8UbhBR1-ZPsU_s6JbCRbGazYt9fe8Rqf70cJV9dc1wERgkpzfx5NJ6FIGDPLrfL8MMtLe8WLHSbftMu24dbASYh0eiIiTwowTJjPmpCNz9cAYjHq4xHp7I96deDF492SSS6fQGyXN1AAAAAFRgf1zAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
