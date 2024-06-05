from aiogram import types, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot.keyboards.start_keyboard import start_key
from bot.keyboards.algo_keyboard import algo_key
from bot.keyboards.info_keyboard import info_key

router = Router()

class Form(StatesGroup):
    plaintext = State()
    action = State()
    algo = State()

@router.message(F.text == '/start')
async def command_start_handler(msg: types.Message, state: FSMContext) -> None:
    await state.set_state(Form.action)
    await msg.answer(text=f"Привет, {msg.from_user.full_name}! Я - бот шифровальщик, который может зашифровать и расшифровать твои данные разными алгоритмами, а также помочь разобраться в принципе их работы. Итак, с чего начнем?",
                     reply_markup=start_key)  

@router.message(F.text == 'Узнать больше')
async def info_command(msg: types.Message) -> None:
    await msg.answer(text="Хорошо, тут будет гайд, пока его нет.",
                     reply_markup=info_key)
    
@router.message(F.text == 'Зашифровать')
async def encrypt_command(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(action=msg.text)
    await msg.answer(text="Каким алгоритмом зашифровать сообщение?",
                     reply_markup=algo_key)
    
@router.message(F.text == 'Расшифровать')
async def decrypt_command(msg: types.Message, state: FSMContext) -> None:
    await state.update_data(action=msg.text)
    await msg.answer(text="Каким алгоритмом сообщение было зашифровано?",
                     reply_markup=algo_key)
    
