from aiogram import types, Dispatcher
from config import ADMINs, bot
from random import choice


async def pin(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINs:
            await message.answer('Вы не являетесь Админом!')
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)


async def game_smile(message: types.Message):
    if message.text.startswith('game') and message.from_user.id in ADMINs:
        games = ['⚽️', '🏀', '🎲', '🎰', '🎯', '🎳']
        emoji = choice(games)
        await bot.send_message(message.chat.id, text=emoji)


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!')
    dp.register_message_handler(game_smile)
