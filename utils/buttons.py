from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

chanel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("IT Kent 🇺🇿", url='https://t.me/itkentuz'),
    ],
    [
        InlineKeyboardButton("✅ Tekshirish", callback_data='chanel'),
    ]
])


menu = InlineKeyboardMarkup(inline_keyboard=[
    
    [
        InlineKeyboardButton("🆕 Essay Band", callback_data='essay_body'),
    ],
    [
        InlineKeyboardButton("📊 Ielts ball", callback_data='ielts_ball'),
    ]
])

cancel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("❌ Cancel", callback_data='cancel'),
    ]
])

back = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("🔙 Back", callback_data='back'),
    ]
])