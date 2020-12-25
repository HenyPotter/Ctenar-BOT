import discord
import json
import os
import dotenv
import requests
from keep_alive import keep_alive

from discord.ext import commands
from dotenv import load_dotenv




client = discord.Client()
client = commands.Bot(command_prefix=",")
client.remove_command("help")
load_dotenv()
TOKEN = os.getenv('TOKEN')



@client.event  
async def on_ready():
    print("-------------------------")
    print("Bot Name: " + client.user.name)
    print(client.user.id)
    print("API Version: " + discord.__version__)
    print(client.latency * 1000)
    print("-------------------------")

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="onemanshow na rozdané televizi"))

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == "✅":
        role = discord.utils.get(user.server.roles, id=686296864496287777)
        await client.add_roles(user, role)



for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

keep_alive()
client.run(TOKEN)

