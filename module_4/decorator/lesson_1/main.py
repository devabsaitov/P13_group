from aiogram import Dispatcher , Bot , types , executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = "5888421916:AAFIQ0K73hAwKdAkBxuDZv83TlSF_VBw1rU"
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot = bot , storage=MemoryStorage())


@dp.message_handler(commands="start")
async def start(msg : types.Message):

    await msg.answer(text = "Assalomu alaykum")

URL = ''

@dp.message_handler(commands=['image, img'])
async def cmd_image(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))



if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)
