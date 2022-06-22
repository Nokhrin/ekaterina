from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.text_buttons_keyboards.start_menu import kbd_main_menu
from aiogram.dispatcher.filters import Command, Text

### commands filter
## set commands description

# start command
@dp.message_handler(Command('start'))
async def start_command(message: Message):
    start_command_message = [
        f'Здравствуйте, {message.from_user.first_name}!',
        'Меня зовут Екатерина.',
        'Ваш виртуальный помощник в области услуг проживания.',
    ]
    await message.answer(
        text='\n'.join(start_command_message)
    )
    await message.answer(
        text='Нажмите /help, чтобы увидеть мои команды.'
    )

# help command
@dp.message_handler(Command('help'))
async def show_help_message(message: Message):
    message_text = [
        f'Я понимаю команды:',
        f'/start - приветствие',
        f'/help - мои команды',
        f'/handbook - справочник',
    ]
    await message.answer(
        text='\n'.join(message_text),
    )

@dp.message_handler(Command('handbook'))
async def handbook_command(message: Message):
    await message.answer('Вы проживаете в Общежитии?',
        reply_markup=kbd_main_menu
    )
