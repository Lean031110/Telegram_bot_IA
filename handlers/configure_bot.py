import logging
import os
from telebot import types
from learning import process_word_document, process_excel_document, add_messages_to_db, retrain_models

def configure_bot(bot, message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('/train_ai')
    btn2 = types.KeyboardButton('/toggle_moderation')
    btn3 = types.KeyboardButton('/list_users')
    btn4 = types.KeyboardButton('/stats')
    btn5 = types.KeyboardButton('/conclusion')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, "Configuración del bot:", reply_markup=markup)

def process_document(bot, message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        file_path = os.path.join("downloads", message.document.file_name)
        os.makedirs("downloads", exist_ok=True)
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        if file_path.endswith(".docx"):
            messages = process_word_document(file_path)
        elif file_path.endswith(".xlsx"):
            messages = process_excel_document(file_path)
        else:
            bot.send_message(message.chat.id, "Formato de archivo no soportado. Solo se permiten archivos .docx y .xlsx")
            return

        add_messages_to_db(messages)
        retrain_models()
        bot.send_message(message.chat.id, "Documento procesado y modelos reentrenados correctamente.")

    except Exception as e:
        logging.error(f"Error al procesar el documento: {e}")
        bot.send_message(message.chat.id, "Hubo un error al procesar el documento.")