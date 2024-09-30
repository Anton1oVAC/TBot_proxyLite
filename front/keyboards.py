from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
#from aiogram.utils.keyboard import InlineKeyboardBuilder


def support_link():
	inline_support_link_kb = [
		InlineKeyboardButton(text="Написать в поддержку", url='https://t.me/Anton1o_Vakhnin')
	]
	return InlineKeyboardMarkup(inline_keyboard=[inline_support_link_kb])