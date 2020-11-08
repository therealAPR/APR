import telebot

bot = telebot.TeleBot("1160619272:AAE-xoEL3Atg3UUiQ6Vy-NQtPlvuYguVI6o", parse_mode=None) # You can set

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Howdy, how are you doing?")
