import asyncio
import os

from aiogram import Dispatcher, Bot
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import F, Router

from dotenv import load_dotenv, find_dotenv
from keyboards import support_link

load_dotenv(find_dotenv())


# class
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()
start_router = Router()


# Декоратор
@dp.message(CommandStart())
async def start_cmd(message: Message):
	await message.answer("Привет! Вот ссылка:", reply_markup=support_link())

@dp.message(Command('help'))
async def help_cmd(message: Message):
	await message.answer("Что нужно?")


async def main() -> None:
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())
