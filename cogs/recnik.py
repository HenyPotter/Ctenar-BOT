import discord
import requests
import json
import random
from datetime import datetime
from discord.ext import commands

client = discord.Client()

citat = [
"Neviděl jsme",
"To jsem nezaznamenal",
"To je trochu hozená rukavice",
"Hajzle",
"Počkej neukazuj moji plochu",
"Pochopil jsem, že mít v životě všechno je pěkně na hovno"
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
    async def citat(self, ctx):
        embed = discord.Embed(title="Citát", color=0xffff00, timestamp=ctx.message.created_at)
        embed.add_field(name="Tento je můj olíbený:", value=f"{random.choice(citat)}")
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Aktivoval příkaz ,citat"
        print(log_message, file=open('log.txt', 'a'))
        await ctx.send(embed=embed)



 

def setup(client):
    client.add_cog(Fun(client))
