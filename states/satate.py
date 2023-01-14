from aiogram.dispatcher.filters.state import State,StatesGroup

class language(StatesGroup):
    rus=State()
    uzb=State()



class Comment(StatesGroup):
    ism=State()
    phone_number=State()
    commentt=State()

class Comment_rus(StatesGroup):
    name=State()
    number=State()
    comentttt=State()