import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Query all records from the table
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

# Process and print the results
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

conn.close()
