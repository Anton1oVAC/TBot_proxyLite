import asyncio
import os
from aiogram import Dispatcher, Bot

from front.handlers import r
from admin.adm_handlers import r_adm
from admin.fsm_add import r_add
from database.models import db_main
from dotenv import load_dotenv, find_dotenv
from logging_conf import log_conf

load_dotenv(find_dotenv())

async def main() -> None:
	await db_main()
	TOKEN = os.getenv('TOKEN')
	bot = Bot(token=TOKEN)
	dp = Dispatcher()
	dp.include_router(r)
	dp.include_router(r_adm)
	dp.include_router(r_add)
	await dp.start_polling(bot)

if __name__ == '__main__':
	logger = log_conf()
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('Exit')
