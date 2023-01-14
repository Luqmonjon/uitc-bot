from aiogram.types import MediaGroup,InputFile,Message,ContentTypes,CallbackQuery
from loader import dp
from aiogram.dispatcher.filters import Text
from pathlib import Path
from keyboards.default.keyboard_button_uzb import mainMenu_uzb
papka=Path().joinpath("Statik","Downloads")
papka.mkdir(parents=True,exist_ok=True)

@dp.message_handler(content_types='photo')
async def photoo(ms:Message):
    idd = ms.photo[-1].file_id
    await ms.answer(idd)

@dp.message_handler(content_types='photo')
async def ras(ms:Message):
    rasm=ms.photo[-1]
    rasm_id=rasm.file_id
    await rasm.download(destination=papka)
    await ms.answer("Rasm saqlandi")
    await ms.answer(text=rasm_id)
@dp.message_handler(content_types='video')
async def vid(ms:Message):
    video=ms.video
    video_id=video.file_id
    await ms.answer("Video saqlandi")
    await ms.answer(text=video_id)
@dp.callback_query_handler(Text(equals='abobil'))
async def abo(call:CallbackQuery):
    abob=MediaGroup()
    u1="AgACAgIAAxkBAAOiY4eMhEYN1C0J-4B2KsFlXL7p_4IAAqm_MRs290BIvsjqDtFY0d4BAAMCAAN5AAMrBA"
    u2="AgACAgIAAxkBAAOjY4eMhFN9xzyABA62cTbVlzmMZ84AAqq_MRs290BIyhDoXYZ8IDoBAAMCAAN5AAMrBA"
    u3="AgACAgIAAxkBAAOlY4eMhEM2HuiMGA7i6QIOdIrXmS8AAqy_MRs290BI90KpMu2rOV8BAAMCAAN5AAMrBA"
    u4="AgACAgIAAxkBAAOkY4eMhD4DxN95MVU6TrF1zOzUOLAAAqu_MRs290BIgksqf_QnY-MBAAMCAAN5AAMrBA"
    b=("'ABOBIL' marketing agentligi uchun tayyorlangan logobrending.",

    "\nLoyiha boshqaruvchisi: Qobiljon",
    "\nMutaxassis: Umarjon Abdulvohidov",

    "\n\n⏳Tayyorlash vaqti: 5 kun",
    "\nMijoz tomonidan qayta tahrirlash: Yo'q",

    "\n\nTEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")
    d="\n".join(b)
    # abo_list=[u1,u2,u3,u4]
    # for i in abo_list:
    abob.attach_photo(photo=u1)
    abob.attach_photo(photo=u2)
    abob.attach_photo(photo=u3)
    abob.attach_photo(photo=u4,caption=d)
         
    await call.message.answer_media_group(media=abob)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    await call.message.delete()


@dp.callback_query_handler(Text(equals='coffe'))
async def cof(call:CallbackQuery):
    cofe=MediaGroup()
    c1 = "AgACAgIAAxkBAAIDdmO5nmU-xTknqMNvoQtjrp2WrySiAALqxDEb2LPISa6dNgQdZEqbAQADAgADeQADLQQ"
    c2 = "AgACAgIAAxkBAAIDeGO5nmsAAVdX8nrT7UlZm2bFlrhYdQAC68QxG9izyEn-QfxwWTn2PwEAAwIAA3kAAy0E"
    c=("'COFFEE LIGHT' kompaniyasi uchun tayyorlangan mahsulot qadoq dizayni.(TAKLIF SIFATIDA TAYYORLANGAN)",
"\nMutaxassis: Umarjon Abdulvohidov ",
"\n⏳Tayyorlash vaqti: 3 kun",
"\nMijoz tomonidan qayta tahrirlash: Yo'q",

"\nTEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")
    c= "\n\n".join(c)
    cofe.attach_photo(photo=c1)
    cofe.attach_photo(photo=c2, caption=c)
    await call.message.answer_media_group(media=cofe)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()


@dp.callback_query_handler(Text(equals="ipak_yo'li"))
async def ipak(call:CallbackQuery):
    ipak_y=MediaGroup()
    i1="AgACAgIAAxkBAAO8Y4eNLJI8rwE508JD_4hkMqei2icAAq-_MRs290BIT1jXtJCTYXkBAAMCAAN5AAMrBA"
    i2="AgACAgIAAxkBAAO-Y4eNMdqKZzxySqcr3gABFeojQ0-wAAKwvzEbNvdASASsooeA4VucAQADAgADeQADKwQ"
    i3="AgACAgIAAxkBAAPAY4eNOI2y-dxDhXVS6IzUq72I5dAAArG_MRs290BIcebFcC03BlEBAAMCAAN5AAMrBA"
    i4="AgACAgIAAxkBAAPCY4eNO85K5T_h1q2nUlFWD7nqmGMAArK_MRs290BIuvOm72jMFp4BAAMCAAN5AAMrBA"
    i=("Buyuk Ipak Yo'li | mehmonxonasi uchun klassik usulda chizilgan logo",

        "Bog'lanish: +998900500034")
    i="\n\n".join(i)
    ipak_y.attach_photo(photo=i1)
    ipak_y.attach_photo(photo=i2)
    ipak_y.attach_photo(photo=i3)
    ipak_y.attach_photo(photo=i4,caption=i)
    await call.message.answer_media_group(media=ipak_y)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()


@dp.callback_query_handler(Text(equals="ziyo"))
async def ziyokor(call:CallbackQuery):
    ziyo_group=MediaGroup()
    z1="AgACAgIAAxkBAAPUY4eOTSZMtJoYN7b6ArLAD9NzfRcAArO_MRs290BIZKBA8xs6vkABAAMCAAN5AAMrBA"
    z2="AgACAgIAAxkBAAPWY4eOVLeb_F0rEmP3MIjhAhs8kjgAArS_MRs290BITOrK-wnp2IoBAAMCAAN5AAMrBA"
    z=("'Ziyokor education' uchun veb sayt tashqi dizayn.",

    "Loyiha boshqaruvchi: Qobiljon",
    "Dizayner: Umarjon",


    "⏳Tayyorlash vaqti: 10 kun",
    "Mijoz tomonidan qayta tahrirlash: Yo'q",

    "TEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")
    z="\n\n".join(z)
    ziyo_group.attach_photo(photo=z1)
    ziyo_group.attach_photo(photo=z2,caption=z)
    await call.message.answer_media_group(media=ziyo_group)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()


@dp.callback_query_handler(Text(equals="rizo"))
async def rizoo(call:CallbackQuery):
    rizo_group=MediaGroup()
    r1="AgACAgIAAxkBAAPKY4eOHVreARcgyCLB_6dmSAMY8b0AArW_MRs290BIytD3q-4MmHkBAAMCAAN5AAMrBA"
    r=("Mijoz: 'Rizo Tour'",

    "'Rizo Tour' sayohat agentligi uchun chizilgan logobrending",

    "Mutaxassis: Muhammadnabiyev Muhammadamin",
    "Yordamchi: Umarjon Abdulvohidov", 

    "⏳Tayyorlash vaqti: 5 kun",
    "Mijoz tomonidan qayta tahrirlash: Yo'q",

    "TEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")
    r="\n\n".join(r)
    rizo_group.attach_photo(photo=r1,caption=r)
    await call.message.answer_media_group(media=rizo_group)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()

@dp.callback_query_handler(Text(equals="banner"))
async def bannerr(call:CallbackQuery):
    banerrrr=MediaGroup()
    b1="AgACAgIAAxkBAAPeY4eOoiXeygWgIYCb-_XXAqMrwZUAAre_MRs290BIhBdgmMgxqYABAAMCAAN5AAMrBA"
    b=("X-Stend Banner dizayni",
    "'Buyuk Ipak Yo'li' mehmonxonasi uchun chizilgan X-stend banner dizayni",
    "Bog'lanish: +998900500034")
    b="\n\n".join(b)
    banerrrr.attach_photo(photo=b1,caption=b)
    await call.message.answer_media_group(media=banerrrr)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()

@dp.callback_query_handler(Text(equals="travel"))
async def trevel(call:CallbackQuery):
    trevell=MediaGroup()
    t1="AgACAgIAAxkBAAPGY4eN1_YvWkPuiF4pRz8jFc2GQZsAAru_MRs290BIwYnMAhPgw64BAAMCAAN5AAMrBA"
    t=("'TEZ travel 'kompaniyasi uchun veb sayt tashqi dizayn.",
    "Loyiha boshqaruvchi: Qobiljon",
    "Dizayner: Umarjon",
    "⏳Tayyorlash vaqti: 13 kun",
    "Mijoz tomonidan qayta tahrirlash: Yo'q",

    "TEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")
    t="\n\n".join(t)
    trevell.attach_photo(photo=t1,caption=t)
    await call.message.answer_media_group(media=trevell)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()

@dp.callback_query_handler(Text(equals="ustoz_shogirt"))
async def ustoz(call:CallbackQuery):
    ustozim=MediaGroup()
    u1="AgACAgIAAxkBAAPaY4eOkgP6MzNH9R0YNlC1cmBQ-goAArm_MRs290BISwHSUcsz4HcBAAMCAAN5AAMrBA"
    u=("'USTOZ TA'LIM'  (http://www.ustoztalim.uz/)online test platformasi uchun veb sayt tashqi dizayn.",
    "Loyiha boshqaruvchi: Qobiljon",
    "Dizayner: Umarjon",
    "⏳Tayyorlash vaqti: 10 kun",
    "Mijoz tomonidan qayta tahrirlash: Yo'q",
    "TEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")
    u="\n\n".join(u)

    ustozim.attach_photo(photo=u1,caption=u)
    await call.message.answer_media_group(media=ustozim)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()

@dp.callback_query_handler(Text(equals="boschch"))
async def bosch(call:CallbackQuery):
    bosch_group=MediaGroup()
    bos1="BAACAgIAAxkBAAIBrmOQd9wqILKmAafLbB25xuVT-jxhAAJlHQACEezJSlWFN8r5X89CKwQ"
    bos2="BAACAgIAAxkBAAIBsWOQd_z-vYGo--p8y_8ua8Ry66eyAAJnHQACEezJSngWdtZOwRHUKwQ"
    bos=("'BOSCH' Namangan viloyati filiali uchun  tayyorlangan moushn video.",
    "Mutaxassis: Umarjon Abdulvohidov ",
    "⏳Tayyorlash vaqti: 5 kun",
    "Mijoz tomonidan qayta tahrirlash: 1 marta",
    "TEL: +998900500034 |Admin (https://t.me/john_sobirjonov)")

    bos="\n\n".join(bos)
    bosch_group.attach_video(video=bos1)
    bosch_group.attach_video(video=bos2,caption=bos)
    await call.message.answer_media_group(media=bosch_group)
    await call.message.answer(text="Asosiy sahifadan kerakli bo'limni tanlang👇👇👇👇👇",reply_markup=mainMenu_uzb)
    
    await call.message.delete()