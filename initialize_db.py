import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname="Shipping", user="root", password="anna27", host="localhost", port="5432")
conn.autocommit=True
cursor = conn.cursor()

cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("Shipping")))
cursor.execute(sql.SQL("ALTER DATABASE {} OWNER TO {}").format(sql.Identifier("Shipping"), sql.Identifier("root")))
cursor.close()
conn.close()

# db_name = 'Shipping'  
# user = 'root'  
# password = 'anna27'