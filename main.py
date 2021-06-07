import random
from telebot import types
from multiprocessing import Process
from datetime import datetime
import test_sender
import test_timer
import time
import telebot
import config

bot = telebot.TeleBot(config.token)

if __name__ == '__main__':

    @bot.message_handler(content_types=["text"])
    def pretty_messages(message):  # Название функции не играет никакой роли
        markup = types.ReplyKeyboardMarkup(True)
        markup.add('порадовать себя)')
        if message.text == 'порадовать себя)':
            bot.send_message(message.chat.id, random.choice(config.array), reply_markup=markup)
            print("press")
    # а теперь запускаем проверку в отдельном потоке

    tm = int(datetime.now().strftime(' %H'))
    if tm != 1 and tm != 2 and tm != 3 and tm != 4 and tm != 5 and tm != 6:
        p2 = Process(target=test_timer.main)
        p2.start()
    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)
            # повторяем через 15 секунд в случае недоступности сервера Telegram
            time.sleep(15)

