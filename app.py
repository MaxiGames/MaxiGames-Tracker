import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix="interesting this bot has no commands", help_command=None, intents = discord.Intents.all())


@client.event
async def on_ready():
    print("Logged in as maxigames tracker :D")

@client.event
async def on_member_update(before, after):
    if before.id != 863419048041381920:
        return
    if before.status == discord.Status.online and after.status == discord.Status.offline:
        channel = client.get_channel(874589313810186260)
        print(f"{before.name} has gone offline :O")
        await channel.send(f"{before.name} has gone offline :O")

client.run(os.getenv('maxigamestracker'))