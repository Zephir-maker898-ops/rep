from apscheduler.schedulers.asyncio import AsyncIOScheduler
import asyncio
import telebot
import config
import random
import time

bot = telebot.TeleBot(config.token)


async def send_timer():
    bot.send_message(config.id_group, random.choice(config.array))
    print('timer')

def main():

    sched = AsyncIOScheduler(standalone=True)
    sched.add_job(send_timer, 'cron', hour='*', jitter=3500)
    sched.start()
    asyncio.get_event_loop().run_forever()



if __name__ == '__main__':
    main()

