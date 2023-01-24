import requests
from dotenv.main import load_dotenv
import os

load_dotenv()

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]

def send_telegram(token,chat_id,message):
    
    url= f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    
    requests.get(url).json()
    
    print("Message sent")
