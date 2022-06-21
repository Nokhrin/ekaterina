from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards.inline_keyboards.callback_data_config import handbook_callback


# keyboards
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0

from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_1
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_1_1

from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_1_2




from app import logger

# @dp.message_handler(Text('Проживаю'))
# async def get_handbook(message: Message):
#     await message.answer(
#         text=f'Какая тема вас интересует?',
#         reply_markup=kbd_handbook_level_0
#     )

@dp.message_handler(Text(equals=['Проживаю', 'Не проживаю']))
async def get_reside(message: Message):
    logger.info('handbook started')

    if message.text.lower() == 'проживаю':
        await message.answer(
            text=f'Вы ответили, что проживаете в Общежитии.',
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text=f'Какая тема вас интересует?',
            reply_markup=kbd_handbook_level_0
        )
    elif message.text.lower() == 'не проживаю':
        await message.answer(
            text=f'Вы ответили, что не проживаете в Общежитии.',
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text=f'Какая тема вас интересует?',
            reply_markup=kbd_handbook_level_0
        )


@dp.message_handler(Command('test'))
async def get_reside(message: Message):
    if message.text.lower() == 'проживаю':
        await message.answer(
            text=f'Вы ответили, что проживаете в Общежитии.',
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text=f'Какая тема вас интересует?',
            reply_markup=kbd_handbook_level_0
        )
    elif message.text.lower() == 'не проживаю':
        await message.answer(
            text=f'Вы ответили, что не проживаете в Общежитии.',
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text=f'Какая тема вас интересует?',
            reply_markup=kbd_handbook_level_0
        )


### filtering callbacks
@dp.callback_query_handler(handbook_callback.filter(item_name='domestic_services'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logger.info(callback_data)

    await call.message.answer(
        text=f'Вы выбрали Хозяйственное обслуживание',
        reply_markup=kbd_handbook_level_0_1
    )


@dp.callback_query_handler(handbook_callback.filter(item_name='housing'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logger.info(callback_data)

    await call.message.answer(
        text=f'Вы выбрали 1.1. Жилое помещение',
        reply_markup=kbd_handbook_level_0_1_1
    )
