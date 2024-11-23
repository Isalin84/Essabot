import asyncio
import logging
from aiogram import Bot, Dispatcher
from config.config import BOT_API_TOKEN
from handlers import start_handler, photo_handler, menu_handler

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=BOT_API_TOKEN)
dp = Dispatcher()

# Подключение роутеров
dp.include_router(start_handler.router)
dp.include_router(photo_handler.router)
dp.include_router(menu_handler.router)

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
