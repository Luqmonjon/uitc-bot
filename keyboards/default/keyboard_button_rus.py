from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
mainMenu_rus=ReplyKeyboardMarkup(
    [ 
        [ 
            KeyboardButton("📄 Информация"),
            KeyboardButton("✅ Завершенные проекты")
        ],
        [
            KeyboardButton("📍 Mестоположени"),
            KeyboardButton("📝 Комментарии")
        ]
    ],resize_keyboard=True,one_time_keyboard=True
)