import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from src.handlers import router
from config import BOT_TOKEN


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp = Dispatcher(storage=MemoryStorage())



async def main():
    init_db()
    dp.include_router(router)
    await dp.start_polling(bot)






















