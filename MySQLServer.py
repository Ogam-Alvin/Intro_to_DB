import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12767",
    database="alx_book_store"
)

mc= mydb.cursor()
try:
    mc.execute("""  
               CREATE DATABASE IF NOT EXISTS alx_book_store;
                """)
    print('Database has been created')
except:
    print('Database error')

finally:
    mc.close()