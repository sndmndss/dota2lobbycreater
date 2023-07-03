import discord
from discord.ext import commands

from apikeys import *

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@client.event
async def onready():
    print("The bot is working now")
    print('-------------------------------------------')

@client.command()
async def hello(ctx):
    await ctx.send('Пися попа')

client.run(TOKEN)