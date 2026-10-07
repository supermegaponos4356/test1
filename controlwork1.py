import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
























