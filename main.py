import asyncio  # Работа с асинхронностью

from aiogram import Bot, Dispatcher

from config import config  # Config
from handlers import common, now_price
from keyboard.menu import curs_menu_command


def register_all_routers(dp: Dispatcher):
    dp.include_router(common.common_router)
    dp.include_router(now_price.price_router)


async def main():
    bot = Bot(token=config.token, parse_mode='HTML')
    dp = Dispatcher()  # Менеджер бота

    register_all_routers(dp)

    try:
        print('Bot Started')
        await bot.set_my_commands(curs_menu_command)
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == '__main__':  # Если мы запускаем конкретно этот файл.
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
