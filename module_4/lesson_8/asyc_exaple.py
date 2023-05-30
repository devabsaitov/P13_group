import asyncio

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# 5627792337
async def send_welcome():
    for i in range(10):
        await bot.send_message(5627792337,"Hi!\nI'm EchoBot!\nPowered by aiogram.")

asyncio.run(send_welcome())