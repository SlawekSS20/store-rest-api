import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (" \
               "    id int, " \
               "    username test, " \
               "    password text" \
               ") "
cursor.execute(create_table)

user = (1, "Sławek", "tetsajkljslkj")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

# wstawiam jednego usera...
cursor.execute(insert_query, user)

# wstawiam wielu userów
users = [
    (2, "Jan", "abcder"),
    (3, "Nowak", "abcder"),
    (4, "bob", "asdf"),
]
cursor.executemany(insert_query, users)


select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

# print(cursor.execute(select_query)) # tu wyniku jest Cursor object

connection.commit()
connection.close()
