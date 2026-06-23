import telebot
import os

TOKEN = "8800974001:AAGk0SKaK7-WX4o3kkFVZFyEe4u4T82oKJs"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👑 ربات Taj VPN با موفقیت فعال شد!")

bot.infinity_polling()
