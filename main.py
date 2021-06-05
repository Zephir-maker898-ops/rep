import telebot
from telebot import types

import config
import random



bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
        markup = types.ReplyKeyboardMarkup(True)
        markup.add('порадовать себя)')
        bot.send_message(message.chat.id, random.choice(config.array), reply_markup=markup)




if __name__ == '__main__':
    bot.infinity_polling()
