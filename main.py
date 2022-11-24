import asyncio
import config
import asyncpraw
import aiogram
from aiogram import Bot, types, Dispatcher
from aiogram.types import message
from aiogram.utils import  executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton




API_TOKEN = config.settings['TOKEN']
CHANNEL_ID = -1001861351751

bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML )

dp = Dispatcher(bot)

reddit = asyncpraw.Reddit(client_id=config.settings['CLIENT_ID'],
                          client_secret=config.settings['SECRET_CODE'],
                          user_agent='random_raddit_bot/1.0.1')

mems = []
TIMEOUT = 1
SUBREDDIT_NAME = 'memes'
POST_LIMIT = 2

async def send_message(channel_id: int, text: str):
    await bot.send_message(channel_id, text)

async def main():
    while True:

        await asyncio.sleep(TIMEOUT)
        memes_submissions = await reddit.subreddit(SUBREDDIT_NAME)
        memes_submissions = memes_submissions.new(limit=POST_LIMIT)
        item = await memes_submissions.__anext__()
        if item.title not in mems:
            mems.append(item.title)
            await send_message(CHANNEL_ID, item.url)




loop = asyncio.get_event_loop()
loop.run_until_complete(main())


