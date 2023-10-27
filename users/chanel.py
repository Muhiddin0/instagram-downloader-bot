
from loader import app
from utils import texts, buttons
from pyrogram.handlers import CallbackQueryHandler
from pyrogram.types import Message

async def chanel(app, message:Message):
    
    user_id = message.from_user.id
    name = message.from_user.first_name

    try:
        await app.get_chat_member(chat_id="@itkentuz", user_id=user_id)
    except:
        await app.send_message(
            chat_id=user_id,
            text=texts.not_member, 
            reply_markup=buttons.chanel
        )
        return
    
    await app.send_message(text=texts.start, chat_id=user_id)

app.add_handler(CallbackQueryHandler(chanel))



# @dp.callback_query_handler(text_contains='chanel')
# async def chanel(callback: types.CallbackQuery):
#     message = callback.message
    
#     user_id = callback.message.from_user.id
#     chanel = await bot.get_chat_member(chat_id="@itkentuz", user_id=user_id)

#     if chanel['status'] == 'left':
#         await message.answer(texts.chanel, reply_markup=buttons.chanel)
#         return
    
#     await message.answer(texts.start)