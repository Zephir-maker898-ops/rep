from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import telebot
import config
import random
from datetime import datetime


bot = telebot.TeleBot(config.token)


async def send_timer():
    tm = int(datetime.now().strftime('%H'))
    if 3 < tm < 22:
        print(tm)
        bot.send_message(config.id_group, random.choice(config.array_text)+random.choice(config.array_smiles))
        print('timer')


def main():
    sched = AsyncIOScheduler(standalone=True)
    sched.add_job(send_timer, 'cron', hour='*', jitter=1800)
    sched.start()
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()
