from aiogram import Bot, Dispatcher
from aiogram.types import Message
from core.handlers.basic import get_start
import asyncio
import logging
from core.settings import settings





async def start_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text= 'Здарова! Всё нормалёк!')

async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text= 'Пакедова')




async def start():
    logging.basicConfig(level=logging.INFO
                        )
    bot = Bot(token = settings.bots.admin_id, parse_mode='HTML')

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)


    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__== "__main__":
    asyncio.run(start())