from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from generators import generating_promt

from keyboards.reply import main_kb

router = Router()

@router.message(Command("gpt"))
async def bot_promt(message: Message):
    response = await generating_promt(message.text)
    await message.answer(text = response, reply_markup=main_kb)