from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callback.bitcoin_ethereum import PricesCallbackData

bitcoin_prices = InlineKeyboardButton(text='Курс Bitcoin,BTC',
                                  callback_data=PricesCallbackData(type='bitcoin_curs').pack())
ethereum_prices = InlineKeyboardButton(text='Курс Ethereum,ETH',
                                      callback_data=PricesCallbackData(type='ethereum_curs').pack())
tether_prices = InlineKeyboardButton(text='Курс Tether,USDT',
                                      callback_data=PricesCallbackData(type='tether_curs').pack())
xrp_prices = InlineKeyboardButton(text='Курс Ripple,XRP',
                                      callback_data=PricesCallbackData(type='xrp_curs').pack())
bnb_prices = InlineKeyboardButton(text='Курс Binance Coin,BNB',
                                      callback_data=PricesCallbackData(type='bnb_curs').pack())

now_history = InlineKeyboardMarkup(inline_keyboard=[
    [bitcoin_prices, ethereum_prices, tether_prices, xrp_prices, bnb_prices]
])
