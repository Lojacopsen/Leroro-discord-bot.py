import discord
from discord.ext import commands,tasks
import random
from random import choice
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') #prefisso del bot

@client.command(pass_context=True,help = ".clear [n messaggi]") #cancella n messaggi (il comando clear conta già come suo messaggio)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
        messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send('Leroro ha cancellato il lavoro degli spammoni')

@client.event
async def on_ready():
    change_status.start()
    print('ready leroro1')
