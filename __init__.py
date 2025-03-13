from .handle_messages import handle_group_messages
from .send_conclusion import handle_send_conclusion
from .welcome_message import handle_welcome_message
from .toggle_moderation import handle_toggle_moderation
from .list_users import handle_list_users
from .warn_user import handle_warn_user
from .kick_user import handle_kick_user
from .group_stats import handle_group_stats
from .train_ai import handle_train_ai
from .search_online import handle_search_online
from .configure_bot import configure_bot, process_document
from .discuss import handle_discuss
from .ask import handle_ask
from .help import handle_help
from .start import handle_start

def register_handlers(bot):
    bot.message_handler(func=lambda message: message.chat.type in ["supergroup", "group"])(lambda message: handle_group_messages(bot, message))
    bot.message_handler(commands=['start'])(lambda message: handle_start(bot, message))
    bot.message_handler(commands=['help'])(lambda message: handle_help(bot, message))
    bot.message_handler(commands=['conclusion'])(lambda message: handle_send_conclusion(bot, message))
    bot.message_handler(content_types=['new_chat_members'])(lambda message: handle_welcome_message(bot, message))
    bot.message_handler(commands=['toggle_moderation'])(lambda message: handle_toggle_moderation(bot, message))
    bot.message_handler(commands=['list_users'])(lambda message: handle_list_users(bot, message))
    bot.message_handler(commands=['warn'])(lambda message: handle_warn_user(bot, message))
    bot.message_handler(commands=['kick'])(lambda message: handle_kick_user(bot, message))
    bot.message_handler(commands=['stats'])(lambda message: handle_group_stats(bot, message))
    bot.message_handler(commands=['train_ai'])(lambda message: handle_train_ai(bot, message))
    bot.message_handler(commands=['search'])(lambda message: handle_search_online(bot, message))
    bot.message_handler(commands=['configure'])(lambda message: configure_bot(bot, message))
    bot.message_handler(commands=['discuss'])(lambda message: handle_discuss(bot, message))
    bot.message_handler(commands=['ask'])(lambda message: handle_ask(bot, message))
    bot.message_handler(content_types=['document'])(lambda message: process_document(bot, message))