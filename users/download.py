
import requests
from loader import app
from utils import buttons, texts
from downloader import Loader
from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client
import asyncio

async def start_task(app:Client, message:Message):

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
        requests.get(url)
        data = Loader.instagram(url)
    except:
        await loading_message.edit_text(text='⭕️ Xatolik yuz berdi')
        return
    
    
    await app.delete_messages(
        chat_id=user_id,
        message_ids=loading_message.id
    )

    data_items = data['data']['items'][-1]
    if 'meta' in data_items: 
        caption = texts.download.format(
            data_items['meta']['sourceUrl'],
            data_items['meta']['title']
        )
        caption += texts.succesfuly_download
    else:caption = texts.succesfuly_download

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