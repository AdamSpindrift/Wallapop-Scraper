import psycopg2
from dotenv.main import load_dotenv
import os

load_dotenv()

#some_data = [{'description': ' Nintendo switch oled ', 'price': ' 275€ ', 'img': 'https://cdn.wallapop.com/images/10420/ec/78/__/c10420p867019245/i3091343787.jpg?pictureSize=W320'}, {'description': ' Nintendo switch  ', 'price': ' 300€ ', 'img': 'https://cdn.wallapop.com/images/10420/ec/6a/__/c10420p866975857/i3090876014.jpg?pictureSize=W320'}, {'description': ' Nintendo switch oled ', 'price': ' 270€ ', 'img': 'https://cdn.wallapop.com/images/10420/ec/70/__/c10420p867009440/i3091224603.jpg?pictureSize=W320'}]

def db_read_write(host,db,user,password,port,dataUpload):
    
    try:
    
        conn = psycopg2.connect(f"dbname={db} user={user} password={password} port={port} host={host}")

        cursor = conn.cursor()
        
        cursor.execute("SELECT * from nintendo_listings")
        rows = cursor.fetchall()
        current_rows = []
        
        for r in rows:
            r1 = list(r)
            r1.pop(0)
            current_rows.append(r1)
        
        scraped_tuples = []
        
        for d in dataUpload:
            
            data_tuple = (d["description"],d["price"],d["img"])
            
            scraped_tuples.append(data_tuple)
         
        scraped_list = []
        
        for i in scraped_tuples:
            i1 = list(i)
            scraped_list.append(i1)
               
        dataInsertionTuples = []
        
        for i, s in enumerate(scraped_list):
            #print(i)
            if scraped_list[i] in current_rows:
                print("Match Found")
            else:
                print("New Listing")
                dataInsertionTuples.append(scraped_tuples[i])
        
        
        if len(dataInsertionTuples) > 0 :
            dataText = ",".join(cursor.mogrify('(%s,%s,%s)',row).decode("utf-8") for row in dataInsertionTuples)
            SQL = """INSERT INTO nintendo_listings(description,price,img)VALUES {0}""".format(dataText)
            cursor.execute(SQL)
            conn.commit()
        else:
            print("No New Listings")

        
    except (Exception, psycopg2.Error) as err: 
        print("Error while interacting with PostgreSQL...\n", err)
    
    finally:
        if conn:
            cursor.close()
            conn.close()
            
        return dataInsertionTuples