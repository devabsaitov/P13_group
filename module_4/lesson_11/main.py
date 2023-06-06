import logging

import psycopg2
from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook , start_polling
from psycopg2 import ProgrammingError

API_TOKEN = '5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4'
# webhook + ngrok
# webhook settings
WEBHOOK_HOST = 'https://de70-178-218-201-17.ngrok-free.app'
WEBHOOK_PATH = '/dilshod'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3001


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands="start")
async def echo(message: types.Message):
    try:
        con = psycopg2.connect(dbname="asdsfrg", username="postgres", password="2", port=5432 , host="localhost")
        cur = con.cursor()
    except Exception as e:
        logging.error(e)

async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)
    logging.basicConfig(filename="bot_error.log",filemode="a",level=logging.ERROR, format="%(asctime)s  -> %(levelname)s   -> %(message)s")
async def on_shutdown(dp):
    logging.warning('Shutting down..')
    await bot.delete_webhook()
    await dp.storage.close()
    await dp.storage.wait_closed()
    logging.warning('Bye!')

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )