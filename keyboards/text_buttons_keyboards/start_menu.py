# main menu
# two text buttons
# Проживаю - Не проживаю

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kbd_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        # two buttons in one row
        [
            KeyboardButton(text='Проживаю'),
            KeyboardButton(text='Не проживаю'),
        ],
        [
            KeyboardButton(text='Закрыть меню'),
        ],
    ],
    resize_keyboard=True
)
