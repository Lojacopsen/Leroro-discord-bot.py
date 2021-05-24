#leroro discord bot by lojacoppisi
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
    print('ready leroro')

@tasks.loop(seconds=300) 
async def change_status():
    status = ['pagare ture','distruggere universi','scoparsi lerora','mangiare lojacops'] #stato del bot 
    await client.change_presence(activity=discord.Game(choice(status)))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Leroro'):
        await message.channel.send('PREGATEMI SCHIAAAVI') #le risposte ad una scritta dell'utente

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('UwU'):
        await message.channel.send('zitto tu!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('CIBAKU TENSEI!'):
        await message.channel.send('TENGAI SHINSEI!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('ZAWARUDO!'):
        await message.channel.send('*dio time stop*')


client.run('your token!') #Metti il token del bot UwU
#questo è solo un template, non aspettatevi chissà che.
