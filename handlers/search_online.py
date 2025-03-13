def handle_search_online(bot, message):
    query = message.text.partition(' ')[2]
    if not query:
        bot.send_message(message.chat.id, "Por favor, especifica una consulta de búsqueda. Ejemplo: /search consulta")
        return
    bot.send_message(message.chat.id, f"Buscando en línea: {query}")
    # Aquí deberías implementar la lógica para buscar en línea y devolver los resultados