# menu_handler.py
from aiogram import Router, F  # Основные инструменты для создания обработчиков
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton  # Работа с клавиатурой и сообщениями
from aiogram.fsm.context import FSMContext  # Контекст FSM для управления состояниями
from aiogram.fsm.state import StatesGroup, State  # Класс для работы с состояниями
from googletrans import Translator  # Библиотека для перевода текста
import os
import random
from aiogram.types import FSInputFile  # Для отправки файлов

router = Router()  # Создаем маршрутизатор
translator = Translator()  # Экземпляр переводчика

# Состояния для перевода текста
class TranslationState(StatesGroup):
    waiting_for_text = State()  # Состояние ожидания текста от пользователя


# Генерация главного меню
def main_menu_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)  # Создаем клавиатуру с автоизменением размера
    keyboard.row(
        KeyboardButton(text="📄 Получить H&S Policy"),  # Кнопка для политики
        KeyboardButton(text="📜 Показать Golden Rules")  # Кнопка для Golden Rules
    )
    keyboard.row(
        KeyboardButton(text="🎲 Получить случайное правило"),  # Кнопка для аудиофайлов
        KeyboardButton(text="🌐 Перевести текст")  # Кнопка для перевода текста
    )
    return keyboard


@router.message(F.text == "/menu")
async def show_main_menu(message: Message):
    """Показать главное меню."""
    await message.answer("Вот главное меню:", reply_markup=main_menu_keyboard())


@router.message(F.text == "📄 Получить H&S Policy")
async def send_hs_policy(message: Message):
    """Отправка H&S Policy документа."""
    file_path = "docs/H&S_Policy.docx"  # Путь к файлу
    if os.path.exists(file_path):  # Проверяем, существует ли файл
        file = FSInputFile(file_path)
        await message.answer_document(file)  # Отправляем документ пользователю
    else:
        await message.answer("Файл H&S Policy не найден. Убедитесь, что он существует в папке docs.")


@router.message(F.text == "📜 Показать Golden Rules")
async def send_golden_rules(message: Message):
    """Отправка списка Golden Rules."""
    golden_rules = [
        "1) SAM и LOTOTO: Я всегда буду проверять надлежащую изоляцию опасных источников...",
        "2) Опасные вещества: Я всегда буду работать с опасными веществами только с применением необходимых мер...",
        "3) Работа на высоте: Я всегда буду использовать все надлежащие средства для работы на высоте...",
        "4) Электричество: Я всегда буду работать с электричеством только с использованием необходимых защит...",
        "5) Наряд-допуск: Я всегда буду работать с оформленным нарядом-допуском...",
        "6) Транспортные средства: Я всегда буду соблюдать минимальное безопасное расстояние..."
    ]
    await message.answer("\n".join(golden_rules))  # Отправляем пользователю список правил


@router.message(F.text == "🎲 Получить случайное правило")
async def send_random_audio(message: Message):
    """Отправка случайного аудиофайла."""
    assets_path = "Assets"  # Папка с аудиофайлами
    if not os.path.exists(assets_path):  # Проверяем существование папки
        await message.answer("Папка с аудиофайлами не найдена.")
        return

    audio_files = [f for f in os.listdir(assets_path) if f.endswith(".mp3")]  # Список аудиофайлов
    if not audio_files:  # Если файлов нет
        await message.answer("В папке Assets нет звуковых файлов.")
        return

    random_audio = random.choice(audio_files)  # Выбираем случайный файл
    file_path = os.path.join(assets_path, random_audio)

    audio = FSInputFile(file_path)
    await message.answer_audio(audio)  # Отправляем аудиофайл


@router.message(F.text == "🌐 Перевести текст")
async def start_translation_mode(message: Message, state: FSMContext):
    """Включение режима перевода текста."""
    await message.answer("Введите текст, который вы хотите перевести:")
    await state.set_state(TranslationState.waiting_for_text)  # Устанавливаем состояние


@router.message(TranslationState.waiting_for_text)
async def translate_message(message: Message, state: FSMContext):
    """Обработка текста для перевода."""
    try:
        detected_language = translator.detect(message.text).lang  # Определяем язык текста
        if detected_language == "ru":
            translated_text = translator.translate(message.text, src="ru", dest="en").text
            await message.answer(f"Перевод на английский:\n{translated_text}")
        elif detected_language == "en":
            translated_text = translator.translate(message.text, src="en", dest="ru").text
            await message.answer(f"Перевод на русский:\n{translated_text}")
        else:
            await message.answer("Поддерживаются только русский и английский языки.")
    except Exception as e:
        await message.answer(f"Ошибка перевода: {str(e)}")
    finally:
        await state.clear()  # Сбрасываем состояние
