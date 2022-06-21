# commands and settings for users
from loader import dp
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault
from config import load_config

# delete after testing
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0

# config = load_config('.env')

### default settings
# bot description

### doesn't work
# # set default bot commands
# async def set_default_commands(bot: Bot):
#     await bot.set_my_commands(
#         commands=[
#             BotCommand('start', config.tg_bot.start_command),
#         ],
#         scope=BotCommandScopeDefault()
#     )
#
#
# def register_user_main(dp: Dispatcher):
#     dp.register_message_handler(set_default_commands, commands=['start'])



### command filters
# start command
@dp.message_handler(Command('start'))
async def show_start_message(message: Message):
    message_text=[
        f'Здравствуйте, {message.from_user.first_name}!',
        f'Меня зовут Екатерина. Ваш виртуальный помощник в области услуг проживания.',
        f'Чем могу помочь?',
    ]
    await message.answer(
        # TODO - get greeting from current time
        #text='Добрый день! Меня зовут Екатерина. Ваш виртуальный помощник в области услуг проживания. Чем могу помочь?',
        text='\n'.join(message_text),
        # reply_markup=
    )

# help command
@dp.message_handler(Command('help'))
async def show_help_message(message: Message):
    message_text = [
        f'Я понимаю команды:',
        f'/start - начать работу',
        f'/help - мои команды',
        f'/menu - основное меню',
    ]
    await message.answer(
        text='\n'.join(message_text),
    )


# ### text filters
# @dp.message_handler(Text(equals=['Проживаю', 'Не проживаю']))
# async def get_reside(message: Message):
#     if message.text.lower() == 'проживаю':
#         await message.answer(
#             text=f'Вы ответили, что проживаете в Общежитии.',
#             reply_markup=ReplyKeyboardRemove()
#         )
#         await message.answer(
#             text=f'Какая тема вас интересует?',
#             reply_markup=kbd_handbook_level_0
#         )
#     elif message.text.lower() == 'не проживаю':
#         await message.answer(
#             text=f'Вы ответили, что не проживаете в Общежитии.',
#             reply_markup=ReplyKeyboardRemove()
#         )
#         await message.answer(
#             text=f'Какая тема вас интересует?',
#             reply_markup=kbd_handbook_level_0
#         )
