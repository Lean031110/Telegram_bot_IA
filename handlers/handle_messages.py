import logging
from learning import classify_intent, generate_response, analyze_sentiment, add_messages_to_db

def handle_group_messages(bot, message):
    logging.info(f"Received group message from {message.from_user.username}: {message.text}")
    intent = classify_intent(message.text)
    sentiment = analyze_sentiment(message.text)
    add_messages_to_db([(message.text, intent)])
    response = generate_response(intent)
    bot.send_message(message.chat.id, response)
    logging.info(f"Mensaje guardado: {message.from_user.username}: {message.text} (Intento: {intent}, Sentimiento: {sentiment})")