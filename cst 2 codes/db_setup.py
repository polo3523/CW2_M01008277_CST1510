import sqlite3
import os


def setup_database():
    if not os.path.exists('DATA'):
        os.makedirs('DATA')

    conn = sqlite3.connect('DATA/intelligence_platform.db')
    cursor = conn.cursor()

    # Upgraded table for Tier 1 Requirements
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cyber_incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL, 
            severity TEXT NOT NULL,
            status TEXT DEFAULT 'Open',
            date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            date_resolved TIMESTAMP
        )
    ''')

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'Analyst'
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ SUCCESS: New database created with all required columns!")


if __name__ == "__main__":
    setup_database()