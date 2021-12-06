import telebot


bot = telebot.TeleBot("5045845144:AAGd0RCScb3y_0qjOA47zD_wRx8M48n4qXQ", parse_mode="MarkdownV2")


@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot")


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.reply_to(message, message.text)


bot.polling()