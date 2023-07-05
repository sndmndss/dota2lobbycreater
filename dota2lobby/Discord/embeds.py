import discord
import time



def LogEdit(message_before,message_after):
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    embed = discord.Embed(title="{} edited a message in {} channel".format(str(message_before.author)[:-2],
                                                                           str(message_before.channel.name)),
                          description="", color=discord.Color.from_rgb(255, 0, 100))
    if len(str(message_before.content)) < 256 and len(str(message_after.content)) <256:
        embed.add_field(name=message_before.content, value="This is the message before any edit",
                    inline=True)
        embed.add_field(name=message_after.content, value="This is the message after the edit",
                    inline=True)
    embed.add_field(name='Time: ', value= time_string)
    return embed

def LogTxtEdit(message_before,message_after):
    with open("message.txt", "w") as file:
        file.write('{}\n was changed to \n {}'.format(str(message_before.content), str(message_after.content)))
    pass

def LogTxtDelete(message):
    with open("message.txt", "w") as file:
        file.write('{}'.format(str(message.content)))
    pass

def SplitEmbed():
    embed = discord.Embed(title="-------------------------------------------------------")
    return embed

def LogDelete(message):
    named_tuple = time.localtime()
    time_string = time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
    embed = discord.Embed(
        title="{} deleted a message in {} text channel".format(str(message.author)[:-2], str(message.channel.name)),
        description="", color=discord.Color.from_rgb(255, 0, 0))
    if len(str(message.content)) < 256:
        embed.add_field(name=message.content, value="This is the message that he has deleted ", inline = True)
    embed.add_field(name='Time: ', value= time_string)
    return embed
