from telegram.ext import Updater
import httpx
from config import settings


def start(update, context):
    message = (
        "Eu sou um bot que irá disponibilizar imagens de "
        "gatinhos para tornar seu dia mais feliz. \n\n"
        "Comandos: \n"
        "/meow - fasfds asdfsf  asfsadf"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def helpp(update, context):
    messagem = (
        "Comandos para usar no bot: \n"
        "/start - inicia o bot"
        "/help - lista os comandos"
        "/meow - envia uma foto de gatinho"
        "/infinite_image - envia continuamente fotos de gatinho"
        "/stop_loop - Para o envio de fotos de gatinho"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=messagem)


def send_image(update, context):
    contents = httpx.get(settings.API_URL)
    url_photo = contents.json()[0]["url"]
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url_photo)

def infinite_image(update, context):
    while True:
        send_image(update, context)

def stop_loop(update, context):
    Updater.stop()