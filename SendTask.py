import os
import telebot
import datetime

from QueryTask import queryAll, queryByDate, queryByPriority

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

user = bot.get_me()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ola, como eu poderia te ajudar no dia de hoje?")


@bot.message_handler(func=lambda m: True)
def send_all_task(message):
    if message.text == 'All':
        results = queryAll()

    elif message.text == 'Today' or 'Hoje':
        today = datetime.date.today()
        d1 = today.strftime("%d.%m")
        date = float(d1)

        results = queryByDate(date)

    elif message.text == 'Yesterday' or 'Ontem':
        today = datetime.date.today()
        d1 = today.strftime("%d.%m")
        date = float(d1) - 1

        results = queryByDate(date)

    else:
        try:
            date = float(message.text)

            results = queryByDate(date)

        except:
            priority = message.text

            results = queryByPriority(priority)

    for task in results:

        bot.reply_to(message, task[2])


bot.polling()
