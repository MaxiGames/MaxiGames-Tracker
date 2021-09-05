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
        message = await channel.send(f"{time.ctime(time.time())}: {before.name} has gone offline <@&879718955772702750>")
        await message.publish()

        admin = client.get_channel(863400648681848873)
        await admin.send(f"{time.ctime(time.time())}: {before.name} has gone offline <@712942935129456671>, <@782247763542016010>, <@676748194956181505> and <@682592012163481616>")

with open("serviceAccountKey.json", "r") as f:
    data = json.load(f)
    client.run(data["tokenId"])