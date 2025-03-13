def handle_help(message):
    help_text = """
    *Comandos disponibles:*
    /start - Iniciar el bot
    /help - Mostrar esta ayuda
    /conclusion - Obtener conclusiones del chat
    /toggle_moderation - Activar/Desactivar moderación
    /list_users - Listar usuarios
    /warn - Advertir a un usuario
    /kick - Expulsar a un usuario
    /stats - Obtener estadísticas del grupo
    /train_ai - Reentrenar modelos de IA
    /search - Buscar información en línea
    /configure - Configurar el bot
    /discuss - Sacar un tema de conversación
    /ask - Responder preguntas conocidas
    """
    bot.send_message(message.chat.id, help_text, parse_mode='Markdown')