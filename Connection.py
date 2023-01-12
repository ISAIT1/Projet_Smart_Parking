import mysql
from mysql import connector

con = mysql.connector.connect(
    user="root",
    password="",
    port=3308,
    host="localhost",
    database="smart_parking")
cursor = con.cursor()
cursor.execute('SELECT * FROM admin')
data = cursor.fetchall()
for d in data:
    print(con)
con.close()
