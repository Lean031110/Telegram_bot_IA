from learning import initiate_conversation

def handle_discuss(bot, message):
    topic = initiate_conversation()
    bot.send_message(message.chat.id, f"Tema de conversación: {topic}")