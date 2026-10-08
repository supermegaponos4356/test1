import asyncio
from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN
from src.handlers import router




BOT_TOKEN  = "8962190292:AAEz4_06wiXub1T2mkYSJbVj37L4Yj7C0_k"





async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)
    print("бот запущен")

if __name__ == "__main__":
    asyncio.run(main())
























