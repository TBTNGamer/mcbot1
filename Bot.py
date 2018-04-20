import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?!")

chat_filter = ["FUCK", "NIGGER", "NIGGA", "BITCH", "ASSHOLE", "IDIOT", "MORON", "KYS", "KMS", "F!CK", "FREAK", "CUNT", "MANIAC", "FUCKED", "SHUT UP", "SHIT", "DUMB", "IDIOT", "FAGGOT", "DARN", "MOTHERFUCKER", "MOTHER FUCKER", "ASS", "BASTARD", "CRAP", "HELL", "HOLY SHIT", "SHIT ASS", "SHITASS", "WHORE", "TWAT"]
bypass_list = ["282509271470440450", "418774360770215947", "259664007772897280"]


@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content.upper().startswith('?!MC'):
        await client.send_message(message.channel,"Eh? Did someone mention me?")
    if message.content.upper().startswith('?!SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    contents = message.content.split(" ")
    for word in contents: #content is a list type
        if word.upper() in chat_filter:
            #do something
            if not message.author.id in bypass_list:
                #filter is disabled for those who are in the bypass list
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "**Hey!** You're not allowed to say that in here!")
                except discord.errors.NotFound:
                    return


client.run("NDM2OTAzNTA1ODc0MTI0ODAy.DbuqiA.iRW2sGjWzC05Wp5c_AgZox5I0EI")


