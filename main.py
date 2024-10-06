import asyncio
import os
import logging
import sys
from aiogram import Dispatcher, Bot

from front.handlers import r
from database.models import db_main

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

async def main() -> None:
	await db_main()
	TOKEN = os.getenv('TOKEN')
	bot = Bot(token=TOKEN)
	dp = Dispatcher()
	dp.include_router(r) 
	await dp.start_polling(bot)

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, stream=sys.stdout)
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('Exit')
