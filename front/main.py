from aiogram import types, Dispatcher, Bot
from aiogram.filters import CommandStart
import asyncio

import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
	await message.answer(message.text)

async def main() -> None:
	await dp.start_polling(bot)

if __name__ == '__main__':
	asyncio.run(main())
