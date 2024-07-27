import pickle
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mha53825382",
    database="BookList"
)

cursor = mydb.cursor()
# buffered=True will allow fetchone() function. Otherwise unread result found error raises.
# However cursor.reset() since buffered option gets unused data


cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

""" 
sqlCode = "INSERT INTO users (username, password) VALUES (%s, %s)"
user1 = ("username1", "password1")

cursor.execute(sqlCode, user1)

users = [
    ("username2", "password2"),
    ("username3", "password3"),
    ("username4", "password4"),
    ]

cursor.executemany(sqlCode, users)
"""

""" 
cursor.execute("SELECT * FROM BookInfo")

for row in cursor.fetchall():
    print(row)
print(cursor.fetchone())
 """
cursor.execute("SELECT * FROM BookInfo")
print(cursor.fetchone())
cursor.reset()

with open("ActualData.pkl", "rb") as file:
    for _ in range(6):
        bookList = pickle.load(file)
        for bookTuple in bookList:
            bookString = bookTuple[0]
            if bookTuple[0].find('"') != - 1 or bookTuple[0].find("'") != - 1:
                print(bookTuple[0])
                bookString = bookString.replace('"', r'\"')
                bookString = bookString.replace("'", r"\'")
                print(bookString)
                print()
            cursor.execute(f"""UPDATE BookInfo SET bookPage = {bookTuple[2]}
                           WHERE book = "{bookString}" AND bookPage IS NULL""")

mydb.commit() # To save tables to MySQL