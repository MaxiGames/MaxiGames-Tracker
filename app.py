import discord
from discord.ext import commands
import os
import time
import json

client = commands.Bot(command_prefix="interesting this bot has no commands", help_command=None, intents = discord.Intents.all())

@client.event
async def on_ready():
    print("Logged in as maxigames tracker :D")

@client.command()
async def testmaxigamesgoesoffline(ctx):
    before = ctx.author
    before.status = discord.Status.online

    after = ctx.author
    after.status = discord.Status.offline
    await on_member_update(before, after)

@client.event
async def on_member_update(before, after):
    if before.id != 863419048041381920:
        return
    if before.status == discord.Status.online and after.status == discord.Status.offline:
        channel = client.get_channel(879718535499227156)
        print(f"{time.ctime(time.time())}: {before.name} has gone offline")
        message = await channel.send(embed = discord.Embed(title=f"{time.ctime(time.time())}: {before.name} has gone offline", colour=0xff0000))
        await message.publish()
        return
    
    if before.status == discord.Status.offline and after.status == discord.Status.online:
        channel = client.get_channel(879718535499227156)
        print(f"{time.ctime(time.time())}: {before.name} has come online")
        message = await channel.send(embed = discord.Embed(title=f"{time.ctime(time.time())}: {before.name} has come back online", colour=0x00ff00))
        await channel.send("<@&879718955772702750>")
        await message.publish()

with open("serviceAccountKey.json", "r") as f:
    data = json.load(f)
    client.run(data["tokenId"]) 