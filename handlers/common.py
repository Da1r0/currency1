from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboard.inline import now_history

common_router = Router()


@common_router.message(Command('start'))
async def start_command(message: Message):
    await message.answer(f'☀Привет, {message.from_user.first_name}!☀\n'
                         'Я чат-бот, который показывает средний курс криптовалют в реальном времени.📈\n'
                         'Чтобы разобраться, как со мной работать, введите команду /help')


@common_router.message(Command('help'))
async def help_command(message: Message):
    await message.answer('Ты не понял(а), как со мной работать?🤔\n'
                         'Ты попал(а) по адресу.🤓\n'
                         'Чтобы узнать средний курс криптовалют на сегодня, '
                         'нажмите на клавиатуру, которая находиться под сообщением⬇️\n'
                         'Также можно посмотреть курс криптовалют с помощью команд, '
                         'которые предложены в Меню', reply_markup=now_history)

