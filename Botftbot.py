from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Replace 'YOUR_API_TOKEN' with your bot's API token
API_TOKEN = '7153583503:AAEzqUTYxjIKYghEvEb6rCsW453xXpeDYUc'

def start(update, context):
    update.message.reply_text('Hello! I am your new bot. How can I assist you?')

def help_command(update, context):
    update.message.reply_text('You can use /start to start the bot and /help to get this message.')

def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(API_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # On non-command i.e. message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
