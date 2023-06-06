import httpx
import json
import redis
import os

import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

API_TOKEN = os.getenv('TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

con = redis.Redis(host=os.getenv("redis_h"), port=os.getenv("redis_p"))



response = httpx.get("https://jsonplaceholder.typicode.com/photos")
dates = json.loads(response.content)[:10]  #
con.set("products", json.dumps(dates))




async def prev_session_next_btn(session):
    prev = InlineKeyboardButton("⬅️prev" , callback_data=f"prev_{session}")
    session_btn = InlineKeyboardButton(f"product - {session + 1}" , callback_data=f"session_{session}")
    next = InlineKeyboardButton("next ➡" , callback_data=f"next_{session}")
    design = [
        [prev , session_btn , next]
    ]
    if not int(session):
        del design[0][0]
    elif int(session) == len(dates) - 1 :
        del design[0][-1]
    return InlineKeyboardMarkup(inline_keyboard=design)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler(commands="pages")
async def echo(message: types.Message, state : FSMContext):
    session_data: dict = dates[0]
    btn = await prev_session_next_btn(0)
    await state.set_state("prev_session_next")
    await message.answer_photo(photo=session_data.get("url"), caption=session_data.get("title"), reply_markup= btn)

@dp.callback_query_handler(state = "prev_session_next")
async def prev_session_next_callback(call: types.CallbackQuery , state: FSMContext):
    operation , session_num = call.data.split("_")
    session_num = int(session_num)
    if operation == "prev":
        session_num -= 1
    elif operation == "next":
        session_num += 1
    else:
        pass
    session_data: dict = dates[session_num]
    btn = await prev_session_next_btn(session_num)
    await call.message.edit_media(InputMediaPhoto(session_data.get("url"), caption=session_data.get("title")), reply_markup=btn)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

