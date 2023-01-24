import requests
from dotenv.main import load_dotenv
import os

load_dotenv()

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]
url = f"https://api.telegram.org/bot{token}/getUpdates"


# get messages
print(requests.get(url).json())

# send messages
url2= f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text=Hello Adam, Testing"
    
requests.get(url2).json()