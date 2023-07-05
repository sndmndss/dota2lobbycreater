import time
import discord
from discord.ext import commands
import embeds

from apikeys import *

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@client.event
async def onready():
    print("The bot is working now")
    print('-------------------------------------------')

@client.event
async def on_message_delete(message):
    channel = client.get_channel(1125820992304984064)
    await channel.send(embed=embeds.LogDelete(message))
    if len(str(message.content)) >= 2000:
        embeds.LogTxtDelete(message)
        with open("message.txt", "rb") as file:
            await channel.send(file=discord.File(file, "message.txt"))
    elif len(str(message.content)) < 2000 and len(str(message.content)) >= 256:
        await channel.send(str(message.content))
        await channel.send(embed=embeds.SplitEmbed())


@client.event
async def on_message_edit(message_before, message_after):
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    channel = client.get_channel(1125820992304984064)
    await channel.send(embed=embeds.LogEdit(message_before,message_after))
    if len(str(message_before.content)) >= 2000 or len(str(message_after.content)) >= 2000:
        embeds.LogTxtEdit(message_before,message_after)
        with open("message.txt", "rb") as file:
            await channel.send(file = discord.File(file, "message.txt"))
    elif len(str(message_before.content)) <2000 and len(str(message_before.content)) >256 or len(str(message_after.content)) <2000 and len(str(message_after.content)) >256:
        await channel.send(str(message_before.content))
        embed = discord.Embed(title="To:")
        await channel.send(embed=embed)
        await channel.send(str(message_after.content))
        await channel.send(embed=embeds.SplitEmbed())



client.run(TOKEN)
