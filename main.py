
import telebot

token = '1885600223:AAG9Be2lb9uX3-FzkB2xuVBoyEh178FJ4HM'
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text + ", а еще я отень люблю Лизу)💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘💘 и много кутаю))")


if __name__ == '__main__':
     bot.infinity_polling()