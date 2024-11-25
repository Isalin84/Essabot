from aiogram import Router, F
from aiogram.types import Message
import os


router = Router()  # Создаем маршрутизатор


@router.message(F.text == "📤 Отправить фото")
async def receive_photo_instruction(message: Message):
   """
   Инструкция для пользователя, как отправить фото в бот.
   """
   await message.answer(
       "Пожалуйста, отправьте мне фото, и я сохраню его в папке `photos` на сервере."
   )


@router.message(F.photo)
async def save_uploaded_photo(message: Message):
   """
   Обработчик загрузки фото от пользователя.
   Сохраняет полученные изображения в папку `photos`.
   """
   photos_path = "photos"  # Папка для сохранения фотографий
   os.makedirs(photos_path, exist_ok=True)  # Создаем папку, если её ещё нет


   # Получаем фото самого высокого качества
   photo = message.photo[-1]


   # Получаем информацию о файле через метод get_file
   file_info = await message.bot.get_file(photo.file_id)


   # Генерируем путь для сохранения
   file_path = os.path.join(photos_path, f"{photo.file_unique_id}.jpg")


   # Скачиваем файл
   await message.bot.download_file(file_info.file_path, destination=file_path)


   # Уведомляем пользователя об успешном сохранении
   await message.answer(f"Ваше фото успешно сохранено как: {file_path}")
