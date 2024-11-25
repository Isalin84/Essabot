# start_handler.py
from aiogram import Router, F
from aiogram.types import Message
from utils.keyboards import main_menu_keyboard  # Импорт клавиатуры главного меню

router = Router()  # Создаем маршрутизатор


@router.message(F.text == "/start")
async def start_command(message: Message):
    """
    Обработчик команды /start.
    Приветствует пользователя и предлагает перейти в главное меню.
    """
    await message.answer(
        "Привет! Я ваш персональный бот для автоматизации задач.\n"
        "Нажмите /menu, чтобы открыть главное меню или воспользуйтесь командами ниже:\n"
        "📄 H&S Policy\n📜 Golden Rules\n🎲 Случайное правило\n🌐 Перевести текст"
    )
    # Отправляем главное меню
    await message.answer("Вот главное меню:", reply_markup=main_menu_keyboard())


@router.message(F.text == "/help")
async def help_command(message: Message):
    """
    Обработчик команды /help.
    Предоставляет пользователю информацию о доступных функциях бота.
    """
    await message.answer(
        "Вот список доступных команд:\n"
        "/start - Запустить бота\n"
        "/menu - Показать главное меню\n"
        "📄 Получить H&S Policy\n"
        "📜 Показать Golden Rules\n"
        "🎲 Получить случайное правило\n"
        "🌐 Перевести текст\n"
        "📷 Загрузить фото\n"
        "📤 Отправить фото"
    )
