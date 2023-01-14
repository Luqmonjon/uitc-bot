from aiogram.types import Message,ContentTypes
from loader import dp
from aiogram.dispatcher.filters import Text
from keyboards.inline.bajarilganlar import bajarilganlar,bajarilganlar_rus

@dp.message_handler(Text(equals="✅ Bajarilgan loyihalar"))
async def proekt(ms:Message):
    await ms.answer("Bajarilgan proektlarimizdan namunalarni ko'rishingiz mumkin!",reply_markup=bajarilganlar)

@dp.message_handler(Text(equals="✅ Завершенные проекты"))
async def proekt_rus(ms:Message):
    await ms.answer("Вы можете ознакомиться с образцами наших реализованных проектов!",reply_markup=bajarilganlar_rus)