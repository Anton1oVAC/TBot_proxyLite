import os

from aiogram.types import Message
from aiogram import Router
from aiogram.filters import Command

from .adm_keyboards import adm
from front.keyboards import inline_start

r_adm = Router()

@r_adm.message(Command('admin'))
async def adm_cmd(message: Message):
	if message.from_user.id == int(os.getenv('ADMIN_ID')):
		await message.answer(f'Вы авторизовались', reply_markup=adm)
	else:
		await message.answer(f'Вы не админ', reply_markup=inline_start())



@r_adm.message(lambda message: message.text == 'Добавить товар')
async def added_product(message: Message):
	await message.answer(f'Soon...')

@r_adm.message(lambda message: message.text == 'Изменить товар')
async def changed_product(message: Message):
	await message.answer(f'Soon...2')

@r_adm.message(lambda message: message.text == 'Удалить товар')
async def deleted_product(message: Message):
	await message.answer(f'Soon...3')