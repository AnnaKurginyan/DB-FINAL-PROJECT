import psycopg2
from psycopg2 import sql

def create_database(db_name, db_owner, user, password, host='83.149.198.142', port=5444):

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
    

    cursor.close()
    conn.close()


def connect_to_db(db_name, user, password, host='83.149.198.142', port=5444):
    conn = psycopg2.connect(
        dbname=db_name,  
        user=user,
        password=password,
        host=host,
        port=port
    )
    return conn

def create_table(conn):
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS ships (
        ship_id            SERIAL PRIMARY KEY,
        ship_name          VARCHAR(100),
        ship_type          VARCHAR(100),
        water_displacement INT,
        home_port          INT,
        captain            VARCHAR(100)
        FOREIGN KEY (home_port) REFERENCES port(port_id)
    );
    '''
    cursor.execute(create_table_query)
    print("Table 'ships' created successfully.") 
    cursor.close()


def create_table(conn):
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS visit (
        purpose         VARCHAR(100),
        dock            INT,
        arrival_day     INT,
        departure_day   INT,
        ship            INT,
        port            INT,
        FOREIGN KEY (ship) REFERENCES ships(ship_id),
        FOREIGN KEY (port) REFERENCES port(port_id)
    );
    '''
    cursor.execute(create_table_query)
    print("Table 'visit' created successfully.")
    cursor.close()


def create_table(conn):
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS port (
        port_id          SERIAL PRIMARY KEY,
        port_country     VARCHAR(100),
        port_name        VARCHAR(100),
        one_day_price    INT,
        port_kategory    VARCHAR(100)
    );
    '''
    cursor.execute(create_table_query)
    print("Table 'port' created successfully.")
    cursor.close()

# db_name = 'Shipping'  
# db_owner = 'annaKURG'  
# user = 'annaKURG'  
# password = 'anna27'  
# create_database(db_name, db_owner, user, password)
