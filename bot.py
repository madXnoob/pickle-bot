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
            'I fucking hate midgets.','If i found out my kid was going to be a midget i would abort it.','I just dont think they deserve to live.'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['golden agers']:

        responses = [
            'remember when we used to play party bash all the time?','remember when josh brought mom to the apartment?','remember going to coffee factory?','remember when chris wanted some m&ms from josh and josh didnt share?','remember watching the soccer world cup and reno said if i make it peru wins?','remember when swift came over to clean my shize?','remember when we went to epcot with josh?'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['muff','i miss muff','moffa','i miss moffa']:

        responses = [
            'Samers','I wonder if muff is thinking about me','I could of touched muffs vagene'
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
            'this dick'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['leave him']:

        responses = [
            'He had his chance'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['get ditched']:

        responses = [
            'Yeah yeah tell me something i dont know'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['shut up']:

        responses = [
            'Nah'
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
    elif message.content.lower() in ['this bot sucks','bot sucks','bot is trash']:

        responses = [
            'your mom'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['i miss muff']:

        responses = [
            'samers'
        ]
        response = random.choice(responses)
    elif message.content.lower() in ['get on','hop on','get online','join voice chat','join chat','get in here you bastid','get in here','join']:

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
    elif message.content.lower() in ['what time ow','what time ow?','what time overwatch','what time overwatch?','overwatch','overwatch?']
    
        responses = [
            'AND THEY SAY CHIVARLY IS DEAD','is this easy mode?','you are nothing without me','is rein main on?','someone call the whambulance','Have some Lucio-Ohs','In the desert, the cheetah lives for 3 years, the camel lives for 9','DIPSTICK'
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