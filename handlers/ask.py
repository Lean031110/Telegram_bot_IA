from learning import classify_intent, generate_response

def handle_ask(bot, message):
    intent = classify_intent(message.text)
    response = generate_response(intent)
    bot.send_message(message.chat.id, response)