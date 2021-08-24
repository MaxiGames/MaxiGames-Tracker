import discord
from discord.ext import commands
import os
import time

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
        await channel.send(f"{time.ctime(time.time())}: {before.name} has gone offline <@&879718955772702750>")
client.run(os.getenv('maxigamestracker'))