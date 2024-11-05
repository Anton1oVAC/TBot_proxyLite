from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from .states import dlt
from .adm_keyboards import cancel
import database.requests as dr

r_dlt = Router()


@r_dlt.message(lambda message: message.text == 'Удалить товар')
async def deleted_product(message: Message, state: FSMContext):
	await state.set_state(dlt.name)
	await message.answer(f'Введите название товара для удаления:', reply_markup=cancel)

@r_dlt.message(dlt.name)
async def process_item_name(message: Message, state: FSMContext):
    item_name = message.text
    await dr.deleted_item(item_name)
    await message.answer(f'Товар с названием "{item_name}" был удален.')
    await state.clear()
