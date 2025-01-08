import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(dbname="Shipping", user="postgres", password="postgres", host="localhost", port="5432")
conn.autocommit=True
cursor = conn.cursor()

cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("Shipping")))
cursor.execute(sql.SQL("ALTER DATABASE {} OWNER TO {}").format(sql.Identifier("Shipping"), sql.Identifier("postgres")))
cursor.close()
conn.close()

# db_name = 'Shipping'  
# user = 'postgres'  
# password = 'postgres'