#import os

from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from .keyboards import inline_start, payment
#from admin.adm_keyboards import adm
import database.requests as rq

r = Router()


# Роутер старт
@r.message(CommandStart())
async def start_cmd(message: Message):
	await rq.set_user(message.from_user.id)
	await message.answer("Привет! Вот ссылка:", reply_markup=inline_start())

# Роутер "Каталог товара"
@r.callback_query(F.data == 'pay')
async def pay(callback: CallbackQuery):
    await callback.answer()
    items = await rq.get_added_item()  # Получаем список добавленных товаров
	
    if not items:
        await callback.message.answer("В каталоге нет добавленных товаров.")
        return

    # Формируем сообщение с товарами
    items_message = "Добавленные товары:\n\n"
    for i in items:
        items_message += f"{i.name}\n {i.price}\n {i.description}\n\n"

    await callback.message.answer(items_message, reply_markup=payment())


# "Каталог товара: кнопки"
@r.callback_query(F.data == 'trial period')
async def added_product(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer(f'Soon...')

@r.callback_query(F.data == 'one month')
async def changed_product(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer(f'Soon...2')

@r.callback_query(F.data == 'three month')
async def deleted_product(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer(f'Soon...3')

@r.callback_query(F.data == 'four month')
async def deleted_product(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer(f'Soon...4')

@r.callback_query(F.data == 'one year')
async def deleted_product(callback: CallbackQuery):
	await callback.answer()
	await callback.message.answer(f'Soon...5')



@r.message(Command('help'))
async def help_cmd(message: Message):
	await message.answer("Что нужно?")
