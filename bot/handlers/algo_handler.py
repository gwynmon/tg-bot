from os import getenv
from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import rsa
from bot.handlers.main_handler import Form
from bot.controller.algo_controller import encrypt, decrypt

router = Router()

@router.message(Form.action)
async def algo_command(msg: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.algo)
    data = await state.get_data()
    await state.update_data(algo=msg.text)
    action = data['action']

    if not (await is_algo_exist(msg)):
        await msg.answer(text="Я не знаю такого алгоритма")
        raise Exception("Argument Exception")

    if (action.lower() == 'зашифровать'):
        await msg.answer(text=f"Введите сообщение, которое хотите зашифровать алгоритмом {msg.text}")
    elif (action.lower() == 'расшифровать' and msg.text.lower() == 'rsa'):
        await msg.answer(text=f"Введите сообщение, которое хотите расшифровать алгоритмом {msg.text}, а также значения n, e, d, p, q (все раздели единичным пробелом)")
    elif (action.lower() == 'расшифровать'):
        await msg.answer(text=f"Введите сообщение, которое хотите расшифровать алгоритмом {msg.text}, а также ключ через пробел (без других знаков)")

@router.message(Form.algo)
async def encrypt_command(msg: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.plaintext)
    data = await state.get_data()
    if data['action'].lower() == 'зашифровать':
        algo = data['algo']
        cipher = encrypt(algo, msg.text)
        if algo.lower() != 'rsa':
            await msg.answer(text=f"Вы ввели сообщение: {msg.text} \n Зашифрованное: {cipher[0]} \n Ключ шифрования: {cipher[1]}")
        else:
            await msg.answer(text=f"Вы ввели сообщение: {msg.text} \n Зашифрованное: {cipher[0]} \n n: {cipher[1].n} \n e: {cipher[1].e} \n d: {cipher[1].d} \n p: {cipher[1].p} \n q: {cipher[1].q}")
    elif data['action'].lower() == 'расшифровать' and data['algo'].lower() == 'rsa':
        try:
            plaintext, n, e, d, p, q = msg.text.split(' ')
        except ValueError:
            msg.answer(text="Сообщение или ключ введены некорректно")

        plaintext = bytes.fromhex(plaintext)
        key = rsa.PrivateKey(n=int(n), e=int(e), d=int(d), p=int(p), q=int(q))
        result = decrypt(data['algo'], plaintext, key)

        await msg.answer(text=f"{result}")
    elif data['action'].lower() == 'расшифровать':
        try:
            plaintext, key = msg.text.split(' ')
        except ValueError:
            msg.answer(text="Сообщение или ключ введены некорректно")
        #ХУЙНЯ НЕ РАБОТАЕТ ЕСЛИ ХЕКС ИЗ RC4
        if data['algo'].lower() != 'rc4':
            plaintext = bytes.fromhex(plaintext)
        if data['algo'].lower() == '3des':
            key = bytes.fromhex(key)
        result = decrypt(data['algo'], plaintext, key)
        await msg.answer(text=f"Расшифрованное сообщение: {result}")
    else:
        await msg.answer(text="Я не знаю такой команды")



async def is_algo_exist(msg: types.Message) -> bool:
    load_dotenv('.env')
    algos = getenv('ALGOS').split(' ')
    exist = False
    for algo in algos:
        if (msg.text.lower() == algo.lower() ):
            exist = True
            break 
    return exist
    
        