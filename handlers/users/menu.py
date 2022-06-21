from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.text_buttons_keyboards.start_menu import kbd_main_menu
from aiogram.dispatcher.filters import Command, Text

# commands filter
@dp.message_handler(Command('handbook'))
async def show_menu(message: Message):
    await message.answer('Вы проживаете в Общежитии?',
        reply_markup=kbd_main_menu
    )
