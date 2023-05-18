
import logging
from aiogram import Bot , Dispatcher , executor , types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardRemove, WebAppInfo

API_TOKEN = '5981596441:AAH7aFeTq_oAJkfSOaGh-l7O38AWw_TY-V4'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

class RegisterState(StatesGroup):
    fullname = State()
    password = State()
    email = State()

# reply , inline
# register
async def reply_btn_show(msg: types.Message, state : FSMContext):
    # 1 version
    # markup = ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    # markup.add("button1", "button2")
    # markup.add("button3", "button4")
    # markup.add(KeyboardButton("Phone number", request_contact=True), KeyboardButton("Location", request_location=True))
    # 2 versions
    design = [
        ["button1", "button2", "button3", "button4"],
        ["button1", "button2", "button3", "button4"],
        ["button1", "button4"],
        ["button1", "button2", "button3", "button4"],
    ]
    # await state.set_state("1_btns")
    await InlineAndReplyState.reply_set.set()
    markup = ReplyKeyboardMarkup(keyboard=design , resize_keyboard=True)
    await msg.answer("create Button", reply_markup=markup)
async def inline_btn_show(msg: types.Message , state : FSMContext):
    design = [
    [InlineKeyboardButton("Kun uz", url="https://kun.uz/"),InlineKeyboardButton("My git hub", web_app=WebAppInfo(url="https://github.com/devabsaitov"))],
    [InlineKeyboardButton("inline 3", callback_data="3")],
    [InlineKeyboardButton("inline 4", callback_data="4")]]
    ikm = InlineKeyboardMarkup(inline_keyboard=design)
    await state.set_state("1_inlines")
    await msg.answer("create inline Button", reply_markup=ikm)


async def reply_keyboard_btn_handler(msg: types.Message, state : FSMContext):
    await state.finish()
    await msg.answer(msg.text)
async def inline_callback_handler(call : types.CallbackQuery, state:FSMContext):
    await call.message.delete()
    await state.finish()

    await call.message.answer(call.data, reply_markup=ReplyKeyboardRemove())



dp.register_message_handler(reply_btn_show, commands = 'reply')
dp.register_message_handler(inline_btn_show, commands = 'inline')
dp.register_callback_query_handler(inline_callback_handler, state = '1_inlines')
dp.register_message_handler(reply_keyboard_btn_handler,lambda msg: msg.text.startswith("button") ,state = InlineAndReplyState.reply_set)


if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)













