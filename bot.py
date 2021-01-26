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



async def greet(guild):
    print_to_stdout('Greeting')
    greetings = [
        'TOUCHDOWN!'
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

    response= ''
    if 'vikings' in message.content.lower():

        responses = [
            'Yeah well the Scotts beat the vikings soooo','scotts are better then vikings','scotts literally and unironically kicked the vikings arses'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['midget','midgets']

         responses = [
        'I fucking hate midgets'
        ]
         responses = random.choice(responses)
    elif message.content.lower() in ['stupid shit']:

        responses = [
            'woah'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['family','fam','familia']:
        responses = [
            'FamBam :)'
        ]
        response = random.choice(responses)
    else: return

    await asyncio.sleep(1.5)

    await message.channel.send(response)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print_to_stdout(f'{client.user} is connected to the following guild:\n'
    f'{guild.name}(id: {guild.id})')

    await greet(guild)


client.run(TOKEN)
