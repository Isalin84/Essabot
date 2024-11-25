from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_keyboard():
    """
    Создает главное меню с кнопками для взаимодействия.
    """
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📄 Получить H&S Policy"),
                KeyboardButton(text="📜 Показать Golden Rules")
            ],
            [
                KeyboardButton(text="🎲 Получить случайное правило"),
                KeyboardButton(text="🌐 Перевести текст")
            ],
            [
                KeyboardButton(text="📤 Отправить фото")  # Добавляем кнопку для отправки фото
            ]
        ],
        resize_keyboard=True  # Опция для изменения размера кнопок
    )
    return keyboard
