import sqlite3

def init_db():
    # Connect to SQLite database (Create if it doesn't exist)
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    #Create a table for storing user login data
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

init_db()
print("Database and 'users' table created successfully.")