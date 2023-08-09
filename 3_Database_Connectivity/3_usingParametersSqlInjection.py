import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Using parameters to avoid SQL injection
student_name = "Bob"
cursor.execute("SELECT * FROM students WHERE name = ?", (student_name,))
row = cursor.fetchone()

if row:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
else:
    print(f"Student with name '{student_name}' not found.")

conn.close()
