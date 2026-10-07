import asyncio
from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN
from src.handlers import router

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
























