import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Токен бота
BOT_API_TOKEN = os.getenv("BOT_API_TOKEN")

# Проверка токена
if not BOT_API_TOKEN:
    raise ValueError("BOT_API_TOKEN не найден в .env!")
