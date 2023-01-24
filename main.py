from wallapop_scrape import wallapopScrape
from postgres_read_write import db_read_write
from telegram_bot import send_telegram
from dotenv.main import load_dotenv
import os
import datetime

load_dotenv()

# PosgresSQL Environment Variables
host = os.environ["POSTGRES_HOST"]
database = "wallapopnintendodb"
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
port = os.environ["POSTGRES_PORT"]

# Telegram Environment Variables
token = os.environ["TELEGRAM_TOKEN"]
chat_id = os.environ["CHAT_ID"]


# scrape wallapop
results = wallapopScrape("https://es.wallapop.com/app/search?category_ids=12900&keywords=nintendo&latitude=41.38804&longitude=2.17001&filters_source=quick_filters&object_type_ids=10088&order_by=newest")


# establish new listings and update database 
new_listings = db_read_write(host,database,user,password,port,results)



# telegram if no new listings
if len(new_listings) == 0:
    send_telegram(token,chat_id,"No New Listings Found")

# telegram if new listings
if len(new_listings) > 0:
    
    send_telegram(token,chat_id,"New Listings Found")
    
    time_now = datetime.datetime.now()
    time_format = time_now.strftime("%d/%m/%Y - %H:%M")
    
    new_line = "\n"
    message = f"Hello Adam, your new listings at {time_format} are: \n {new_line.join(map(str,new_listings))}"
    send_telegram(token,chat_id,message)






