from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from aiogram.types import Message
from loader import dp
from keyboards.inline.inline_keyboard import til

@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/lang - Tilni o'zgartirish")
    
    await message.answer("\n".join(text))

@dp.message_handler(commands="lang")
async def tillll(ms:Message):
        await ms.answer(text="Tilni tanlang👇👇👇👇👇",reply_markup=til)
