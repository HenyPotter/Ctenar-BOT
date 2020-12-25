import discord
import requests
import json
import random
from datetime import datetime
from discord.ext import commands

client = discord.Client()

kamil = [
    "borec",
    "frajer",
    "Frajírek",
    "OMSF ignorant",
    "loupežník",
    "podvodník",      
    "podomní prodejce židlí",
    "chilli prankster",
    "leakovač obecný",
]





class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Prodejce židlí  - ✔️")

    # command

    @commands.command()
    async def kazma(self, ctx):
        embed = discord.Embed(title="Kamil", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.add_field(name="Kazma je", value=f"{random.choice(kamil)}")
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Aktivoval příkaz ,kazma"
        print(log_message, file=open('log.txt', 'a'))
        await ctx.send(embed=embed)



 

def setup(client):
    client.add_cog(Fun(client))
