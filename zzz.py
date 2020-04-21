import logging
from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
updater = Updater(token='TOKEN', use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()
