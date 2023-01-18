import psycopg2
from dotenv.main import load_dotenv
import os

load_dotenv()

some_data = [{'description': ' Nintendo switch oled ', 'price': ' 275€ ', 'img': 'https://cdn.wallapop.com/images/10420/ec/78/__/c10420p867019245/i3091343787.jpg?pictureSize=W320'}, {'description': ' Nintendo switch  ', 'price': ' 300€ ', 'img': 'https://cdn.wallapop.com/images/10420/ec/6a/__/c10420p866975857/i3090876014.jpg?pictureSize=W320'}, {'description': ' Nintendo switch oled ', 'price': ' 270€ ', 'img': 'https://cdn.wallapop.com/images/10420/ec/70/__/c10420p867009440/i3091224603.jpg?pictureSize=W320'}]

def db_read_write(host,db,user,password,port,dataUpload):
    
    try:
    
        conn = psycopg2.connect(f"dbname={db} user={user} password={password} port={port} host={host}")

        cursor = conn.cursor()

        dataInsertionTuples = [
            ('Nintendo64 2024','130£','https://wwww.image-url-is-here.com'),
            ('Nintendo64 2022','5£','https://wwww.wow.com'),
        ]
        
        for d in dataUpload:
            
            data_tuple = (d["description"],d["price"],d["img"])
            
            dataInsertionTuples.append(data_tuple)
        

        dataText = ",".join(cursor.mogrify('(%s,%s,%s)',row).decode("utf-8") for row in dataInsertionTuples)
        SQL = """INSERT INTO nintendo_listings(description,price,img)VALUES {0}""".format(dataText)
        cursor.execute(SQL)
        conn.commit()

        cursor.execute("SELECT * from nintendo_listings")
        rows = cursor.fetchall()

        for row in rows:
            print("ID :",row[0])
            print("Description :",row[1])
            print("Price :",row[2])
            print("Img URL :",row[3])
            print("\n")
        
    except (Exception, psycopg2.Error) as err: 
        print("Error while interacting with PostgreSQL...\n", err)
    
    finally:
        if conn:
            cursor.close()
            conn.close()
    
host = os.environ["POSTGRES_HOST"]
database = "wallapopnintendodb"
user = os.environ["POSTGRES_USER"]
password = os.environ["POSTGRES_PASSWORD"]
port = os.environ["POSTGRES_PORT"]


db_read_write(host,database,user,password,port,some_data)