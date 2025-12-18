import sqlite3
import os
import bcrypt

def get_db_connection():
    # This ensures both scripts talk to the file in the DATA folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(base_dir, "DATA", "intelligence_platform.db")
    return sqlite3.connect(db_path)

def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Using ? placeholders to prevent SQL Injection (Requirement from Slide 1)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, hashed))
        conn.commit()
        conn.close()
        return True, "Registration successful"
    except sqlite3.IntegrityError:
        return False, "Username already exists"

def login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        return True, "Login successful"
    return False, "Invalid username or password"