from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.photo)
async def handle_photo(message: Message, bot):
    photo_id = message.photo[-1].file_id
    file = await bot.get_file(photo_id)
    file_path = f"photos/photo_{photo_id}.jpg"
    await bot.download_file(file.file_path, destination=file_path)
    await message.answer(f"Фото сохранено")
