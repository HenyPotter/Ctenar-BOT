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
        print("Info command - ✔️ ")

    # cog usage
    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(title="**<:Ctenar:759776440450416671> Info**", colour=0x00c000, timestamp=ctx.message.created_at)
        embed.add_field(name="`Ping:` ", value=f"**{round(self.client.latency * 1000)}** ms", inline=False)
        embed.add_field(name="`API Version: `", value=f"**{discord.__version__}**", inline=False)
        embed.add_field(name="`Bot version:` ", value="**1.1**", inline=False)
        embed.add_field(name="`Bot developers:`", value="<@406894015204687872>,<@515242772454834177>")
        embed.set_footer(text=f"{self.client.user.name}", 
        icon_url=self.client.user.avatar_url)
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Aktivoval příkaz ,about asi je zvedavy"
        print(log_message, file=open('log.txt', 'a'))
       
        await ctx.send(embed=embed)
		
		

def setup(client):
    client.add_cog(Info(client))
