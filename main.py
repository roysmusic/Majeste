import asyncio
from pytgcalls import idle
from driver.veez import call_py, bot, user

import requests
from pyrogram import idle
from pyrogram import Client as Bot

from callsmusic import run
from config import API_ID, API_HASH, BOT_TOKEN



bot = Client(
    session_name=BOT_NAME,
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root='plugins')
)


)



bot.start()
run()
idle()
