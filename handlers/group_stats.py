import sqlite3

def handle_group_stats(bot, message):
    conn = sqlite3.connect("chat_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM messages")
    total_messages = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM users")
    total_users = cursor.fetchone()[0]

    conn.close()

    bot.send_message(message.chat.id, f"Estadísticas del grupo:\nTotal de mensajes: {total_messages}\nTotal de usuarios: {total_users}")