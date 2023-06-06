import logging
from datetime import timedelta

from aiogram import Bot, Dispatcher, executor, types
import redis
API_TOKEN = '5888421916:AAFIQ0K73hAwKdAkBxuDZv83TlSF_VBw1rU'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
con = redis.Redis(host='localhost' , port=6379)



@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    if con.get(f"{message.from_user.id}"):
        await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
        con.set(f"{message.from_user.id}", message.from_user.first_name, ex=timedelta(seconds=10))
    else:
        await message.answer("Login qilindi ")
        con.set(f"{message.from_user.id}" ,message.from_user.first_name,ex=timedelta(seconds=10))




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)