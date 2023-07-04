from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from config import bot

async def napomni(bot:Bot):
    await bot.send_message(5530923083, text='прочитай документацию')

async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone='Asia/Bishkek')
    scheduler.add_job(
        napomni,
        trigger=CronTrigger(day_of_week=2, hour=18, minute=30),
        kwargs={"bot": bot}
    )
    scheduler.start()