from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
#from aiogram.utils.keyboard import InlineKeyboardBuilder


# Роутер старт: старт клавиатура
def inline_start():
    inline_support_link_kb = [
        [
            InlineKeyboardButton(text="Каталог товара", callback_data='pay')
        ],
        
        [
            InlineKeyboardButton(text="Написать в поддержку", url='https://t.me/Anton1o_Vakhnin'),
            InlineKeyboardButton(text="Узнать свой ID", url='https://t.me/getmyid_bot')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_support_link_kb)


# "Каталог товара: кнопки"
def payment():
    inline_payment_kb = [
        [
            InlineKeyboardButton(text="Пробный период: 2 дня - Бесплатно", callback_data='trial period')
        ],
        [
            InlineKeyboardButton(text="1 месяц = 300р", callback_data='one month')
        ],
        [
            InlineKeyboardButton(text="3 месяца = 600р", callback_data='three month')
        ],
        [
            InlineKeyboardButton(text="1 год = 3000р", callback_data='one year')
        ]
    ] 
    return InlineKeyboardMarkup(inline_keyboard=inline_payment_kb)
