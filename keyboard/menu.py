from aiogram.types import BotCommand

curs_menu_command = [
    BotCommand(command='/start', description='Запустить/Перезапустить бота💬'),
    BotCommand(command='/help', description='Не понял, как пользоваться ботом🤔'),
    BotCommand(command='/curs_now_bitcoin', description='Средний курс биткоина на сегодня📈'),
    BotCommand(command='/curs_now_ethereum', description='Средний курс эфириума на сегодня📈'),
    BotCommand(command='/curs_now_tether', description='Средний курс тезера на сегодня📈'),
    BotCommand(command='/curs_now_xrp', description='Средний курс риппла на сегодня📈'),
    BotCommand(command='/curs_now_bnb', description='Средний курс бинанс-коина на сегодня📈')
]
