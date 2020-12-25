import discord
import requests
import json
import random
from datetime import datetime
from discord.ext import commands

client = discord.Client()

serialy = [
"Gotham",
"Breaking Bad",
"The Big Bang Theory",
"Umbrella Academy",
"Stranger Things <3",
"Narcos",
"Narcos: Mexico",
"Vikings",
"Sex Education",
"Cobra Kai",
"House Of Cards",
"Better Call Saul",
"Black Summer",
"Teen Wolf",
"Peaky Blinders",
"Daredevil",
"Punisher",
"Jessica Jones",
"Iron Fist",
"Luke Cage",
"Altered Carbon",
"Black Mirror",
"You",
"The Blacklist",
"Ozark",
"Mindhunter",
"Le Casa De Papel <3",
"The Witcher",
"13 Reasons Why",
"Orange Is The New Black",
"The Society",
"Spinning Out",
"Titans",
"Gossip Girl",
"Elite",
"I'm Not Okay With This",
"The End Of The F***ing World",
"Gilmore Girls",
"Atypical",
"How To Get Away With Murder",
"Too Hot To Handle",
"Love, Death + Robots",
"Outer Banks",
"Lucifer",
"Friends",
"Riverdale",
"How To Sell Drugs Online (Fast)",
"Bojack Horseman",
"Arrow",
"Barbarians",
"Wu Assassins",
"Epidemiya",
"Biohackers",
"Sherlock",
"Locke & Key",
"Emily In Paris",
"Community",
"Dead To Me",
"Glow",
"Good Girls",
"Paradise PD",
"The Queen's Gambit",
"La Révolution",
"The Crown",
"Insatiable",
"Locked Up",
"Big Mouth",
"Travelers",
"3%",
"The Rain",
"Chilling Adventures Of Sabrina",
"Lost In Space",
"The Haunting",
"Ratched",
"Shadowhunters: The Mortal Instruments",
"Star Trek (v Česku jen Discovery)",
"South Park",
"Good Place",
"On My Block",
"Ragnarok",
"Control Z",
"You Me Her",
"Never Have I Ever",
"Warrior Nun",
"Brooklyn Nine-Nine",
"Black Lightning",
"Sick Note",
"Van Helsing",
"Cursed",
"The Protector",
"Glitch",
"The Order",
"Diablero",
"Anne With An E",
"Dark"
]





class Netflix(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Netflix command - ✔️")

    # commands

    @commands.command()
    async def netflix(self, ctx):
        embed = discord.Embed(title="Náhodný netflix seriál", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.add_field(name="Zkus tenhle -", value=f"{random.choice(serialy)}")
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Aktivoval příkaz ,netflix"
        print(log_message, file=open('log.txt', 'a'))

        await ctx.send(embed=embed)
        
        
def setup(client):
    client.add_cog(Netflix(client))
