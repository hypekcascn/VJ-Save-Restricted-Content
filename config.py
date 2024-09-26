import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("28643757", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("48bc23636469ce76a865b3fbea6e6661", "")

#Database 
DB_URI = os.environ.get("mongodb+srv://alokpatel9506:<db_g37OafBqfXrqwXgJ>@cluster0.7cgra.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", "")
