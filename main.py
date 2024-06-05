import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.handlers import main_handler, algo_handler
from dotenv import load_dotenv


async def main() -> None:
    load_dotenv('.env')
    TOKEN = getenv("TOKEN_API")

    dp = Dispatcher()

    dp.include_routers(main_handler.router, algo_handler.router)

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())