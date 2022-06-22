from loader import dp, bot
from aiogram import Bot
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

# temp import
from keyboards.text_buttons_keyboards.start_menu import kbd_main_menu


from app import logger

###===== Chapter 0 ==============###
@dp.message_handler(Text(equals=['Проживаю', 'Не проживаю']))
# @dp.message_handler(Text(equals=['Проживаю', 'Не проживаю', 'Закрыть справочник']))
async def get_reside(message: Message):
    # logger.info('handbook started')

    if message.text.lower() == 'проживаю':
        await message.answer(
            text=f'Главное меню справочника',
            reply_markup=ReplyKeyboardRemove()
        )
        await message.answer(
            text=f'Какая тема вас интересует?',
            reply_markup=kbd_handbook_level_0
        )
    elif message.text.lower() == 'не проживаю':
        # await message.answer(
        #     text=f'Выберите категорию',
        #     reply_markup=ReplyKeyboardRemove()
        # )
        await message.answer(
            text=f'-- в разработке --',
            reply_markup=kbd_main_menu
        )
    # elif message.text.lower() == 'закрыть справочник':
    #     await message.answer(
    #         text=f'Для просмотра списка команд нажмите /help',
    #         reply_markup=ReplyKeyboardRemove(),
    #     )



### filtering callbacks

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logger.info(call)

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'1. Хозяйственное обслуживание',
        reply_markup=kbd_handbook_level_0_1
    )

###======== Chapter 1.1 =============###

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.1. Жилое помещение',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'Выберите следующий раздел',
        reply_markup=kbd_handbook_level_0_1_1
    )


@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_1_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.1.1. Водоснабжение и канализация',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_1
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_1_2'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.1.2. Электрика',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_1
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_1_3'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.1.3. Перемещение мебели',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_1
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_1_4'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.1.4. Другое',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_1
    )


###======== Chapter 1.2 =============###

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_2'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.2. Места общего пользования',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'Выберите следующий раздел',
        reply_markup=kbd_handbook_level_0_1_2
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_2_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.2.1. Уборка мест общего пользования',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_2
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_2_2'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.2.2. Посторонний предмет',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_2
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_1_2_3'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '1.2.3. Другое',
    ]
    await call.message.answer('\n'.join(answer_text))

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_1_2
    )


###===== Chapter 2 ================###

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_2'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'2. Регистрация',
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

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'Выберите следующий раздел',
        reply_markup=kbd_handbook_level_0_2_1
    )


@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_2_1_1'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        'Вы выбрали 2.1.1. Что необходимо для регистрации',
        '',
        'Необходимые для регистрации документы подготавливаются комендантом общежития Уральского главного управления.',
        'Пакет документов включает в себя:',
        '- Заявление о регистрации на каждого члена семьи, указанного в договоре (для лиц старше 18 лет подготавливает общежития, для детей до 18 лет заявление \"от руки\" пишет наниматель)',
        '- Свидетельство о временной регистрации (подготавливает администрация общежития)',
        '- Копия подписанного договора найма специализированного жилого помещения (подготавливает администрация)',
        '- Оригинал паспорта (для детей до 18 лет копия свидетельства о рождении) (предоставляется нанимателем)',
    ]

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text='\n'.join(answer_text),
        reply_markup=kbd_handbook_level_0_2_1
    )

@dp.callback_query_handler(handbook_callback.filter(chapter_number='0_2_1_2'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    answer_text = [
        '2.1.2. В какие сроки осуществляется регистрация',
    ]
    await call.message.answer(
        text='\n'.join(answer_text)
    )

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'-- в разработке --',
        reply_markup=kbd_handbook_level_0_2_1
    )






### back to handbook main page
@dp.callback_query_handler(handbook_callback.filter(chapter_number='0'))
async def get_domestic_services(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    # logger.info(call)

    await bot.delete_message(
        chat_id=call.message.chat.id,
        message_id=call.message.message_id
    )

    await call.message.answer(
        text=f'Главное меню справочника',
        reply_markup=kbd_handbook_level_0
    )


### cancel
@dp.message_handler(Text(equals=['Закрыть справочник']))
async def get_cancel(message: Message):
    answer_text = [
        'Закрываю справочник',
        '',
        'Чтобы открыть справочник, нажмите /handbook',
        'Для просмотра доступных команд нажмите /help',
    ]

    await bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id
    )

    await message.answer(
        text='\n'.join(answer_text),
        reply_markup=ReplyKeyboardRemove()
    )


@dp.callback_query_handler(handbook_callback.filter(item_name_en='cancel'))
async def get_cancel(call: CallbackQuery, callback_data: dict):
    answer_text = [
        'Закрываю справочник',
        '',
        'Чтобы открыть справочник, нажмите /handbook',
        'Для просмотра доступных команд нажмите /help',
    ]
    await call.message.answer(
        text='\n'.join(answer_text),
    )
    await call.message.edit_reply_markup(
        reply_markup=None
    )
