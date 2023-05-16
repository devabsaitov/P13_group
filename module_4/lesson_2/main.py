#  aiogram
# pip install aiogram
import logging

from aiogram import Bot , Dispatcher , executor , types

from module_4.lesson_2.test import any_text_handler, test

API_TOKEN = '5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4' # BotFather
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)


dp.register_callback_query_handler(test, lambda msg : msg.text == "start")
dp.register_message_handler(any_text_handler, state = "fullname_set")


# 976658539
if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)






