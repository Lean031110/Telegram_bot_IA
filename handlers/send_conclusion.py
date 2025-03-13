import logging
from learning import analyze_chat

def handle_send_conclusion(bot, message):
    try:
        common_words = analyze_chat()
        if common_words:
            conclusion = "Palabras más comunes:\n" + "\n".join([f"{word}: {count}" for word, count in common_words])
        else:
            conclusion = "No se encontraron datos suficientes para generar conclusiones."
        bot.send_message(message.chat.id, conclusion)
    except Exception as e:
        logging.error(f"Error al generar conclusiones: {e}")
        bot.send_message(message.chat.id, "Hubo un error al generar las conclusiones.")