from .models import async_session
from .models import User, Category, Item
from sqlalchemy import select


async def set_user(tg_id: int) -> None:
	async with async_session() as session:
		user = await session.scalar(select(User).where(User.tg_id == tg_id))
		if not user:
			session.add(User(tg_id=tg_id))
			await session.commit()


# Функция добавления товара в бд
async def set_item(name: str, price: int, description: str) -> None:
	async with async_session() as session:
		new_item = Item(name=name, price=price, description=description)
		session.add(new_item)
		try:
			await session.commit()
		except Exception as e:
			await session.rollback()  # Откатить изменения в случае ошибки
			print(f"Ошибка при добавлении товара: {e}")  # Логируем ошибку


# Функция удаления товара в бд
async def deleted_item(name: str) -> None:
	async with async_session() as session:
		result = await session.execute(select(Item).where(Item.name==name))
		dlt_item = result.scalar()
		if dlt_item:
			await session.delete(dlt_item)
			try:
				await session.commit()
			except Exception as e:
				await session.rollback()
				print(f"Ошибка при удалении товара: {e}.")
		else:
			print(f"Товар '{name}' не найден!")


# Список добавленных товаров для роутера=pey
async def get_added_item() -> list:
	async with async_session() as session:
		result = await session.execute(select(Item))
		item = result.scalars().all()
		return item


# Функция для получения списка "названия товара" из бд
async def get_item_by_name(item_name: str) -> Item:
    async with async_session() as session:
        result = await session.execute(select(Item).where(Item.name == item_name))
        item = result.scalars().first()
        return item
	

# Функция по обновлению цены товара в бд
async def update_item_price(item_name: str, new_price: int):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(Item).where(Item.name == item_name))
            item = result.scalars().first()
            if item:
                item.price = new_price
                await session.commit()


# Функция для изменения описания товара в бд
async def update_item_description(item_name: str, new_description: str):
    async with async_session() as session:
        async with session.begin():
            result = await session.execute(select(Item).where(Item.name == item_name))
            item = result.scalars().first()
            if item:
                item.description = new_description
                await session.commit()
           