import os
import telebot
import datetime
from functions.Returntask import ReturnTask
from Database.QueryTask import queryAll, queryByDate, queryByPriority

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

user = bot.get_me()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Ola, como eu poderia te ajudar no dia de hoje?")


@bot.message_handler(func=lambda m: True)
def send_all_task(message):
    results = ReturnTask(message.text)

    for task in results:
        me = message.chat.id

        bot.send_message(
            me, f'Para o dia: *{task[1]}*, \n{task[2]}', parse_mode='Markdown')


bot.polling()
