import psycopg2
from dotenv.main import load_dotenv
import os
import datetime

load_dotenv()


def db_read_write(host,db,user,password,port,dataUpload):
    
    try:
    
        conn = psycopg2.connect(f"dbname={db} user={user} password={password} port={port} host={host}")

        cursor = conn.cursor()
        
        cursor.execute("SELECT * from nintendo_listings")
        rows = cursor.fetchall()
        current_rows = []
        
        time_now = datetime.datetime.now()
        time_format = time_now.strftime("%Y-%m-%d")
        
        for r in rows:
            r1 = list(r)
            r1.pop(0)
            current_rows.append(r1)
        
        scraped_tuples = []
        
        for d in dataUpload:
            
            data_tuple = (d["description"],d["price"],d["img"],time_format)
            
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
            dataText = ",".join(cursor.mogrify('(%s,%s,%s,%s)',row).decode("utf-8") for row in dataInsertionTuples)
            SQL = """INSERT INTO nintendo_listings(description,price,img,date)VALUES {0}""".format(dataText)
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