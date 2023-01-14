from aiogram.types import Message
from loader import dp
from aiogram.dispatcher import FSMContext
from states.satate import Comment_rus
from keyboards.default.keyboard_button_rus import mainMenu_rus
phone_regex="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

@dp.message_handler(text="📝 Комментарии")
async def reg(ms:Message):
    await ms.answer("Введите ваше имя:👇👇👇👇")
    await Comment_rus.name.set()

@dp.message_handler(state=Comment_rus.name)
async def ismii(ms:Message,state:FSMContext):
    ismi=ms.text
    await state.update_data(name=ismi)
    await ms.answer("Введите свой номер👇👇👇👇")
    await Comment_rus.next()

@dp.message_handler(state=Comment_rus.number,regexp=phone_regex)
async def numb(ms:Message, state:FSMContext):
    await state.update_data(phone=ms.text)
    await ms.answer("Оставьте свой комментарий:👇👇👇👇")
    await Comment_rus.next()

@dp.message_handler(state=Comment_rus.number)
async def numb(ms:Message,state:FSMContext):
    await ms.answer("Введите правильный номер телефона:👇👇👇👇")
    await ms.answer("👨🏽‍💻")

@dp.message_handler(state=Comment_rus.comentttt)
async def com(ms:Message,state:FSMContext):
    await state.update_data(comment=ms.text)
    about=await state.get_data()
    name1=about.get("name")
    phone1=about.get("phone")
    comment1=about.get("comment")
    text1=(
        "Комментарий, отправленный пользователем",
        f"✅ Имя : {name1}",
        f"✅ Номер телефона : {phone1}",
        f"✅ Оставить комментарий : {comment1}"
    )
    javob="\n".join(text1)
    await ms.answer(text=javob,reply_markup=mainMenu_rus)
    await state.finish()