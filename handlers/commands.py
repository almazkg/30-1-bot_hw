from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
import random, os


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f'Пусть друзья богатеют, враги не беднеют, посмотрим потом, кто кого одолеет. Начнем игры разума, '
                           f' {message.from_user.full_name}')


dp.register_message_handler(start_command, commands=['start'])


async def mem_photo(message: types.Message):
    photo = open('images/' + random.choice(os.listdir('images')), 'rb')
    await message.answer_photo(photo)


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Кто такой Альтрон?"
    answers = [
        "Преподаватель",
        "Певец",
        "Персонаж Кинематографической вселенной Marvel",
        "Танцор",
        "Программист",
        "Персонаж сериала 'Игра в Кальмара'",
    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Фанаты Марвел не простили бы(((",
        open_period=10,
        reply_markup=markup
    )


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(mem_photo, commands=['mem'])
