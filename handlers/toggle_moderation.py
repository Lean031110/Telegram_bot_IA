MODERATION_ENABLED = False

def handle_toggle_moderation(bot, message):
    global MODERATION_ENABLED
    MODERATION_ENABLED = not MODERATION_ENABLED
    status = "activada" if MODERATION_ENABLED else "desactivada"
    bot.send_message(message.chat.id, f"La moderación ha sido {status}.")