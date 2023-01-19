from wallapop_scrape import wallapopScrape
from postgres_read_write import db_read_write
from telegram_bot import send_telegram
from dotenv.main import load_dotenv
import os

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


results = wallapopScrape("https://es.wallapop.com/app/search?category_ids=12900&keywords=nintendo&latitude=41.38804&longitude=2.17001&filters_source=quick_filters&object_type_ids=10088&order_by=newest")

new_listings = db_read_write(host,database,user,password,port,results)
list_length = len(new_listings)


if len(new_listings) > 0:
    send_telegram(token,chat_id,new_listings)






