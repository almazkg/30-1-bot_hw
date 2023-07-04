from aiogram import executor, types
import logging
from config import dp
from handlers import commands, callback, admin, fsm_mentor, schedule
from database.bot_db import sql_create

fsm_mentor.register_handlers_fsm(dp)
commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)

async def on_startup(dp):
    sql_create(),
    await schedule.set_scheduler()


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        a = int(message.text) ** 2
        await message.answer(a)
    else:
        await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup)
