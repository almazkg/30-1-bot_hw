from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import ADMINs

class FSMAdmin(StatesGroup):
    name = State()
    age = State()
    phonetic = State()
    group = State()

async def fsm_start(message:types.Message, state:FSMContext):
    if message.from_user.id in ADMINs:
        await FSMAdmin.name.set()
        await message.reply('Введите имя Ментора!')
    else:
        await message.answer('Вы не являетесь Админом!')


async def name_load(message:types.Message, state:FSMContext):
    if not message.text.isalpha():
        await message.reply('Вводите только буквы!')
    else:
        async with state.proxy() as data:
            data['name'] = message.text

            await FSMAdmin.next()
            await message.answer('Введите возраст Ментора!')

async def age_load(message:types.Message, state:FSMContext):
    if not message.text.isdigit():
        await message.reply('Ввдите только цифры!')
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer('введите направление!')

async def phonetic_load(message:types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['phonetic'] = message.text
    await FSMAdmin.next()
    await message.answer('введите вашу группу!')

async def group_load(message:types.Message, state:FSMContext):

    async with state.proxy() as data:
        data['group'] = message.text
    await state.finish()
    await message.answer('форма заполнено!')
    print(data)

async def cancel_fsm(message:types.Message, state:FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.reply('Отменено!')


def register_handlers_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel'), state='*')
    dp.register_message_handler(fsm_start, commands=['fsm'])
    dp.register_message_handler(name_load, state=FSMAdmin.name)
    dp.register_message_handler(age_load, state=FSMAdmin.age)
    dp.register_message_handler(phonetic_load, state=FSMAdmin.phonetic)
    dp.register_message_handler(group_load, state=FSMAdmin.group)

