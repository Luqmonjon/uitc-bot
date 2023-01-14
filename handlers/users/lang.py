from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher.filters import Text
from loader import dp
from keyboards.default.keyboard_button_uzb import mainMenu_uzb
from keyboards.default.keyboard_button_rus import mainMenu_rus

@dp.callback_query_handler(Text(equals='uzb'))
async def uz(call:CallbackQuery):
    texttt=(f"Assalomu alaykum,{call.from_user.full_name}!\nUITC zamonaviy kasblar maskanining rasmiy telegram botiga xush kelibsiz! ",
    "🤖 Telegram bot orqali UITC maskani haqida to'liq ma'lumotlar olishingiz, hamda o'zingiz uchun kerakli bo'lgan IT darslariga elektron tarzda ro'yxatdan o'tishingiz mumkin!",
    "🧑‍⚕️ Ro'yxatdan o'tganingizdan so'ng bizning xodimlarimiz siz bilan bog'lanishadi bu orqali siz IT maskanimizning qaysi sohasida o'qishizngizni aniqlashtirib olishingiz mumkin!")
    await call.message.answer(text="\n".join(texttt),reply_markup=mainMenu_uzb)
    await call.message.delete()
@dp.callback_query_handler(Text(equals='rus'))
async def ru(call:CallbackQuery):
    textt =( f"Здравствуйте, {call.from_user.full_name}!\nДобро пожаловать в официальный телеграм-бот Центра современной карьеры UITC!",
    "🤖 Вы можете получить полную информацию об академии UITC через Telegram-бота, а также записаться в электронном виде на нужные вам IT-классы!",
    "🧑‍⚕️ После регистрации наши сотрудники свяжутся с вами, чтобы вы могли подтвердить время посещения нашей академии UITC!")
    await call.message.answer(text="\n".join(textt),reply_markup=mainMenu_rus)
    await call.message.delete()
   
    
