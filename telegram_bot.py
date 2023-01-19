import requests
from dotenv.main import load_dotenv
import os
import datetime

load_dotenv()

token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]

def send_telegram(token,chat_id,listings):
    
    time_now = datetime.datetime.now()
    time_format = time_now.strftime("%d/%m/%Y - %H:%M")

    #Send Message
    new_line = "\n"
    message = f"Hello Adam, your new listings at {time_format} are: \n {new_line.join(map(str,listings))}"
    
    url= f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
    
    requests.get(url).json()
    
    print("New listings sent")
