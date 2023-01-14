from aiogram.types import MediaGroup,InputFile,Message,ContentTypes,CallbackQuery
from loader import dp
from aiogram.dispatcher.filters import Text
from pathlib import Path
from keyboards.default.keyboard_button_rus import mainMenu_rus
papka=Path().joinpath("Statik","Downloads")
papka.mkdir(parents=True,exist_ok=True)

@dp.callback_query_handler(Text(equals='abo'))
async def abobi(call:CallbackQuery):
    abob=MediaGroup()
    u1="AgACAgIAAxkBAAOiY4eMhEYN1C0J-4B2KsFlXL7p_4IAAqm_MRs290BIvsjqDtFY0d4BAAMCAAN5AAMrBA"
    u2="AgACAgIAAxkBAAOjY4eMhFN9xzyABA62cTbVlzmMZ84AAqq_MRs290BIyhDoXYZ8IDoBAAMCAAN5AAMrBA"
    u3="AgACAgIAAxkBAAOlY4eMhEM2HuiMGA7i6QIOdIrXmS8AAqy_MRs290BI90KpMu2rOV8BAAMCAAN5AAMrBA"
    u4="AgACAgIAAxkBAAOkY4eMhD4DxN95MVU6TrF1zOzUOLAAAqu_MRs290BIgksqf_QnY-MBAAMCAAN5AAMrBA"
    b=("Логотип брендинг подготовлен для маркетингового агентства 'ABOBIL'.",
    "Руководитель проекта: Кабильон",
    "Специалист: Умарджон Абдулвахидов",
    "⏳Время подготовки: 5 дней",
    "Повторное редактирование клиентом: Нет",

    "ТЕЛ: 998900500034 | Администратор")
    d="\n".join(b)
    abob.attach_photo(photo=u1)
    abob.attach_photo(photo=u2)
    abob.attach_photo(photo=u3)
    abob.attach_photo(photo=u4,caption=d)
         
    await call.message.answer_media_group(media=abob)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()

@dp.callback_query_handler(Text(equals='cofe'))
async def cof(call:CallbackQuery):
    cofe=MediaGroup()
    c1 = "AgACAgIAAxkBAAIDdmO5nmU-xTknqMNvoQtjrp2WrySiAALqxDEb2LPISa6dNgQdZEqbAQADAgADeQADLQQ"
    c2 = "AgACAgIAAxkBAAIDeGO5nmsAAVdX8nrT7UlZm2bFlrhYdQAC68QxG9izyEn-QfxwWTn2PwEAAwIAA3kAAy0E"
    c=("Логотип брендинг подготовлен для маркетингового агентства 'ABOBIL'."
    "Руководитель проекта: Кабильон",
    "Специалист: Умарджон Абдулвахидов",
    "⏳Время подготовки: 5 дней",
    "Повторное редактирование клиентом: Нет",
    "ТЕЛ: 998900500034 | Администратор)")
    c= "\n\n".join(c)
    cofe.attach_photo(photo=c1)
    cofe.attach_photo(photo=c2, caption=c)
    await call.message.answer_media_group(media=cofe)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()

@dp.callback_query_handler(Text(equals="ipak"))
async def ipak(call:CallbackQuery):
    ipak_y=MediaGroup()
    i1="AgACAgIAAxkBAAO8Y4eNLJI8rwE508JD_4hkMqei2icAAq-_MRs290BIT1jXtJCTYXkBAAMCAAN5AAMrBA"
    i2="AgACAgIAAxkBAAO-Y4eNMdqKZzxySqcr3gABFeojQ0-wAAKwvzEbNvdASASsooeA4VucAQADAgADeQADKwQ"
    i3="AgACAgIAAxkBAAPAY4eNOI2y-dxDhXVS6IzUq72I5dAAArG_MRs290BIcebFcC03BlEBAAMCAAN5AAMrBA"
    i4="AgACAgIAAxkBAAPCY4eNO85K5T_h1q2nUlFWD7nqmGMAArK_MRs290BIuvOm72jMFp4BAAMCAAN5AAMrBA"
    i=("Великий шелковый путь | классически нарисованный логотип для отеля",
    "Контакт: 998900500034")
    i="\n\n".join(i)
    ipak_y.attach_photo(photo=i1)
    ipak_y.attach_photo(photo=i2)
    ipak_y.attach_photo(photo=i3)
    ipak_y.attach_photo(photo=i4,caption=i)
    await call.message.answer_media_group(media=ipak_y)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()

@dp.callback_query_handler(Text(equals="ziyokor"))
async def ziyokorr(call:CallbackQuery):
    ziyo_group=MediaGroup()
    z1="AgACAgIAAxkBAAPUY4eOTSZMtJoYN7b6ArLAD9NzfRcAArO_MRs290BIZKBA8xs6vkABAAMCAAN5AAMrBA"
    z2="AgACAgIAAxkBAAPWY4eOVLeb_F0rEmP3MIjhAhs8kjgAArS_MRs290BITOrK-wnp2IoBAAMCAAN5AAMrBA"
    z=("Дизайн сайта для 'Зиякор образование'.",
    "Руководитель проекта: Кабильон",
    "Дизайнер: Умарджон",
    "⏳ Время подготовки: 10 дней",
    "Повторное редактирование клиентом: Нет",
    "ТЕЛ: 998900500034 | Администратор")
    z="\n\n".join(z)
    ziyo_group.attach_photo(photo=z1)
    ziyo_group.attach_photo(photo=z2,caption=z)
    await call.message.answer_media_group(media=ziyo_group)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()

@dp.callback_query_handler(Text(equals="rizotoure"))
async def rizoo(call:CallbackQuery):
    rizo_group=MediaGroup()
    r1="AgACAgIAAxkBAAPKY4eOHVreARcgyCLB_6dmSAMY8b0AArW_MRs290BIytD3q-4MmHkBAAMCAAN5AAMrBA"
    r=("Клиент: 'Ризо Тур'",

    "Логотип-брендинг для турфирмы 'Ризо Тур'",

    "Специалист: Мухаммаднабиев Мухаммадамин",
    "Ассистент: Умарджон Абдулвахидов",
    "⏳Время подготовки: 5 дней",
    "Повторное редактирование клиентом: Нет",
    "ТЕЛ: 998900500034 | Админ (https://t.me/john_sobirjonov)")
    r="\n\n".join(r)
    rizo_group.attach_photo(photo=r1,caption=r)
    await call.message.answer_media_group(media=rizo_group)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()
@dp.callback_query_handler(Text(equals="dizayn"))
async def bannerr(call:CallbackQuery):
    banerrrr=MediaGroup()
    b1="AgACAgIAAxkBAAPeY4eOoiXeygWgIYCb-_XXAqMrwZUAAre_MRs290BIhBdgmMgxqYABAAMCAAN5AAMrBA"

    b=("Дизайн баннера X-Stand",
    "Нарисован дизайн баннера X-стенда для 'UITC IT Academy'",
    "Контакт: 998900500034")
    b="\n\n".join(b)
    banerrrr.attach_photo(photo=b1,caption=b)
    await call.message.answer_media_group(media=banerrrr)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()
@dp.callback_query_handler(Text(equals="bistro"))
async def trevel(call:CallbackQuery):
    trevell=MediaGroup()
    t1="AgACAgIAAxkBAAPGY4eN1_YvWkPuiF4pRz8jFc2GQZsAAru_MRs290BIwYnMAhPgw64BAAMCAAN5AAMrBA"
    t=("Дизайн сайта для компании 'TEZ travel'.",
    "Руководитель проекта: Кабильон",
    "Дизайнер: Умарджон",
    "Время подготовки: 13 дней",
    "Повторное редактирование клиентом: Нет",
    "ТЕЛ: 998900500034 | Админ (https://t.me/john_sobirjonov)")
    t="\n\n".join(t)
    trevell.attach_photo(photo=t1,caption=t)
    await call.message.answer_media_group(media=trevell)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()
@dp.callback_query_handler(Text(equals="teacher"))
async def ustoz(call:CallbackQuery):
    ustozim=MediaGroup()
    u1="AgACAgIAAxkBAAPaY4eOkgP6MzNH9R0YNlC1cmBQ-goAArm_MRs290BISwHSUcsz4HcBAAMCAAN5AAMrBA"
    u=("Внешний дизайн сайта тестовой онлайн-площадки «УСТОЗ ТАЛЕМ».",
    "Руководитель проекта: Кабильон",
    "Дизайнер: Умарджон",
    "⏳ Время подготовки: 10 дней",
    "Повторное редактирование клиентом: Нет",
    "ТЕЛ: 998900500034 | Администратор")
    u="\n\n".join(u)

    ustozim.attach_photo(photo=u1,caption=u)
    await call.message.answer_media_group(media=ustozim)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()
    
@dp.callback_query_handler(Text(equals="boschc"))
async def bosch(call:CallbackQuery):
    bosch_group=MediaGroup()
    bos1="BAACAgIAAxkBAAIBsWOQd_z-vYGo--p8y_8ua8Ry66eyAAJnHQACEezJSngWdtZOwRHUKwQ"
    bos2="BAACAgIAAxkBAAIBrmOQd9wqILKmAafLbB25xuVT-jxhAAJlHQACEezJSlWFN8r5X89CKwQ"
    bos=("Видеоролик подготовлен для филиала 'BOSCH' в Наманганской области."
    "Специалист: Умарджон Абдулвахидов",
    "⏳Время подготовки: 5 дней",
    "Повторное редактирование клиентом: 1 раз",
    "ТЕЛ: 998900500034 | Администратор")

    bos="\n\n".join(bos)
    bosch_group.attach_video(video=bos1)
    bosch_group.attach_video(video=bos2,caption=bos)
    await call.message.answer_media_group(media=bosch_group)
    await call.message.answer(text="Вы вернулись на главную страницу👇👇👇👇👇",reply_markup=mainMenu_rus)
    await call.message.delete()