import psycopg2

def db_read_write(host,db,user,password,port):
    
    conn = psycopg2.connect(
        host = host,
        database = db,
        user = user,
        password = password,
        port = port,
    )
