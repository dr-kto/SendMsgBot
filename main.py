import eel
import telebot

TOKEN = "1990527566:AAEOHVU71WKFHttlWCWNo9uisa_A8cchrUQ"

bot = telebot.TeleBot(TOKEN)


@eel.expose
def send_message(chat_id, message):
    bot.send_message(chat_id, message)
    return "Cooбщение отправлено!"


eel.init("web")
eel.start("index.html", size = (400, 600), mode="edge")
