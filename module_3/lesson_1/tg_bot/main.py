from pprint import pprint

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup , KeyboardButton
from magic_filter import F

BOT_TOKEN = "5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4"   # Bot Father
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot , storage=MemoryStorage())

@dp.message_handler(commands = ['start'])
async def start_handler(msg : types.Message):
    print(msg.from_user.first_name , msg.chat.id)
    phone = KeyboardButton(text = "Phone", request_contact=True)
    location = KeyboardButton(text = "Location", request_location=True)

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(phone)
    markup.add(location)

    await msg.answer(text = "Assalomu alaykum", reply_markup=markup)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.bot.send_video(5062242028 , video = "AgACAgIAAxkBAAIFrGQ6nop32Ki5jW9YXD6XhFdlqHUoAAI5yDEbnTPBSXXTq_E-SFkJAQADAgADeAADLwQ")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


