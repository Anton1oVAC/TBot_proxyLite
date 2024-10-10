import os

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import BigInteger, ForeignKey, String

from dotenv import load_dotenv
load_dotenv()

DATABASE_URL=os.getenv('DATABASE_URL')



engine = create_async_engine(url=DATABASE_URL)
async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
	pass

# Таблица: Пользователь
class User(Base):
	__tablename__ = 'users'

	id: Mapped[int] = mapped_column(primary_key=True)
	tg_id = mapped_column(BigInteger)
	#name: Mapped[str] = mapped_column(String(25))
	#number_phone: Mapped[int] = mapped_column()


# Таблица: Категория товара
class Category(Base):
	__tablename__ = 'categories'

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(50))
	
# Таблица: Айтемы в товаре
class Item(Base):
	__tablename__ = 'items'

	id: Mapped[int] = mapped_column(primary_key=True)
	name: Mapped[str] = mapped_column(String(50))
	price: Mapped[int] = mapped_column()
	description: Mapped[str] = mapped_column(String(100))
	#category: Mapped[int] = mapped_column(ForeignKey('categories.id'))


async def db_main():
	async with engine.begin() as conn:
		await conn.run_sync(Base.metadata.create_all)