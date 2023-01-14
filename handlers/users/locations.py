from loader import dp
from aiogram import types

@dp.message_handler(text='📍 Joylashuv')
async def get_contact(message: types.Message):
       await message.answer_location(latitude="40.99467910822702",
                                      longitude="71.60500860584311")
       await message.answer("Bizning manzillarimiz👆👆👆👆")

@dp.message_handler(text='📍 Mестоположени')
async def get_contact(message: types.Message):
       await message.answer_location(latitude="40.99467910822702",
                                      longitude="71.60500860584311")
       await message.answer("Наши Адресы👆👆👆👆")
