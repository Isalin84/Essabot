import os
import random
from aiogram import Router
from aiogram.types import Message, FSInputFile

router = Router()

# Список золотых правил
golden_rules = [
    "1) SAM и LOTOTO: Я всегда буду проверять надлежащую изоляцию опасных источников...",
    "2) Опасные вещества: Я всегда буду работать с опасными веществами...",
    "3) Работа на высоте: Я всегда буду использовать все надлежащие средства...",
    "4) Электричество: Я всегда буду работать с электричеством...",
    "5) Наряд-допуск: Я всегда буду работать с оформленным нарядом-допуском...",
    "6) Транспортные средства: Я всегда буду соблюдать минимальное безопасное расстояние..."
]

# Обработчик для отправки H&S Policy
@router.message(lambda message: message.text == "📄 Получить H&S Policy")
async def send_hs_policy(message: Message):
    file_path = "docs/H&S_Policy.docx"  # Путь к файлу
    if os.path.exists(file_path):  # Проверяем, существует ли файл
        file = FSInputFile(file_path)  # Создаем объект FSInputFile
        await message.answer_document(file)  # Отправляем документ
    else:
        await message.answer("Файл H&S Policy не найден. Убедитесь, что он существует в папке docs.")

# Обработчик для отправки списка Golden Rules
@router.message(lambda message: message.text == "📜 Показать Golden Rules")
async def send_golden_rules(message: Message):
    await message.answer("\n".join(golden_rules))

# Обработчик для отправки случайного правила
@router.message(lambda message: message.text == "🎲 Получить случайное правило")
async def send_random_rule(message: Message):
    await message.answer(random.choice(golden_rules))
