import os
from dotenv import load_dotenv  # Для работы с .env файлами


# Загрузка переменных окружения из .env
load_dotenv()


# Токен для доступа к Telegram Bot API
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")


# Проверяем, что токен загружен
if not BOT_API_TOKEN:
   raise ValueError("BOT_API_TOKEN не найден! Проверьте файл .env.")