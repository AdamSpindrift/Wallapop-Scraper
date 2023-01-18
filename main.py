from wallapop_scrape import wallapopScrape
from postgres_read_write import db_read_write
from dotenv.main import load_dotenv
import os

load_dotenv()

results = wallapopScrape("https://es.wallapop.com/app/search?category_ids=12900&keywords=nintendo&latitude=41.38804&longitude=2.17001&filters_source=quick_filters&object_type_ids=10088")

#print(results)

host = os.environ["POSTGRES_HOST"]
database = "wallapopnintendodb"
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
port = os.environ["POSTGRES_PORT"]

newListings = db_read_write(host,database,user,password,port,results)




