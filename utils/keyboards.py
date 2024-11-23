from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton

def main_menu():
    builder = ReplyKeyboardBuilder()

    # Первая строка кнопок
    builder.row(
        KeyboardButton(text="📄 Получить H&S Policy"),
        KeyboardButton(text="📜 Показать Golden Rules")
    )

    # Вторая строка кнопок
    builder.row(
        KeyboardButton(text="🎲 Получить случайное правило"),
        KeyboardButton(text="📷 Отправить фото")
    )

    # Третья строка кнопок
    builder.row(
        KeyboardButton(text="🌍 Перевести текст")
    )

    # Возвращаем разметку
    return builder.as_markup(resize_keyboard=True)
