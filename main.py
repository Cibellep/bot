from telegram.ext import Updater, CommandHandler
from config import settings
from commands import send_image, helpp, start


def main():
    updater = Updater(token=settings.TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("meow", send_image))
    updater.dispatcher.add_handler(CommandHandler("help", helpp))
    updater.start_polling()
    updater.idle()
    

if __name__ == "__main__":
    main()
