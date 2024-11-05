import os

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .adm_keyboards import adm
from front.keyboards import inline_start

r_adm = Router()


# Обработчик команды админ и вывод клавиатуры для админа
@r_adm.message(Command('admin'))
async def adm_cmd(message: Message):
	if message.from_user.id == int(os.getenv('ADMIN_ID')):
		await message.answer(f'Вы авторизовались', reply_markup=adm)
	else:
		await message.answer(f'Вы не админ', reply_markup=inline_start())


# Обработчик кнопки для отмены фсм состояния
@r_adm.message(lambda message: message.text == 'Отмена действия фсм')
async def cancel_button(message: Message, state: FSMContext):
	await state.clear()
	await message.answer(f'Отмена фсм', reply_markup=adm)