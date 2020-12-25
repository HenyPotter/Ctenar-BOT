import discord
from discord.ext import commands
from datetime import datetime

client = discord.Client()


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    # cog has been successfully loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("help command - ✔️ ")

    # cog usage
    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Commandy:", colour=0x00c000, description=",about - Řekne info o Botovi  \n,oms - Vybere náhodný díl OMS \n,citat - Řekne šťťavnatý citát pana Kazmy \n,netflix - Idk to přidal Heny \n,profile <uživatel> - Řekne info o dedikovaném uživateli \n,avatar <uživatel> - Ukáže avatar dedikovaného uživatele")
 
        await ctx.send(embed=embed)
		
		

def setup(client):
    client.add_cog(Info(client))
