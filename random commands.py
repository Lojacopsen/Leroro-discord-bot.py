import discord
from discord.ext import commands,tasks
import random
from random import choice
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') #prefisso del bot

@client.event
async def on_ready():
    change_status.start()
    print('ready leroro')
    
client.run('your token') #the token -_-
