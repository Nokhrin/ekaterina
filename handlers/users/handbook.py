from loader import dp
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from keyboards.inline_keyboards.callback_data_config import handbook_callback


# keyboards
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0

from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_1
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_1_1
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_1_2

from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_2
from keyboards.inline_keyboards.handbook_keyboard import kbd_handbook_level_0_2_1

from app import logger


@dp.message_handler(Text(equals=['Проживаю', 'Не проживаю', 'Закрыть меню']))
async def get_reside(message: Message):
    # logger.info('handbook started')

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
    elif message.text.lower() == 'закрыть меню':
        await message.answer(
            text=f'Закрываю меню',
            reply_markup=ReplyKeyboardRemove(),
        )



### filtering callbacks
@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logger.info(callback_data)

    await call.message.answer(
        text=f'Вы выбрали 1. Хозяйственное обслуживание',
        reply_markup=kbd_handbook_level_0_1
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_2'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logger.info(callback_data)

    await call.message.answer(
        text=f'Вы выбрали 2. Регистрация',
        reply_markup=kbd_handbook_level_0_2
    )



@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_2_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        'Вы выбрали 2.1. Регистрация по месту пребывания',
        '',
        'Регистрация по месту пребывания (временная регистрация)',
        'осуществляется после подписания сторонами договора найма специализированного жилого помещения на срок, указанный в договоре.',
        'Свидетельство о временной регистрации выдаётся на каждое лицо, указанное в договоре найма.',
        'При этом, в паспорт никаких отметок не ставится.',
    ]
    await call.message.answer('\n'.join(answer_text))
    await call.message.answer(
        text=f'Идём дальше?',
        reply_markup=kbd_handbook_level_0_2_1
    )


@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_2_1_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    await call.message.answer(
        text=f'Вы выбрали 2.1.1. Что необходимо для регистрации',
    )
    answer_text = [
        'Необходимые для регистрации документы подготавливаются комендантом общежития Уральского главного управления.',
        'Пакет документов включает в себя:',
        '- Заявление о регистрации на каждого члена семьи, указанного в договоре (для лиц старше 18 лет подготавливает общежития, для детей до 18 лет заявление \"от руки\" пишет наниматель)',
        '- Свидетельство о временной регистрации (подготавливает администрация общежития)',
        '- Копия подписанного договора найма специализированного жилого помещения (подготавливает администрация)',
        '- Оригинал паспорта (для детей до 18 лет копия свидетельства о рождении) (предоставляется нанимателем)',
    ]
    await call.message.answer('\n'.join(answer_text))
    # keep the last keyboard


### cancel callback
@dp.callback_query_handler(handbook_callback.filter(item_name_en='cancel'))
async def get_cancel(call: CallbackQuery, callback_data: dict):

    await call.message.answer(
        text='Закрываю меню',
    )
    await call.message.edit_reply_markup(reply_markup=None)
