# set up commands description

from aiogram import Bot
from aiogram.types import Message, BotCommand

# commands list
async def set_default_commands(bot: Bot):
    start_command_description=f'Приветствие'
    help_command_description=f'Мои команды'
    handbook_command_description=f'Справочник'

    return await bot.set_my_commands(
        commands=[
            BotCommand('start', start_command_description),
            BotCommand('help', help_command_description),
            BotCommand('handbook', handbook_command_description),
        ]
    )

#
# # set up commands description
#
# from aiogram import Bot
# from aiogram.types import Message, BotCommand
#
# async def set_default_commands(bot: Bot, message: Message):
#     start_command_description=[
#         f'Здравствуйте, {message.from_user.first_name}!',
#         f'Меня зовут Екатерина. Ваш виртуальный помощник в области услуг проживания.',
#         f'Чем могу помочь?',
#     ]
#
#     help_command_description=[
#         f'Я понимаю команды:',
#         f'/start - начать работу',
#         f'/help - мои команды',
#         f'/menu - основное меню',
#     ]
#
#     menu_command_description=[
#         f'Чтобы перейти к справочнику,',
#         f'нажмите /menu',
#     ]
#
#     return await bot.set_my_commands(
#         commands=[
#             BotCommand('start', '\n'.join(start_command_description)),
#             BotCommand('help', '\n'.join(help_command_description)),
#             BotCommand('menu', '\n'.join(menu_command_description)),
#         ]
#     )
