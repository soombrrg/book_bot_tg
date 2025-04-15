from aiogram import Router
from aiogram.types import Message

router = Router()


# Для не предусмотренных сообщений пользователя
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Не предусмотренно!')
