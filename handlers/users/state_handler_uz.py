from aiogram.types import Message
from loader import dp
from aiogram.dispatcher import FSMContext
from states.satate import Comment
from keyboards.default.keyboard_button_uzb import mainMenu_uzb
phone_regex="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

@dp.message_handler(text="📝 Mulohaza bildirish")
async def reg(ms:Message):
    await ms.answer("Ismingizni kiriting:👇👇👇👇")
    await Comment.ism.set()

@dp.message_handler(state=Comment.ism)
async def ismii(ms:Message,state:FSMContext):
    ismi=ms.text
    await state.update_data(name=ismi)
    await ms.answer("Raqamingizni kiriting👇👇👇👇")
    await Comment.next()

@dp.message_handler(state=Comment.phone_number,regexp=phone_regex)
async def numb(ms:Message, state:FSMContext):
    await state.update_data(phone=ms.text)
    await ms.answer("Fikringizni qoldiring:👇👇👇👇")
    await Comment.next()

@dp.message_handler(state=Comment.phone_number)
async def numb(ms:Message,state:FSMContext):
    await ms.answer("Telefon raqamni to'g'ri kiriting:👇👇👇👇")
    await ms.answer("👨🏽‍💻")

@dp.message_handler(state=Comment.commentt)
async def com(ms:Message,state:FSMContext):
    await state.update_data(comment=ms.text)
    about=await state.get_data()
    name1=about.get("name")
    phone1=about.get("phone")
    comment1=about.get("comment")
    text1=(
        "Foydalanuvchi yuborgan fikr",
        f"✅ Ismi : {name1}",
        f"✅ Nomeri : {phone1}",
        f"✅ Qoldirgan fikri : {comment1}"
    )
    javob="\n".join(text1)
    await ms.answer(text=javob,reply_markup=mainMenu_uzb)
    await state.finish()