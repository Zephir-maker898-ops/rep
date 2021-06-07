from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import telebot
import config
import random
import time

bot = telebot.TeleBot(config.token)


def main():
    async def send_timer():
        bot.send_message(config.id_group, random.choice(config.array))

    sched = AsyncIOScheduler()
    sched.add_job(send_timer, 'cron', minute='*', jitter=0.5)
    sched.start()
    asyncio.get_event_loop().run_forever()

    while True:
        try:
            bot.infinity_polling()
        except Exception as e:
            print(e)
            # повторяем через 15 секунд в случае недоступности сервера Telegram
            time.sleep(15)


if __name__ == '__main__':
    main()

