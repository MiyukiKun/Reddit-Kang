from telegram import *
from telegram.ext import *
import praw
import time
import os

bot = Bot("1833090950:AAEUdZDfXcN1K39guH7jMiI8z4hVR3IJhBI")
reddit = praw.Reddit(client_id="ZzYynlO2tygKWg", client_secret="BT6frmh3NWZbGzm-YI33CU9xZcKiWA", user_agent="telegrambot")
updater=Updater("1833090950:AAEUdZDfXcN1K39guH7jMiI8z4hVR3IJhBI",use_context=True)

dispatcher=updater.dispatcher

def test_function (update:Update,context:CallbackContext):
    last = ''
    a = 1
    while a < 50000:
        subred = reddit.subreddit("ecchi")
        new = subred.new(limit = 1)
        for i in new:
            if i.url != last:
                keyboard = [[
                    InlineKeyboardButton("🍆", callback_data='1'),
                    InlineKeyboardButton("❤️", callback_data='2'),
                    InlineKeyboardButton("👎🏻", callback_data='2')
                    ]]
                
                try:
                    bot.sendPhoto(chat_id= "@R_Ecchi", caption= i.title, photo=i.url, reply_markup = InlineKeyboardMarkup(keyboard))
                    last = i.url
                    
                except Exception as e:
                    print(e)
                    print(i.url)
                    bot.send_message(chat_id= "@R_Ecchi", text= f"{i.title}\n{i.url}", reply_markup = InlineKeyboardMarkup(keyboard))

        a = a + 1
        print(a)
        time.sleep(30)
            
test_function(Update, CallbackContext)

updater.start_polling()
