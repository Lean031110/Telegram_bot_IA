def handle_kick_user(bot, message):
    if not message.reply_to_message:
        bot.send_message(message.chat.id, "Por favor, responde al mensaje del usuario al que quieres expulsar.")
        return
    user_to_kick = message.reply_to_message.from_user
    bot.kick_chat_member(message.chat.id, user_to_kick.id)
    bot.send_message(message.chat.id, f"{user_to_kick.first_name} ha sido expulsado del grupo.")