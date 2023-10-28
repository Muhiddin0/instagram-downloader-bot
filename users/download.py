
import os
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
    
    
    await loading_message.edit_text(
        text='yuklanmoqda...'
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
        response = requests.get(i['urls'][-1]['url'])
        content_type:str = response.headers.get('Content-Type')

        if content_type == 'image/jpeg':
            save_path = '{}_{}.png'.format(user_id, message.id)
            with open(save_path, 'wb') as file:
                file.write(response.content)
            await app.send_photo(chat_id=user_id,photo=save_path,caption=caption)
        else:
            save_path = '{}_{}.mp4'.format(user_id, message.id)
            with open(save_path, 'wb') as file:
                file.write(response.content)

            await app.send_video(chat_id=user_id, video=save_path,caption=caption)
    
    await app.delete_messages(
        chat_id=user_id,
        message_ids=loading_message.id
    )

    os.remove(save_path)


@app.on_message(filters.text)
async def download(client, message):
    asyncio.create_task(start_task(client, message))