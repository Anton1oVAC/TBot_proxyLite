from aiogram.fsm.state import State, StatesGroup

# Класс и фсм для "Добавить товар"
class add(StatesGroup):
	name = State()
	price = State()
	description = State()	