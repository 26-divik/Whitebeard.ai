import sqlite3


def get_cursor():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    return c, conn


def create_users_table():
    c, conn = get_cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  name TEXT NOT NULL)''')
    conn.commit()
    conn.close()


def initialize_database():
    c, conn = get_cursor()
    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        users_table_exists = c.fetchone() is not None
    finally:
        conn.close()

    if not users_table_exists:
        create_users_table()