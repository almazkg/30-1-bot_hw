from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


mem = ["https://skillbox.ru/upload/setka_images/14055326052022_c7c2d6650fe8dd3125b1541cb39af56649bd56fa.jpg",
       "https://skillbox.ru/upload/setka_images/14055326052022_0ed1686442ac630326a48ddcef43684fa02b904b.jpg",
       "https://pcpro100.info/wp-content/uploads/2019/09/post_5d80b02ac353b-695x566.jpeg",
       "https://pcpro100.info/wp-content/uploads/2019/09/post_5d80b02ac4b40.jpeg",
       "https://pcpro100.info/wp-content/uploads/2019/09/post_5d80b02ac5409.jpeg",
       "https://pcpro100.info/wp-content/uploads/2019/09/post_5d845e6a687e7.png"
       ]


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f'Пусть друзья богатеют, враги не беднеют, посмотрим потом, кто кого одолеет. Начнем игры разума, '
                           f' {message.from_user.full_name}')


@dp.message_handler(commands=['mem'])
async def send_mem(message: types.Message) -> None:
    random_index = random.randint(0, len(mem) - 1)
    meme = mem[random_index]
    await bot.send_photo(message.chat.id, photo=meme)


@dp.message_handler(commands=['quiz'])
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


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)