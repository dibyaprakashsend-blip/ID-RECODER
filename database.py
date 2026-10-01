import sqlite3

# Create/connect to database
connection = sqlite3.connect("id_finder.db")

cursor = connection.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    registration_no TEXT,
    course TEXT,
    abc_id TEXT
)
""")

connection.commit()
connection.close()

print("Database created successfully!")