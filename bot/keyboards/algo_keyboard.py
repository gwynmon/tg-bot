from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# Новый алгоритм надо добавлять в .env, algo_keyboard.py и algo.controller.py.
# Автор говнокодер простите
but_3des = KeyboardButton(text='3DES')
but_aes = KeyboardButton(text='AES')
but_rsa = KeyboardButton(text='RSA')
but_rc4 = KeyboardButton(text='RC4')

algo_key = ReplyKeyboardMarkup(
    keyboard=[[but_3des, but_aes, but_rsa, but_rc4]],
    resize_keyboard=True,
    one_time_keyboard=True
)