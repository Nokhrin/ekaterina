# bot starter
import asyncio
import logging

from aiogram import Bot, Dispatcher


logger = logging.getLogger(__name__)

from config import load_config

from handlers.echo import register_echo


# register all modules involved
def register_all_handlers(dp):
    register_echo(dp)




async def main():
    # prepare logger
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info('Starting bot')

    # configuring bot runner
    config = load_config('.env')
    bot = Bot(
        token=config.tg_bot.token,
        parse_mode='HTML'
    )
    dp = Dispatcher(bot)

    register_all_handlers(dp)

    # starting bot
    await dp.start_polling()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped')