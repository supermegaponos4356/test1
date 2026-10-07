from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from src.states import RegistrationStates
from src.keyboards import get_confirm_keyboard
from src.db import users_data

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    first_name = message.from_user.first_name
    await message.answer(f"Привет, {first_name}!")

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - Приветствие\n"
        "/help - Список команд\n"
        "/register - Пройти регистрацию\n"
        "/profile - Посмотреть свой профиль"
    )

@router.message(Command("register"))
async def cmd_register(message: Message, state: FSMContext):
    await state.set_state(RegistrationStates.name)
    await message.answer(" Введите ваше имя.")

@router.message(RegistrationStates.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(RegistrationStates.age)
    await message.answer(" Введите ваш возраст.")

@router.message(RegistrationStates.age)
async def process_age(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer(" введите возраст цифрами:")
        return

    age = int(message.text)
    if age <= 0:
        await message.answer("Возраст не может быть равен 0 Введите возраст больше нуля:")
        return

    await state.update_data(age=age)
    await state.set_state(RegistrationStates.confirm)
    
    data = await state.get_data()
    await message.answer(
        f"Ваши данные:\nИмя: {data['name']}\nВозраст: {data['age']}",
        reply_markup=get_confirm_keyboard()
    )

@router.callback_query(RegistrationStates.confirm, F.data == "confirm_reg")
async def process_confirm(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    users_data[callback.from_user.id] = data
    await callback.message.answer("Регистрация завершена")
    await state.clear()
    await callback.answer()

@router.callback_query(RegistrationStates.confirm, F.data == "restart_reg")
async def process_restart(callback: CallbackQuery, state: FSMContext):
    await state.set_state(RegistrationStates.name)
    await callback.message.answer(" Введите ваше имя")
    await callback.answer()

@router.message(Command("profile"))
async def cmd_profile(message: Message):
    user_id = message.from_user.id
    if user_id in users_data:
        data = users_data[user_id]
        await message.answer(
            f"Ваши данные:\n"
            f"Имя — {data['name']}\n"
            f"Возраст — {data['age']}"
        )
    else:
        await message.answer("Вы не зарегистрированы. Напишите /register, чтобы пройти регистрацию.")