from datetime import time
import telebot
from telebot import types
import config
import random
from multiprocessing import Process

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    markup = types.ReplyKeyboardMarkup(True)
    markup.add('порадовать себя)')
    if message.text == 'порадовать себя)':
        bot.send_message(message.chat.id, random.choice(config.array), reply_markup=markup)

# # это функция отправки сообщений по таймеру
# def check_send_messages():
#     while True:
#         # ваш код проверки времени и отправки сообщений по таймеру
#         # пауза между проверками, чтобы не загружать процессор
#         time.sleep(60)
#
# # а теперь запускаем проверку в отдельном потоке
# p1 = Process(target=check_send_messages, args=())
# p1.start()
#
# # а это включение бота на прием сообщений
# # обернуто в try, потому что если Telegram сервер станет недоступен, возможен крэш
# while True:
#     try:
#         bot.infinity_polling()
#     except Exception as e:
#         print(e)
#         # повторяем через 15 секунд в случае недоступности сервера Telegram
#         time.sleep(15)


if __name__ == '__main__':
    bot.infinity_polling()
