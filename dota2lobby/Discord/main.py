import time
import discord
from discord.ext import commands


from apikeys import *

client = commands.Bot(command_prefix='!', intents = discord.Intents.all())

@client.event
async def onready():
    print("The bot is working now")
    print('-------------------------------------------')

@client.event
async def on_message_delete(message):
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    if len(str(message.content)) < 256:
        embed = discord.Embed(title="{} deleted a message in {} text channel".format(str(message.author)[:-2],str(message.channel.name)),
                              description="", color=discord.Color.from_rgb(255, 0, 0))
        embed.add_field(name=message.content, value="This is the message that he has deleted ", inline = True)
        embed.add_field(name="Time:", value=time_string)
        channel = client.get_channel(1125820992304984064)
        await channel.send(embed=embed)
        print(message)
    else:
        channel = client.get_channel(1125820992304984064)
        embed = discord.Embed(
            title="{} deleted a message in {} text channel :".format(str(message.author)[:-2], str(message.channel.name)),
            description="", color=discord.Color.from_rgb(255, 0, 0))
        embed.add_field(name = "Time", value=time_string)
        await channel.send(embed=embed)
        await channel.send(str(message.content))
        embed = discord.Embed(title="-------------------------------------------------------")
        await channel.send(embed=embed)


@client.event
async def on_message_edit(message_before, message_after):
    if len(str(message_before.content)) < 256 and len(str(message_after.content)) < 256:
        embed=discord.Embed(title="{} edited a message in {} channel".format(str(message_before.author)[:-2], str(message_before.channel.name)),
        description="", color=discord.Color.from_rgb(255, 0, 100))
        embed.add_field(name= message_before.content ,value="This is the message before any edit",
        inline=True)
        embed.add_field(name= message_after.content ,value="This is the message after the edit",
        inline=True)
        channel=client.get_channel(1125820992304984064)#logs channel id
        await channel.send(embed=embed)
    else:
        if len(str(message_before.content)) < 256 or len(str(message_after.content)) < 256:
            channel = client.get_channel(1125820992304984064)#logs channel id
            embed = discord.Embed(title="{} edited a message in {} channel from: ".format(str(message_before.author)[:-2],
                                                                                str(message_before.channel.name)),
                                                                                description="", color=discord.Color.from_rgb(255, 0, 100))
        await channel.send(embed=embed)
        await channel.send(str(message_before.content))
        embed = discord.Embed(title="To:                                                                    ")
        await channel.send(embed=embed)
        await channel.send(str(message_after.content))
        embed = discord.Embed(title="----------------------------------------------------")
        await channel.send(embed=embed)
client.run(TOKEN)
