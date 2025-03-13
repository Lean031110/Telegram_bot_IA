from learning import retrain_models

def handle_train_ai(bot, message):
    retrain_models()
    bot.send_message(message.chat.id, "Modelos de IA reentrenados con éxito.")