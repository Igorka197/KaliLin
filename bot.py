import telebot

# Вставь сюда свой токен от @BotFather
bot = telebot.TeleBot("8757333957:AAGjk6cUQBWZJ1zT4xhdnvJWysm2-goHgys")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой личный бот, работающий на серверах GitHub! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Ты написал: {message.text}")

if __name__ == '__main__':
    print("Бот запущен и работает!")
    bot.infinity_polling()
