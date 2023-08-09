import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

try:
    # Begin a transaction
    conn.execute("BEGIN")

    # Insert multiple records
    cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", [
        ('John', 22),
        ('Mary', 24),
        ('Tom', 20),
    ])

    # Commit the transaction if everything is successful
    conn.execute("COMMIT")

except Exception as e:
    # Rollback the transaction on error
    conn.execute("ROLLBACK")
    print(f"Error: {e}")

conn.close()
