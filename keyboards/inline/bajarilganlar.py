from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

bajarilganlar=InlineKeyboardMarkup(
    inline_keyboard=[ 
        [ 
            InlineKeyboardButton("🅰️ ABOBIL",callback_data='abobil'),
            InlineKeyboardButton("☕️ Coffe Light",callback_data='coffe')
        ],
        [ 
            InlineKeyboardButton("🐫 Buyuk Ipak Yo'li",callback_data="ipak_yo'li"),
            InlineKeyboardButton("📝 Ziyokor education",callback_data='ziyo')
        ],
        [ 
            InlineKeyboardButton("🛫 RizoTour Sayyohlik Agentligi",callback_data='rizo'),
            InlineKeyboardButton("🖼 X-Stend Banner dizayni",callback_data='banner')
        ],
        [ 
            InlineKeyboardButton("🛩 TEZ Travel",callback_data='travel'),
            InlineKeyboardButton("🎓 Ustoz Ta'lim",callback_data="ustoz_shogirt")
        ]
    ],TimeoutError=True
)
bajarilganlar.insert(InlineKeyboardButton("🎞 BOSCH",callback_data='boschch'))

bajarilganlar_rus=InlineKeyboardMarkup(
    inline_keyboard=[ 
        [ 
            InlineKeyboardButton("🅰️ АБОБИЛ",callback_data='abo'),
            InlineKeyboardButton("☕️ Coffe Light",callback_data='cofe')
        ],
        [ 
            InlineKeyboardButton("🐫 Великий шелковый путь",callback_data='ipak'),
            InlineKeyboardButton("🛫 Зиекор образование",callback_data='ziyokor')
        ],
        [ 
            InlineKeyboardButton("🛫 Туристическое агентство РизоТур",callback_data='rizotoure'),
            InlineKeyboardButton("🖼 X-Stend Banner dizayn",callback_data='dizayn')
        ],
        [ 
            InlineKeyboardButton("🛩 Быстро Трэвел",callback_data='bistro'),
            InlineKeyboardButton("🎓 Устоз Образование",callback_data='teacher')
        ]
    ],RuntimeError=True
)
bajarilganlar_rus.insert(InlineKeyboardButton("🎞 BOSCH company",callback_data='boschc'))