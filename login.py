import mysql.connection
# Connect to MySQL database
connection = mysql.connector.connect(
    host='localhost',
    database='banking_system',
    user='root',
    password='Delete2006'
)

# Abrir a connection
cursor = connection.cursor()

# Execute a consulta SQL
cursor.execute("SELECT * FROM login")

# Recupere os resultados da consulta
rows = cursor.fetchall()

# Itere sobre os resultados e imprima-os
for row in rows:
    print(row)

cursor.close()
connection.close()
