from aiogram import types
from aiogram.dispatcher import FSMContext


async def start_handler(msg: types.Message, state : FSMContext):
    await state.set_state('username_set')
    await msg.answer("Username 👇")


async def username_handler(msg : types.Message, state : FSMContext):
    async with state.proxy() as storage:
        storage['username'] = msg.text
    await state.set_state('password_set')
    await msg.answer('Password 👇')


async def password_handler(msg: types.Message, state: FSMContext):
    if len(msg.text) >= 4:
        async with state.proxy() as storage:
            storage['password'] = msg.text
        text = f"""INFO:\nUsername:{storage.get('username')}\npassword:{storage.get('password')}"""
        await msg.answer(text)
        await state.finish()

    else:
        await msg.delete()
        # await state.finish()
        await msg.answer("Password invalid ❌ ! try password 👇")






