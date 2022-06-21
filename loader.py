from aiogram import Bot, Dispatcher, types

from config import load_config

# configuring bot runner
config = load_config('.env')
bot = Bot(
    token=config.tg_bot.token,
    parse_mode='HTML'
)
dp = Dispatcher(bot)
