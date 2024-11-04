from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

adm = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить товар')],
        [KeyboardButton(text='Изменить товар')],
        [KeyboardButton(text='Удалить товар')]
    ],
    resize_keyboard=True
)

cancel = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text='Отмена действия фсм')]
    ],
	resize_keyboard=True
)

