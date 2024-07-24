from asyncio import run

from aiogram import Bot, Dispatcher
from openai import AsyncOpenAI

from config import OPENAI_API_KEY, BOT_TOKEN

from handlers import user_commands, questionare, bot_messages


# openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        questionare.router, 
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        pass