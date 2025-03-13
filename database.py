import sqlite3

DB_NAME = "chat_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            message TEXT,
            intent TEXT,
            sentiment TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def save_message(user, message, intent=None, sentiment=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO messages (user, message, intent, sentiment) VALUES (?, ?, ?, ?)", (user, message, intent, sentiment))
    
    conn.commit()
    conn.close()

def get_messages():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    
    conn.close()
    return messages
