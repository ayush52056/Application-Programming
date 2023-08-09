# To work with databases in Python, you need to import the appropriate
# modules. The most common module for database connectivity is sqlite3
# for SQLite databases.


import sqlite3

# Connect to a database or create if it doesn't exist

# Use the connect() function to establish a connection to the database.
# Provide the database file path or a connection string.
conn = sqlite3.connect('my_database.db')

# Create a cursor to execute SQL queries
# A cursor is used to execute SQL queries and fetch results.
cursor = conn.cursor()

# Create a table
# Use the cursor to execute SQL queries using the execute() method.
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    age INTEGER
                )''')

# Insert data into the table
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ('Alice', 25))

# Save the changes
# After executing queries that modify the database, you need to commit
# the changes.
conn.commit()

# Close the connection
conn.close()
