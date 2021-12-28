from telegram.ext import Updater
import httpx
from config import settings


def start(update, context):
    message = (
        "Eu sou um bot que irá disponibilizar imagens de "
        "gatinhos para tornar seu dia mais feliz. \n\n"
        "Comandos: \n\n"
       
        "/start - inicia o bot \n"
        "/help - lista os comandos \n"
        "/meow - envia uma foto de gatinho \n"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def helpp(update, context):
    messagem = (
        "Comandos para usar no bot: \n"
        "/start - inicia o bot \n"
        "/help - lista os comandos \n"
        "/meow - envia uma foto de gatinho \n"
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=messagem)


def send_image(update, context):
    contents = httpx.get(settings.API_URL)
    url_photo = contents.json()[0]["url"]
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url_photo)