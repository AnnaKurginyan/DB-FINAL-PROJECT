import psycopg2
from psycopg2 import sql


def create_database(db_name, db_owner, user, password, host='172.17.0.2', port=5432):

    conn = psycopg2.connect(
        dbname='postgres',  
        user=user,
        password=password,
        host=host,
        port=port
    )
    
    conn.autocommit = True  
    cursor = conn.cursor()


    create_database = sql.SQL("CREATE DATABASE {} WITH OWNER = {};").format(
        sql.Identifier(db_name),  
        sql.Identifier(db_owner)  
    )
    
    try:
        cursor.execute(create_database)
        print(f"Created successfully. DB_NAME: {db_name}   DB_OWNER: {db_owner}")
    except psycopg2.errors.DuplicateDatabase:
        print(f"Database already exists")
    

    # cursor.close()
    # conn.close()

db_name = 'Shipping'  
db_owner = 'annaKURG'  
user = 'annaKURG'  
password = 'anna27'  
create_database(db_name, db_owner, user, password)

print("exav")
