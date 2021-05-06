
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import BOT_TOKEN
from geocoder import *

# Asking user to send location
def start_message(update, context):

    update.message.reply_text('Пришли свою локацию:')


# 1) Receiving location in dict ('latitude': value, 'longitude': value)
# 2) Parsing values and send them to geocoder()
# 3) Taking back data in tuple()
# 4) Convert and reformat data to string
# 5) Send answer to user
def location(update, context):

    message = update.message
    current_position = (message.location.latitude, message.location.longitude)
    current_position = geocoder(current_position)

    if current_position is None:
        update.message.reply_text("Рядом с тобой нет паркинга :(")

    else:
        position = str(current_position)
        update.message.reply_text(f"""Ближайший паркинг находится здесь:\n{position.strip("(,)").replace("'", "")}""")

# 1) Activating bot and specifying bot_token
# 2) Creating event logger to understand which func we need to use
# 3) Logging "start" and "location" functions
# 4) Starting bot
def main():

    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_message))
    dispatcher.add_handler(MessageHandler(Filters.location, location))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()