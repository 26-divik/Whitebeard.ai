import sqlite3
from app.controller.db_controller import get_cursor
def check_user_exists(username, email):
    c, conn = get_cursor()

    c.execute("SELECT * FROM users WHERE username = ?", (username,))
    user_by_username = c.fetchone()

    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    user_by_email = c.fetchone()

    conn.close()

    return (user_by_username, user_by_email)
def add_user(username, email, password, name):
    username = username.strip().lower()
    email = email.strip().lower()
    password = password
    name = name.strip().lower()
    c, conn = get_cursor() 
    try:
        c.execute('''INSERT INTO users (username, email, password, name) VALUES (?, ?, ?, ?)''',
                  (username, email, password, name))
        conn.commit()
        return True, "User inserted successfully"
    except sqlite3.IntegrityError as e:
        return False, f"Error inserting user: {str(e)}"
    finally:
        conn.close()