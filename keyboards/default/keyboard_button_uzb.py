from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
mainMenu_uzb=ReplyKeyboardMarkup(
    [ 
        [ 
            KeyboardButton("📄 Ma'lumot"),
            KeyboardButton("✅ Bajarilgan loyihalar")
        ],
        [
            KeyboardButton("📍 Joylashuv"),
            KeyboardButton("📝 Mulohaza bildirish")
        ]
    ],resize_keyboard=True,one_time_keyboard=True
)

