from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.text_buttons_keyboards.menu import kbd_main_menu
from aiogram.dispatcher.filters import Command, Text

# commands filter
@dp.message_handler(Command('menu'))
async def show_menu(message: Message):
    await message.answer('Вы проживаете в Общежитии?',
        reply_markup=kbd_main_menu
    )

# text filter
@dp.message_handler(Text(equals=['Проживаю', 'Не проживаю']))
async def get_reside(message: Message):
    if message.text.lower() == 'проживаю':
        await message.answer(
            f'Вы ответили, что проживаете в Общежитии.\nКакая тема вас интересует?',
            reply_markup=ReplyKeyboardRemove()
        )
    elif message.text.lower() == 'не проживаю':
        await message.answer(
            f'Вы ответили, что не проживаете в Общежитии.\nКакая тема вас интересует?',
            reply_markup=ReplyKeyboardRemove()
        )
