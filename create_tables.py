import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

"""
Tworzenie tabel w bazie danych 
------------------------------

Uwagi:
    typ: INTEGER PRIMARY KEY - definiuje kolumnę typu autoincrement
"""

create_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY, 
    username text, 
    password text
)
"""
cursor.execute(create_table)
print('Table users created.')

create_table = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY, 
    name text, 
    price real
)
"""
cursor.execute(create_table)
print('Table items created.')


"""
SEED - dane testowe do bazy danych
"""
# cursor.execute("insert into items values('test',99.99)")
# print('Seed data to items table.')

connection.commit()
connection.close()


