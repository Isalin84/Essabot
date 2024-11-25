import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage  # Хранилище для состояний FSM
from config.config import BOT_API_TOKEN  # Импорт токена из файла конфигурации
from handlers import menu_handler, photo_handler, start_handler  # Подключение обработчиков


# Настройка логирования
logging.basicConfig(level=logging.INFO)


# Создаем экземпляр бота
bot = Bot(token=BOT_API_TOKEN)


# Создаем диспетчер с хранилищем FSM
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


# Регистрация всех обработчиков
dp.include_router(start_handler.router)
dp.include_router(photo_handler.router)
dp.include_router(menu_handler.router)




async def main():
   """Главная функция для запуска бота."""
   print("Бот запущен и готов к работе!")
   await dp.start_polling(bot)  # Запуск long-polling для обработки обновлений




if __name__ == "__main__":
   asyncio.run(main())  # Асинхронный запуск бота