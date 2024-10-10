from .models import async_session
from .models import User, Category, Item
from sqlalchemy import select

async def set_user(tg_id: int) -> None:
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))

		if not user:
			session.add(User(tg_id=tg_id))
			await session.commit()


async def set_item(name: str, price: int, description: str) -> None:
	async with async_session() as session:
		new_item =  Item(name=name, price=price, description=description)
		session.add(new_item)
		try:
			await session.commit()
		except Exception as e:
			await session.rollback()  # Откатить изменения в случае ошибки
			print(f"Ошибка при добавлении товара: {e}")  # Логируем ошибку


# Список добавленных товаров для роутера=pey
async def get_added_item() -> list:
	async with async_session() as session:
		result = await session.execute(select(Item))
		item = result.scalars().all()
		return item