from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from utils.keyboards import main_menu

router = Router()

# Кнопка "Запуск бота"
def start_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🚀 Запуск бота")]
        ],
        resize_keyboard=True
    )

@router.message(F.command == "start")
async def start_command(message: Message):
    await message.answer(
        "Привет! Я бот-помощник. Для начала работы нажмите \"🚀 Запуск бота\":",
        reply_markup=start_menu()
    )

@router.message(F.text == "🚀 Запуск бота")
async def launch_bot(message: Message):
    await message.answer(
        "Меню доступных действий:",
        reply_markup=main_menu()
    )
