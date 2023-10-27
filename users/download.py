
from loader import app
from utils import buttons, texts
from downloader import Loader
from pyrogram import filters
from pyrogram.types import Message

import asyncio

async def start_task(app, message:Message):

    user_id = message.from_user.id
    url = message.text
    
    try:
        await app.get_chat_member(chat_id="@itkentuz", user_id=user_id)
    except:
        await app.send_message(
            chat_id=user_id,
            text=texts.not_member, 
            reply_markup=buttons.chanel
        )
        return

        
    loading_message = await app.send_message(
        chat_id=user_id,
        text='⏳'
    )

    try:
        data = Loader.instagram(url)
    except:
        await loading_message.edit_text(text='⭕️ Xatolik yuz berdi')
        return
    
    
    await app.delete_messages(
        chat_id=user_id,
        message_ids=loading_message.id
    )
    
    data_items = data['data']['items'][-1]['meta']
    caption = texts.download.format(data_items['sourceUrl'], data_items['title'])

    for i in data['data']['items']:
        cdn:str = i['urls'][-1]['url']
        await app.send_video(
            chat_id=user_id,
            video=cdn,
            caption=caption,
        )


@app.on_message(filters.text)
async def download(client, message):
    asyncio.create_task(start_task(client, message))