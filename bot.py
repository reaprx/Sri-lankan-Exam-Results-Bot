import telebot

bot = telebot.TeleBot("1664618022:AAF535rU3lB4bq97MhHffLVzqHhJ_lq3bzU")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello I'm a telegram bot create by @reaprx")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
