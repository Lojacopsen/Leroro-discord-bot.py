import discord
from discord.ext import commands,tasks

@client.event
async def on_ready():
    change_status.start()
    print('ready leroro2!')
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Leroro'):
        await message.channel.send('PREGATEMI SCHIAAAVI')#it's fun
    
client.run('your token') #the token -_-
