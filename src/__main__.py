from asyncio import run

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message

from openai import AsyncOpenAI

from config import OPENAI_API_KEY, BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()
openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


@dp.message(F.text == "/start")
async def start(message: Message): 
    await message.answer(f"Hello, {message.from_user.first_name}")




if __name__ == "__main__":
    run(main())