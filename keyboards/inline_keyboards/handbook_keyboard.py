# static handbook
# build as inline menu

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.inline_keyboards.callback_data_config import handbook_callback

###===============================================
kbd_handbook_level_0 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='1. Хозяйственное обслуживание',
                callback_data=handbook_callback.new(
                    item_name='domestic_services',
                    chapter_number='0_1'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='2. Регистрация',
                callback_data=handbook_callback.new(
                    item_name='registration',
                    chapter_number='0_2'
                )
            ),
        ],
        [
            InlineKeyboardButton(text='Отмена', callback_data='cancel')
        ],
    ]
)

###===============================================
kbd_handbook_level_0_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='1.1. Жилое помещение',
                callback_data=handbook_callback.new(
                    item_name='housing',
                    chapter_number='0_1_1'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='1.2. Места общего пользования',
                callback_data=handbook_callback.new(
                    item_name='common_areas',
                    chapter_number='0_1_2'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ],
    ],
)

###=== sub menu 1.1 ========
kbd_handbook_level_0_1_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='1.1.1. Водоснабжение и канализация',
                callback_data=handbook_callback.new(
                    item_name='water_supply',
                    chapter_number='0_1_1_1'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='1.1.2. Электрика',
                callback_data=handbook_callback.new(
                    item_name='electrics',
                    chapter_number='0_1_1_2'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='1.1.3. Перемещение мебели',
                callback_data=handbook_callback.new(
                    item_name='furniture_removal',
                    chapter_number='0_1_1_3'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='1.1.4. Другое',
                callback_data=handbook_callback.new(
                    item_name='something_else_0_1_1_4',
                    chapter_number='0_1_1_4'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ],
    ],
)


###=== sub menu 1.2 ========
kbd_handbook_level_0_1_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='1.2.1. Уборка мест общего пользования',
                callback_data=handbook_callback.new(
                    item_name='common_areas_cleaning',
                    chapter_number='0_1_2_1'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='1.2.2. Посторонний предмет',
                callback_data=handbook_callback.new(
                    item_name='foreign_object',
                    chapter_number='0_1_2_2'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='1.2.3. Другое',
                callback_data=handbook_callback.new(
                    item_name='something_else_0_1_2_3',
                    chapter_number='0_1_2_3'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ],
    ],
)


###===============================================
kbd_handbook_level_0_2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='2.1. Регистрация по месту пребывания',
                callback_data=handbook_callback.new(
                    item_name='residence',
                    chapter_number='0_2_1'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ],
    ],
)


###=== sub menu 2.1 ========
kbd_handbook_level_0_2_1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='2.1.1. Что необходимо для регистрации',
                callback_data=handbook_callback.new(
                    item_name='registration_requirements',
                    chapter_number='0_2_1_1'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='2.1.2. В какие сроки осуществляется регистрация',
                callback_data=handbook_callback.new(
                    item_name='registration_time_frames',
                    chapter_number='0_2_1_2'
                )
            ),
        ],
        [
            InlineKeyboardButton(
                text='Отмена',
                callback_data='cancel'
            )
        ],
    ],
)
