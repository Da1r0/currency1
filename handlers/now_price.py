import requests
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from callback.bitcoin_ethereum import PricesCallbackData

price_router = Router()

url = "https://api.coinstats.app/public/v1/coins?skip=0&limit=5&currency=EUR"


@price_router.message(Command('curs_now_bitcoin'))
async def bitcoin_command(message: Message):
    response = requests.get(url).json()
    await message.answer(f'Монета: {response["coins"][0]["name"]}\n'
                         f'Символ: {response["coins"][0]["symbol"]}\n'
                         f'Стоимость: {response["coins"][0]["price"]} EUR💶')


@price_router.message(Command('curs_now_ethereum'))
async def ethereum_command(message: Message):
    response = requests.request("GET", url).json()
    await message.answer(f'Монета: {response["coins"][1]["name"]}\n'
                         f'Символ: {response["coins"][1]["symbol"]}\n'
                         f'Стоимость: {response["coins"][1]["price"]} EUR💶')


@price_router.message(Command('curs_now_tether'))
async def tether_command(message: Message):
    response = requests.request("GET", url).json()
    await message.answer(f'Монета: {response["coins"][2]["name"]}\n'
                         f'Символ: {response["coins"][2]["symbol"]}\n'
                         f'Стоимость: {response["coins"][2]["price"]} EUR💶')


@price_router.message(Command('curs_now_xrp'))
async def xrp_command(message: Message):
    response = requests.request("GET", url).json()
    await message.answer(f'Монета: Ripple\n'
                         f'Символ: {response["coins"][3]["symbol"]}\n'
                         f'Стоимость: {response["coins"][3]["price"]} EUR💶')


@price_router.message(Command('curs_now_bnb'))
async def bnb_command(message: Message):
    response = requests.request("GET", url).json()
    await message.answer(f'Монета: Binance Coin\n'
                         f'Символ: {response["coins"][4]["symbol"]}\n'
                         f'Стоимость: {response["coins"][4]["price"]} EUR💶')



@price_router.callback_query(PricesCallbackData.filter())
async def get_by_kb(query: CallbackQuery, callback_data: PricesCallbackData):
    curs_type = callback_data.type
    if curs_type == 'bitcoin_curs':
        response = requests.get(url).json()

        await query.message.answer(f'Монета: {response["coins"][0]["name"]}\n'
                                   f'Символ: {response["coins"][0]["symbol"]}\n'
                                   f'Стоимость: {response["coins"][0]["price"]} EUR💶')
        await query.answer()

    elif curs_type == 'ethereum_curs':
        response = requests.get(url).json()
        await query.message.answer(f'Монета: {response["coins"][1]["name"]}\n'
                                   f'Символ: {response["coins"][1]["symbol"]}\n'
                                   f'Стоимость: {response["coins"][1]["price"]} EUR💶')
        await query.answer()

    elif curs_type == 'tether_curs':
        response = requests.get(url).json()
        await query.message.answer(f'Монета: {response["coins"][2]["name"]}\n'
                                   f'Символ: {response["coins"][2]["symbol"]}\n'
                                   f'Стоимость: {response["coins"][2]["price"]} EUR💶')
        await query.answer()

    elif curs_type == 'xrp_curs':
        response = requests.get(url).json()
        await query.message.answer(f'Монета: Ripple\n'
                                   f'Символ: {response["coins"][3]["symbol"]}\n'
                                   f'Стоимость: {response["coins"][3]["price"]} EUR💶')
        await query.answer()
    else:
        response = requests.get(url).json()
        await query.message.answer(f'Монета: Binance Coin\n'
                                   f'Символ: {response["coins"][4]["symbol"]}\n'
                                   f'Стоимость: {response["coins"][4]["price"]} EUR💶')
        await query.answer()
