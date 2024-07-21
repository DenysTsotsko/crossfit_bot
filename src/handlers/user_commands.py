from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, F

from keyboards.reply import main_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message): 
    await message.answer(f"Hello, {message.from_user.first_name}", reply_markup=main_kb)


@router.message(F.text.lower() == "workout")
async def echo(message: Message): 
    await message.answer("Here where the fsm should stay")