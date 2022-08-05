from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

tugma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Tasdiqlash'),
            KeyboardButton(text='Bekor qilish')
        ],
    ],
    resize_keyboard=True
)