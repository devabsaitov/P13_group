
import logging

from aiogram import Bot , Dispatcher , executor , types
from aiogram.contrib.fsm_storage.memory import MemoryStorage


from module_4.lesson_2.login.functions import start_handler, username_handler, password_handler

API_TOKEN = '5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4' # BotFather
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


# ============== login handlers ================================
dp.register_message_handler(start_handler ,commands='start')
dp.register_message_handler(username_handler, state = "username_set")
dp.register_message_handler(password_handler, state = "password_set")

# ==============================================================


if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)

