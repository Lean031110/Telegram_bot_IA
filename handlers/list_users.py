def handle_list_users(bot, message):
    chat_id = message.chat.id
    members = bot.get_chat_members(chat_id)
    users = [member.user.username for member in members if member.user.username]
    users_list = "\n".join(users)
    bot.send_message(chat_id, f"Usuarios en el grupo:\n{users_list}")