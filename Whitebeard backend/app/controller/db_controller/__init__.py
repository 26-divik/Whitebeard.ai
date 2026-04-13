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
                  email TEXT UNIQUE NOT NULL,
                  password TEXT NOT NULL,
                  name TEXT NOT NULL)''')
    conn.commit()
    conn.close()


def _ensure_users_table_schema():
    c, conn = get_cursor()
    try:
        c.execute("PRAGMA table_info(users)")
        columns = [row[1] for row in c.fetchall()]

        # Migrate legacy schema that still contains username.
        if 'username' in columns:
            c.execute('''CREATE TABLE users_new
                         (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          email TEXT UNIQUE NOT NULL,
                          password TEXT NOT NULL,
                          name TEXT NOT NULL)''')
            c.execute('''INSERT INTO users_new (id, email, password, name)
                         SELECT id, email, password, name FROM users''')
            c.execute("DROP TABLE users")
            c.execute("ALTER TABLE users_new RENAME TO users")
            conn.commit()
    finally:
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
    else:
        _ensure_users_table_schema()