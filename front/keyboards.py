from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
#from aiogram.utils.keyboard import InlineKeyboardBuilder


def support_link():
    inline_support_link_kb = [
        [
            InlineKeyboardButton(text="Написать в поддержку", url='https://t.me/Anton1o_Vakhnin'),
            InlineKeyboardButton(text="Узнать свой ID", url='https://t.me/getmyid_bot')
        ],
        [
            InlineKeyboardButton(text="Узнать цену подписки", callback_data='pay')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_support_link_kb)

#def payment():
#	inline_payment_kb = [
#		InlineKeyboardButton(text="1 месяц", )
#	]