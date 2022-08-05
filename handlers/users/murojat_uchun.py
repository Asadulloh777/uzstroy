import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from keyboards.default.tasdiqlash import tugma
from loader import dp, bot, baza
from states.holat import Murojaat

# Echo bot
@dp.message_handler(text='Saytga murojat qilish 📨')
async def bot_state(message: types.Message):
    await message.answer(text='Ismingizni kiriting:')
    await Murojaat.ism_qabuli.set()
@dp.message_handler(state=Murojaat.ism_qabuli)
async def bot_state(message: types.Message,state: FSMContext):
    name=message.text
    await state.update_data({'ism':name})
    await message.answer(text='Familiyangizni kiriting:')
    await Murojaat.fam_qabuli.set()
@dp.message_handler(state=Murojaat.fam_qabuli)
async def bot_state(message: types.Message,state: FSMContext):
    famil=message.text
    await state.update_data({'famil':famil})
    await message.answer(text='Email pochtangiznizni kiriting:')
    await Murojaat.mail_qabuli.set()
@dp.message_handler(state=Murojaat.mail_qabuli)
async def bot_state(message: types.Message,state: FSMContext):
    mail=message.text
    await state.update_data({'pochta':mail})
    await message.answer(text='Murojatingizni yozing:')

    await Murojaat.text_qabuli.set()
@dp.message_handler(state=Murojaat.text_qabuli)
async def bot_state(message: types.Message,state: FSMContext):
    matn=message.text
    await state.update_data({'text':matn})
    malumotlar = await state.get_data()

    ism = malumotlar.get('ism')
    famil = malumotlar.get('famil')
    pochta = malumotlar.get('pochta')
    text = malumotlar.get('text')
    vaqt = datetime.datetime.now()
    jonatish = f"📄 Ism : {ism}\n" \
               f"📄 Familiya : {famil}\n" \
               f"📬 Email : {pochta}\n" \
               f"📝 Murojat : {text}"
    await message.answer( text=jonatish,reply_markup=tugma)
    await state.finish()
@dp.message_handler(text='Tasdiqlash', state=Murojaat.text_qabuli)
async def bot_state(message: types.Message, state: FSMContext):
    malumotlar = await state.get_data()

    user_id = message.from_user.id
    ism = malumotlar.get('ism')
    famil = malumotlar.get('famil')
    pochta = malumotlar.get('pochta')
    text = malumotlar.get('text')
    vaqt = datetime.datetime.now()
    jonatish = f"📄 Ism : {ism}\n" \
               f"📄 Familiya : {famil}\n" \
               f"📬 Email : {pochta}\n" \
               f"📝 Murojat : {text}"
    baza.adminga_qoshish(ism=ism, fam=famil, mail=pochta, text=text, vaqt=vaqt)
    await bot.send_message(chat_id=user_id, text=jonatish)
    await bot.send_message(chat_id='1710770340', text=jonatish)
    await message.answer(text='Malumotlar sayt adminiga yuborildi', reply_markup=ReplyKeyboardRemove())
    await state.finish()
@dp.message_handler(text='Bekor qilish', state=Murojaat.text_qabuli)
async def bot_state(message: types.Message, state: FSMContext):
    await message.answer(text='Malumotlar o`chirib tashlandi', reply_markup=ReplyKeyboardRemove())
    await state.finish()