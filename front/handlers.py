from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from keyboards import support_link


r = Router()

# Декоратор
@r.message(CommandStart())
async def start_cmd(message: Message):
	await message.answer("Привет! Вот ссылка:", reply_markup=support_link())

@r.message(Command('pay'))
async def pay(message: Message):
	await message.answer("Прайс: 1 месяц = 150 рублей")

@r.message(Command('help'))
async def help_cmd(message: Message):
	await message.answer("Что нужно?")
