import discord
from discord.ext import commands,tasks
import random
from random import choice
import discord
from discord.ext import commands

@client.event
async def on_ready():
    change_status.start()
    print('ready leroro2!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Leroro'):
        await message.channel.send('PREGATEMI SCHIAAAVI')
    
client.run('your token') #the token -_-
