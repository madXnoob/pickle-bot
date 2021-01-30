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

    response = ''
    if 'vikings' in message.content.lower():

        responses = [
            'Yeah well the Scotts beat the vikings, did the germans beat the vikings josh? Didnt think so','scotts are better then vikings, because they are','scotts literally and unironically kicked the vikings arses','Although the Battle of Largs was apparently not considered a significant event by contemporaries, later historians transformed it into an event of international importance. Today, most scholars no longer subscribe to such a view, and instead accord it just an important place in the failed Norwegian campaign.'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['midget','midgets']:

        responses = [
            'I fucking hate midgets.','If i found out my kid was going to be a midget i would abort it.','I just dont think the deserve to live.'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['piggle']:

        responses = [
            'Fuck Piggle. I said it'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['stupid shit','fuck you']:

        responses = [
            'whoa'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['family','fam','familia']:
        responses = [
            'FamBam :)'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['so what are you guys playing?','what game we palying','what game we playing?','trying to play games?','what we gonna play','what we gonna play?']:

        responses = [
            'I miss swift'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['cant leaving work']:

        responses = [
            'You trying to play games?'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['hey guys whats up','hey guys whats up?']:

        responses = [
            'Nah'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['get on']:

        responses = [
            'cant watching crown','cant watching wanda caca','cant watching haunting at hill house','cant studying then fooders','cant watching dark','cant taking a shize'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['im on']:

        responses = [
            'Took too long get ditched'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['good']:

        responses = [
            'Good x2'
        ]
        response = random.choice(responses)
    elif client.user in message.mentions or message.content.lower() in ['famBam','jake','@FamBam']:

        responses = [
            'WhatT'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['too much money']:

        responses = [
            'Jew Bastid'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['smack?','smack']:

        responses = [
            'Yeahers with peen'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['im on swift']:

        responses = [
            'I miss swift'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['david']:

        responses = [
            'Daavviidd'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['code','coding']:

        responses = [
            'Print Hello World'
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