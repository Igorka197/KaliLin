import os
import telebot

# Вставь свой токен строго внутри кавычек!
TOKEN = "8757333957:AAGjk6cUQBWZJ1zT4xhdnvJWysm2-goHgys"

if not TOKEN or TOKEN == "8757333957:AAGjk6cUQBWZJ1zT4xhdnvJWysm2-goHgys":
    print("ОШИБКА: Ты не вставил токен от @BotFather в код!")
    exit()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой личный бот на серверах GitHub! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

print("Бот успешно запущен! Иду в Телегу...")
bot.infinity_polling()
