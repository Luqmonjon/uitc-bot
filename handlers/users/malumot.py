from aiogram.types import Message
from aiogram.dispatcher.filters import Text
from loader import dp

@dp.message_handler(Text(equals="📄 Ma'lumot"))
async def mal(ms:Message):
    a=("🏢UITC - United IT Club akademiyasi haqida!\n 2021-yil 20-mart kuni UITC akademiyasiga asos solindi va shu kundan boshlab rasman ish faoliyatini boshladi",
    "Akademiyada hozirgi kunda 25 dan ortiq xodim faoliyat yuritadi. Shu vaqt davomida ko'plab o'quvchilarni IT ga doir bilimlarni o'rganishiga hissa qo'shib kelmoqdamiz!",
    "Bizning maqsadimiz butun O'zbekiston bo'ylab xalqimizga xizmat qilish va barcha qiziquvchi yoshlarni kelajakda o'z kasbini topishiga yordam berishdir!!",
    "\n\n\n📍Manzil: 3-mikr Yangi O'zbekiston yoshlari ziyo maskani, \n📍Manzil: 5-mikr Alpomish fitnes 1-qavat,\n📍Manzil:Chorsu Yoshlar markazi")
    await ms.answer("\n".join(a))

@dp.message_handler(Text(equals="📄 Информация"))
async def info(ms:Message):
    c=("🏢UITC - Академия Единого Клуба IT!",
 "20 марта 2021 года Академия UITC была основана и с этой даты официально начала свою работу.",
" В настоящее время в академии работает более 25 сотрудников. За это время мы помогли многим студентам узнать об IT!",
 "Наша цель - служить нашим людям по всему Узбекистану и помогать всем заинтересованным молодым людям найти свою профессию в будущем!!",
 "\n\n\n📍Адрес: 3-микронный молодежный центр «Новый Узбекистан»,\n📍Адрес: 5-микронный фитнес-центр «Алпомиш», 1 этаж,\n📍Адрес: Молодежный центр Чорсу")
    await ms.answer("\n".join(c))