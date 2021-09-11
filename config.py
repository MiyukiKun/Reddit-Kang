import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
reddit_personal_use_script = os.environ.get('REDDIT_PERSONAL_USE_SCRIPT')
reddit_secret = os.environ.get('REDDIT_SECRET')
agent = os.environ.get('AGENT')
subreddit1 = os.environ.get('SUBREDDIT1')
subreddit2 = os.environ.get('SUBREDDIT2')
subreddit3 = os.environ.get('SUBREDDIT3')
channel_id = os.environ.get('CHANNEL_ID')

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
