from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import Router

from .states import add
import database.requests as dr 

r_add = Router()

# Обработчкик Кнопоки "Добавить товар" + фсм состояние 
@r_add.message(lambda message: message.text == 'Добавить товар')
async def added_product(message: Message, state: FSMContext):
	await state.set_state(add.name)
	await message.answer(f'Введите название товара:')


@r_add.message(add.name)
async def process_name(message: Message, state: FSMContext):
	await state.update_data(name=message.text)
	await state.set_state(add.price)
	await message.answer(f'Введите цену товара:')

@r_add.message(add.price)
async def process_price(message: Message, state: FSMContext):
	await state.update_data(price=message.text)
	await state.set_state(add.description)
	await message.answer(f'Введите описание товара:')

@r_add.message(add.description)
async def process_description(message: Message, state: FSMContext):
	await state.update_data(description=message.text)
	data = await state.get_data() 
	await dr.set_item(data['name'], data['price'], data['description'])
	await message.answer(
        f"Товар добавлен:\n"
        f"Название: {data['name']}\n"
        f"Цена: {data['price']}\n"
        f"Описание: {data['description']}")
	await state.clear()