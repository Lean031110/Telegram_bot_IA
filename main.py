import telebot
import logging
import time
from config import TOKEN
from handlers import register_handlers

# Configurar el log de errores y el log detallado
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)

# Inicializar el bot
bot = telebot.TeleBot(TOKEN)

# Registrar todos los manejadores de comandos y eventos
register_handlers(bot)

# Manejo de errores y reconexión automática
def restart_on_error():
    while True:
        try:
            bot.polling()
        except Exception as e:
            logging.error(f"Error en bot.polling(): {e}")
            print("⚠️ Error crítico, reiniciando bot en 5 segundos...")
            time.sleep(5)

# Iniciar el bot con manejo de errores
restart_on_error()