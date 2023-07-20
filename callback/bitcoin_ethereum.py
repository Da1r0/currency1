from aiogram.filters.callback_data import CallbackData


class PricesCallbackData(CallbackData, prefix='curs'):
    type: str