import mysql.connector

password = input("Plase enter passsword for MySQL localhost:root")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password
)

cursor = mydb.cursor()
cursor.execute("DROP DATABASE IF EXISTS python")
cursor.execute("CREATE DATABASE python")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=password,
    database="python"
)

cursor = mydb.cursor()
# buffered=True will allow fetchone() function. Otherwise unread result found error raises.
# However cursor.reset() since buffered option gets unused data

cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

cursor.execute("CREATE TABLE users (username VARCHAR(50), password VARCHAR(20))")

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

sqlCode = "INSERT INTO users (username, password) VALUES (%s, %s)"
user1 = ("username1", "password1")

cursor.execute(sqlCode, user1)

users = [
    ("username2", "password2"),
    ("username3", "password3"),
    ("username4", "password4"),
    ]

cursor.executemany(sqlCode, users)

cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)
print(cursor.fetchone())

cursor.execute("SELECT * FROM users")
print(cursor.fetchone())
cursor.reset()

mydb.commit() # To save tables to MySQL
