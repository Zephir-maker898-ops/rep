import telebot
from telebot import types
import config
import random
import time

bot = telebot.TeleBot(config.token)



def main():
    @bot.message_handler(content_types=["text"])
    def pretty_messages(message):  # Название функции не играет никакой роли
        markup = types.ReplyKeyboardMarkup(True)
        markup.add('порадовать себя)')
        if message.text == 'порадовать себя)':
            bot.send_message(message.chat.id, random.choice(config.array), reply_markup=markup)

    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)
            # повторяем через 15 секунд в случае недоступности сервера Telegram
            time.sleep(15)


if __name__ == '__main__':
    main()
