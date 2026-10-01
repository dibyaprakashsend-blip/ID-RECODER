import sqlite3

# Example data extracted from OCR
name = "DIBYA PRAKASH SEND"
regd_no = "2501020425"
course = "B.Tech.(CSE:AI & M.L.)"
abc_id = "888914008091"

# Connect to database
connection = sqlite3.connect("id_finder.db")

cursor = connection.cursor()

# Insert data
cursor.execute("""
INSERT INTO students (name, registration_no, course, abc_id)
VALUES (?, ?, ?, ?)
""", (name, regd_no, course, abc_id))

# Save changes
connection.commit()

# Close database
connection.close()

print("Student information saved successfully!")    