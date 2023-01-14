from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

a={
    "Ruscha":"rus",
    "O'zbekcha":"uzb"
}

til=InlineKeyboardMarkup(row_width=2,TimeoutError=10)
for i,j in a.items():
    til.insert(InlineKeyboardButton(text=i,callback_data=j))