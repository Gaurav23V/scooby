import sqlite3
import uuid
from datetime import datetime

def init_db():
    conn = sqlite3.connect('conversation.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            role TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_message(session_id, role, content):
    conn = sqlite3.connect('conversation.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO messages (session_id, role, content)
        VALUES (?, ?, ?)
    ''', (session_id, role, content))
    conn.commit()
    conn.close()

def get_session_history(session_id):
    conn = sqlite3.connect('conversation.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT role, content FROM messages
        WHERE session_id = ?
        ORDER BY timestamp ASC
    ''', (session_id,))
    messages = cursor.fetchall()
    conn.close()
    return messages