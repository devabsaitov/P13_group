from aiogram import types

async def any_text_handler(msg:types.Message):
    #     await msg.answer_video(video = open("/home/dilshod/PycharmProjects/P13_group/module_4/lesson_2/my_video.mp4", 'rb'), caption="Bu endi meni videoyim :)")
    #     await msg.answer_photo(msg.photo[0].file_id, caption="Bu endi meni rasmim :)")
    await msg.answer_location(36.5 , 3.5)



async def test(msg: types.Message):
    # print(1)
    await msg.answer("Assalomu alaykum")