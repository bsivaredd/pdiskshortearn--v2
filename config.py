import os

API_ID = int(os.environ.get("25856368"))
API_HASH = os.environ.get("7a17467cbfa52b50e22df701e25b37b0")
BOT_TOKEN = os.environ.get("6184655929:AAFWFw2RChw35aTSI8HjI2hGEZpXOfXVh1Q")
METHOD = os.environ.get("METHOD")
PDISKSHORTNEARN_API = os.environ.get("PDISKSHORTNEARN")
MDISK_API = os.environ.get("MDISK_API")
INCLUDE_DOMAIN = os.environ.get("INCLUDE_DOMAIN")
EXCLUDE_DOMAIN = os.environ.get("EXCLUDE_DOMAIN")
CHANNEL_ID = list(int(i.strip()) for i in os.environ.get("1001708519278").split(" ")) if os.environ.get("1001708519278") else []
FORWARD_MESSAGE = bool(os.environ.get("FORWARD_MESSAGE"))
ADMINS = list(int(i.strip()) for i in os.environ.get("ADMINS").split(",")) if os.environ.get("ADMINS") else []
SOURCE_CODE = "https://github.com/bsivaredd/pdiskshortearn--v2/blob/master/config.py"
CHANNELS = bool(os.environ.get("CHANNELS"))
USERNAME = os.environ.get("USERNAME")
REMOVE_EMOJI = os.environ.get('REMOVE_EMOJI', False)
