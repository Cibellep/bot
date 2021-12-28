from telegram.ext import Updater, CommandHandler
from config import settings
from commands import send_image
from commands import start
from commands import infinite_image
from commands import stop_loop
from commands import helpp
def main():
    updater = Updater(token=settings.TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("meow", send_image))
    updater.dispatcher.add_handler(CommandHandler("infinite_image", infinite_image))
    updater.dispatcher.add_handler(CommandHandler("stop_loop", stop_loop))
    updater.dispatcher.add_handler(CommandHandler("help", helpp))
    updater.idle()


if __name__ == "__main__":
    main()
