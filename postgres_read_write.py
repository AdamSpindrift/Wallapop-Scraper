import psycopg2
from dotenv.main import load_dotenv
import os

load_dotenv()

def db_read_write(host,db,user,password,port):
    
    conn = psycopg2.connect(f"dbname={db} user={user} password={password} port={port} host={host}")
    
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM information_schema.tables')
    rows = cursor.fetchall()
    for table in rows:
        print(table)
        
        
    conn.close()
    
host = os.environ["POSTGRES_HOST"]
database = "wallapopnintendodb"
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
port = os.environ["POSTGRES_PORT"]


db_read_write(host,database,user,password,port)