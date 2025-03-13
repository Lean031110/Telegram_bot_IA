def handle_welcome_message(bot, message):
    for new_member in message.new_chat_members:
        bot.send_message(message.chat.id, f"¡Bienvenido {new_member.first_name}!")