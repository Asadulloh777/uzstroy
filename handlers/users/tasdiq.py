from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from loader import dp



@dp.message_handler(text='Tasdiqlash')
async def bot_state(message: types.Message):
    await message.answer(text='Malumotlar sayt adminiga yuborildi', reply_markup=ReplyKeyboardRemove())
@dp.message_handler(text='Bekor qilish')
async def bot_state(message: types.Message):
    await message.answer(text='Malumotlar o`chirib tashlandi', reply_markup=ReplyKeyboardRemove())