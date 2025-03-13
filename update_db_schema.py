import sqlite3

DB_NAME = "chat_data.db"

def update_schema():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Crear tabla messages si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        message TEXT,
        intent TEXT,
        sentiment TEXT
    )
    """)

    # Verificar si la columna 'intent' existe, si no, agregarla
    cursor.execute("PRAGMA table_info(messages)")
    columns = [column[1] for column in cursor.fetchall()]
    if 'intent' not in columns:
        cursor.execute("ALTER TABLE messages ADD COLUMN intent TEXT")

    # Verificar si la columna 'sentiment' existe, si no, agregarla
    if 'sentiment' not in columns:
        cursor.execute("ALTER TABLE messages ADD COLUMN sentiment TEXT")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_schema()
    print("Esquema de la base de datos actualizado correctamente.")