from aiogram import types
from config import dp, bot


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "Каково настоящее имя Черной Пантеры?"
    answers = [
        "Т'Чалла",
        "М'Баку",
        "Нджадака",
        "Н'Джобу",
    ]

    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Уят ай! Марвел коргондор билбесин!",
        open_period=10,
    )


@dp.message_handler(commands='text')
async def echo(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)
