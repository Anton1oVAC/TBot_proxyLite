from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .states import change
from .adm_keyboards import cancel
import database.requests as dr

r_change = Router()

# Обработчик кнопки "Изменить товар" + фсм состояние
@r_change.message(lambda message: message.text == 'Изменить товар')
async def edit_product(message: Message, state: FSMContext):
    items = await dr.get_added_item()
    if not items:
        await message.answer(f'В каталоге нет добавленных товаров')
        return
    items_add = "Добавленные товары:\n\n"
    for i in items:
        items_add += f"{i.name}\n {i.price}\n {i.description}\n\n"
    await message.answer(items_add + f'Введите название товара для изменения:', reply_markup=cancel)
    await state.set_state(change.name)


@r_change.message(change.name)
async def process_select_item(message: Message, state: FSMContext):
    item_name = message.text
    items = await dr.get_item_by_name(item_name)
    if not items:
        await message.answer(f'Товар не найден')
        return
    await state.update_data(item_name=item_name)
    await message.answer(f'Введите новую цену товара:', reply_markup=cancel)
    await state.set_state(change.price)


@r_change.message(change.price)
async def process_update_price(message: Message, state: FSMContext):
    new_price = message.text
    user_data = await state.get_data()
    item_name = user_data.get('item_name')
    await dr.update_item_price(item_name, int(new_price))  
    await message.answer(f'Введите новое описание товара:', reply_markup=cancel)
    await state.set_state(change.description)


@r_change.message(change.description)
async def process_update_description(message: Message, state: FSMContext):
    new_description = message.text
    user_data = await state.get_data()
    item_name = user_data.get('item_name')
    await dr.update_item_description(item_name, new_description)
    await message.answer(f'Товар изменен')
    await state.clear()