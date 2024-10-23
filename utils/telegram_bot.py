import telebot
from django.conf import settings


bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

def send_telegram_message(chat_id, message):
    bot.send_message(chat_id, message)