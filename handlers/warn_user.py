def handle_warn_user(bot, message):
    if not message.reply_to_message:
        bot.send_message(message.chat.id, "Por favor, responde al mensaje del usuario al que quieres advertir.")
        return
    warned_user = message.reply_to_message.from_user
    bot.send_message(message.chat.id, f"{warned_user.first_name}, has sido advertido por {message.from_user.first_name}.")