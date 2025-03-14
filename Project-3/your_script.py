import sqlite3

# Connect to SQLite database (creates library.db if it doesn't exist)
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create books table
cursor.execute('''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL,
    genre TEXT NOT NULL,
    read_status BOOLEAN NOT NULL
)
''')

print("✅ Database and table created successfully!")

# Commit changes and close the connection
conn.commit()
conn.close()
