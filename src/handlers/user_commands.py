from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards.reply import main_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message): 
    await message.answer(f"Hello, {message.from_user.first_name}", reply_markup=main_kb)

@router.message(F.text.lower() == "language 🇺🇦/🇺🇸" )
async def language_change(message: Message):
    await message.answer("Bro, the developer is lazy and stupid.\nHe doesn't want to create this feature.\nSorry... ", reply_markup=main_kb)