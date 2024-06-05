from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

but_guide_menu = KeyboardButton(text='Узнать больше')
but_dec_menu = KeyboardButton(text='Зашифровать')
but_enc_menu = KeyboardButton(text='Расшифровать')

start_key = ReplyKeyboardMarkup(
    keyboard=[[but_guide_menu, but_dec_menu, but_enc_menu]],
    resize_keyboard=True,
    one_time_keyboard=True
)