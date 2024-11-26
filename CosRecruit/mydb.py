import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
)

# cursor object + databse creation 
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE MasterList")
print("Database Online.")