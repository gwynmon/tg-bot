from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but_info = KeyboardButton(text='Инфа')

info_key = ReplyKeyboardMarkup(
    keyboard=[[but_info]],
    resize_keyboard=True,
    one_time_keyboard=True
)