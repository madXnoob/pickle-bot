# bot.py
import os
import random
import asyncio
import sys
import discord
# from dotenv import load_dotenv

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

def print_to_stdout(*a):
    print(*a, file = sys.stdout)

async def random_message_task():
    await client.wait_until_ready()

    guild = discord.utils.get(client.guilds, name=GUILD)

    while True:
        sendChance = random.randint(1,100)
        if sendChance < 3:
            random_messages = [
                'piggle piggle piggle',
                'piggle stewart',
                'think im piggle stewart'
            ]

            print_to_stdout('randomly messaging')
            channel = discord.utils.get(guild.text_channels, name="general")
            await channel.send(random.choice(random_messages))

        await asyncio.sleep(1800)

async def greet(guild):
    print_to_stdout('Greeting')
    greetings = [
        'hey guys it piggle',
        'hi im piggle',
        'piggle piggle'
    ]
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send(random.choice(greetings))

@client.event
async def on_error(event):
    print_to_stdout(event)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user in message.mentions or '!piggle' in message.content.lower() or '!pickle' in message.content.lower():

        responses = [
            'https://imgur.com/zBdK87E',
            'https://imgur.com/MVaP57c',
            'https://imgur.com/635q6Cj',
            'https://imgur.com/gbb1BXt',
            'https://imgur.com/FdWEzkL',
            'https://imgur.com/o4b8pS6',
            'https://imgur.com/jRuilRz',
            'https://imgur.com/TO5zcfu',
            'https://imgur.com/Prywhlf',
            'https://imgur.com/UgSfXM1',
            'https://imgur.com/jiIhNCW',
            'https://imgur.com/avL9UEr',
            'https://imgur.com/DfCWQYn',
            'https://imgur.com/Eyf9oGV',
            'https://imgur.com/m3BVbih',
            'https://imgur.com/k9ZY8tq',
            'https://imgur.com/nG8zC2d',
            'https://imgur.com/bTQBfnY',
            'https://imgur.com/MdihQEK',
            'https://upload.wikimedia.org/wikipedia/commons/b/bb/Pickle.jpg'
        ]

        await asyncio.sleep(1.5)
        response = random.choice(responses)
        await message.channel.send(response)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print_to_stdout(f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})')

    await greet(guild)

client.loop.create_task(random_message_task())
client.run(TOKEN)
