from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)

    quiestion = "Из чего сделан щит капитана Америки?"
    answers = [
        "адамантий",
        "Вибраниум",
        "Промитий",
        "Карбонадий",

    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Фанаты Марвел не простили бы(((",
        open_period=10,
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_3")
    markup.add(next_button)
    quiestion = "Каково настоящее имя Черной Пантерры?"
    answers = [
        "Тчалла",
        "Мбакку",
        "Нджадакка",
        "Нджобу",

    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Фанаты Марвел не простили бы(((",
        open_period=10,
        reply_markup=markup
    )


async def quiz_4(callback: types.CallbackQuery):
    await callback.message.answer('Это все!')


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
    dp.register_callback_query_handler(quiz_4, text="next_button_3")