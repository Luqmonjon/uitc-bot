from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "π°  Botni ishga tushurish"),
            types.BotCommand("help","π Yordam"),
            types.BotCommand("lang","π·πΊ-πΊπΏ : Tilni o'zgartirish"),
        ]
    )
