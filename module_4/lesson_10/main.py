#
# import redis
#
# redis_con = redis.Redis(host="localhost", port=6379, decode_responses=True)
# redis_con1 = redis.Redis(host="localhost", port=6381, decode_responses=True)
# redis_con2 = redis.Redis(host="localhost", port=6382, decode_responses=True)
# redis_con3 = redis.Redis(host="localhost", port=6383, decode_responses=True)
#
# redis_con.set("1" , "10")
# redis_con1.set("1" , "11")
# redis_con2.set("1" , "12")
# redis_con3.set("1" , "13")
#
# print(redis_con.get("1"))
# print(redis_con1.get("1"))
# print(redis_con2.get("1"))
# print(redis_con3.get("1"))


import redis
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto

con = redis.Redis(host='localhost', port = 6380,decode_responses=True)

import logging
from aiogram import Bot, Dispatcher, executor, types
#
API_TOKEN = '5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4'
#
logging.basicConfig(level=logging.INFO)
#
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
datas = []
data = con.keys()
for i in data:
    datas.append(con.hgetall(i))

#
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")
#
def pagenation(data_id):

    prev = InlineKeyboardButton("prev", callback_data=f"prev_{data_id}")
    session_data = InlineKeyboardButton(data_id, callback_data=f"session_{data_id}")
    next = InlineKeyboardButton("next", callback_data=f"next_{data_id}")
    design = [
        [prev,session_data , next]
    ]
    if not int(data_id):
        del design[0][0]

    return InlineKeyboardMarkup(inline_keyboard=design)


@dp.message_handler(commands="pages")
async def send_pages(message: types.Message, state:FSMContext):
    session = datas[0]
    await state.set_state("prev_next")
    await message.answer_photo(photo=session.get("url") , reply_markup= pagenation(0))

@dp.callback_query_handler(state="prev_next")
async def prev_next_callback(call: types.CallbackQuery , state:FSMContext):
    operation , data_id = call.data.split('_')
    data_id = int(data_id)
    if operation == "prev":
        data_id = data_id-1
    else:
        data_id = data_id+1
    session = datas[data_id]
    await state.set_state("prev_next")
    await call.message.edit_media(InputMediaPhoto(session.get('url')), reply_markup=pagenation(data_id))






#
#
#
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)









