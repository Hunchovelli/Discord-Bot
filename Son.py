import discord
import os
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
            
    print (f'{client.user} has connected to the following guild:\n' 
           f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    user_messages = ['wagwan', 'hi', 'wys', 'yo', 'hey' 'hello', 'yoo']
    welcome_messages = ['yo bro','wys bro', 'hi', 'hey', 'hello', 'what\'s good bro']
    if message.content.lower() in user_messages:
        response = random.choice(welcome_messages)
        await message.reply(f'{response} {message.author}')
   

client.run(TOKEN) 