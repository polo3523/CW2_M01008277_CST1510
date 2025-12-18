import sqlite3
import pandas as pd

def create_user_table(conn):
    curr = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    );
    """
    curr.execute(sql)
    conn.commit()

def add_user(conn, name, password):
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password) VALUES (?, ?)"
    curr.execute(sql, (name, password))
    conn.commit()

def migrate_users(conn):
    with open('data/users.txt') as f:
        for user in f:
            name, password = user.strip().split(',')
            add_user(conn, name, password)

def get_all_users(conn):
    curr = conn.cursor()
    curr.execute("SELECT * FROM users")
    return curr.fetchall()

def migrate_cyber_incidents():
    cyber = pd.read_csv('data/cyber_incidents.csv')
    conn = sqlite3.connect('data/cyber_incidents.db')
    cyber.to_sql('cyber_incidents', conn, index=False, if_exists='replace')
    conn.close()
    print('Migrated all cyber incidents to database.')

# -----------------------------
# MAIN
# -----------------------------

conn = sqlite3.connect('data/intelligence_platform.db')

create_user_table(conn)
migrate_users(conn)

print(get_all_users(conn))

conn.close()
