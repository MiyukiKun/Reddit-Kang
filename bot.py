from config import bot, reddit_personal_use_script, reddit_secret, agent, subreddit1, subreddit2, subreddit3, channel_id
from telethon import events, Button
import asyncio
import asyncpraw
import requests

reddit = asyncpraw.Reddit(client_id = reddit_personal_use_script, client_secret = reddit_secret, user_agent = agent)

loop = asyncio.get_event_loop()

async def kang_reddit():
    last1 = ''
    last2 = ''
    last3 = ''

    while True:
        subred1 = await reddit.subreddit("AnimeWallpapersSFW")
        subred2 = await reddit.subreddit("AnimeWallpaper")
        subred3 = await reddit.subreddit("Genshinwallpapers")

        new1 = subred1.new(limit=1)
        new2 = subred2.new(limit=1)
        new3 = subred3.new(limit=1)

        async for i in new1:
            if i.url != last1:
                try:
                    print(i.url)
                    response = requests.get(i.url, stream=True)
                    name = i.title.split(" ")[0]
                    filename = f"{name}.png"
                    with open(filename, "wb") as file:
                        file.write(response.content)
                    print("here")
                    await bot.send_message(
                        channel_id,
                        f"{i.title}\n@{channel_id}",
                        file=filename,
                    )
                    await bot.send_message(
                        channel_id,
                        f"{i.title}\n@{channel_id}",
                        file=filename,
                        force_document=True,
                        buttons=[Button.inline("❤️ 0", data="e1:0:0:0"), Button.inline(
                            "👍🏻 0", data="e2:0:0:0"), Button.inline("👎🏻 0", data="e3:0:0:0")]
                    )
                    os.remove(filename)

                    last1 = i.url
                except Exception as e:
                    print(e)

        async for i in new2:
            if i.url != last2:
                try:
                    print(i.url)
                    response = requests.get(i.url, stream=True)
                    name = i.title.split(" ")[0]
                    filename = f"{name}.png"
                    with open(filename, "wb") as file:
                        file.write(response.content)
                    print("here")
                    await bot.send_message(
                        channel_id,
                        f"{i.title}\n@{channel_id}",
                        file=filename,
                    )
                    await bot.send_message(
                        channel_id,
                        f"{i.title}\n@{channel_id}",,
                        file=filename,
                        force_document=True,
                        buttons=[Button.inline("❤️ 0", data="e1:0:0:0"), Button.inline(
                            "👍🏻 0", data="e2:0:0:0"), Button.inline("👎🏻 0", data="e3:0:0:0")]
                    )
                    os.remove(filename)

                    last2 = i.url
                except Exception as e:
                    print(e)

        async for i in new3:
            if i.url != last3:
                try:
                    print(i.url)
                    response = requests.get(i.url, stream=True)
                    name = i.title.split(" ")[0]
                    filename = f"{name}.png"
                    with open(filename, "wb") as file:
                        file.write(response.content)
                    print("here")
                    await bot.send_message(
                        channel_id,
                        f"{i.title}\n@{channel_id}",
                        file=filename,
                    )
                    await bot.send_message(
                        channel_id,
                        f"{i.title}\n@{channel_id}",
                        file=filename,
                        force_document=True,
                        buttons=[Button.inline("❤️ 0", data="e1:0:0:0"), Button.inline(
                            "👍🏻 0", data="e2:0:0:0"), Button.inline("👎🏻 0", data="e3:0:0:0")]
                    )
                    os.remove(filename)

                    last3 = i.url

                except Exception as e:
                    print(e)

        await asyncio.sleep(60)
        print("nothing")

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await bot.send_message(event.chat_id, "Bot is Running")

@bot.on(events.CallbackQuery(pattern=b"e1"))
async def emoji1(event):
    data = event.data.decode('utf-8')
    data_split = data.split(':')
    new_count = int(data_split[1]) +1
    await event.edit(buttons=[
        Button.inline(f"❤️ {new_count}", data=f"e1:{new_count}:{data_split[2]}:{data_split[3]}"), 
        Button.inline(f"👍🏻 {data_split[2]}", data=f"e2:{new_count}:{data_split[2]}:{data_split[3]}"), 
        Button.inline(f"👎🏻 {data_split[3]}", data=f"e3:{new_count}:{data_split[2]}:{data_split[3]}")
    ])

@bot.on(events.CallbackQuery(pattern=b"e2"))
async def emoji2(event):
    data = event.data.decode('utf-8')
    data_split = data.split(':')
    new_count = int(data_split[2]) + 1
    await event.edit(buttons=[
        Button.inline(f"❤️ {data_split[1]}", data=f"e1:{data_split[1]}:{new_count}:{data_split[3]}"), 
        Button.inline(f"👍🏻 {new_count}", data=f"e2:{data_split[1]}:{new_count}:{data_split[3]}"), 
        Button.inline(f"👎🏻 {data_split[3]}", data=f"e3:{data_split[1]}:{new_count}:{data_split[3]}")
    ])

@bot.on(events.CallbackQuery(pattern=b"e3"))
async def emoji3(event):
    data = event.data.decode('utf-8')
    data_split = data.split(':')
    new_count = int(data_split[3]) + 1
    await event.edit(buttons=[
        Button.inline(f"❤️ {data_split[1]}", data=f"e1:{data_split[1]}:{data_split[2]}:{new_count}"), 
        Button.inline(f"👍🏻 {data_split[2]}", data=f"e2:{data_split[1]}:{data_split[2]}:{new_count}"), 
        Button.inline(f"👎🏻 {new_count}", data=f"e3:{data_split[1]}:{data_split[2]}:{new_count}")
    ])

loop.run_until_complete(kang_reddit())

bot.start()

bot.run_until_disconnected()
