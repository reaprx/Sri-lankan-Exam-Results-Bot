import telebot

bot = telebot.TeleBot("1664618022:AAEG_LYU49USJpklBe9r4f5T_xhDu2s-F8g")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello I'm a telegram bot created by @reaprx")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
