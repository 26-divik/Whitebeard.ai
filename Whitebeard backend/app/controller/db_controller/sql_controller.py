import sqlite3
from app.controller.db_controller import get_cursor
def get_user_by_email(email):
    c, conn = get_cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = c.fetchone()

    conn.close()
    if not row:
        return None

    return {
        "id": row[0],
        "email": row[1],
        "password": row[2],
        "name": row[3]
    }
def add_user (email, password, name):
    email = email.strip().lower()
    password = password
    name = name.strip().lower()
    c, conn = get_cursor() 
    try:
        c.execute('''INSERT INTO users (email, password, name) VALUES (?, ?, ?)''',
                  (email, password, name))
        conn.commit()
        return True, "User inserted successfully"
    except sqlite3.IntegrityError as e:
        return False, f"Error inserting user: {str(e)}"
    finally:
        conn.close()
        
def get_user_by_id(user_id):
    c, conn = get_cursor()
    c.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    row = c.fetchone()

    conn.close()
    if not row:
        return None

    return {
        "id": row[0],
        "email": row[1],
        "password": row[2],
        "name": row[3]
    }