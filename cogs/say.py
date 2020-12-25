import discord
from datetime import datetime
from discord.ext import commands

client = discord.Client()

class Say(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Say command - ✔️")

    # command
    @commands.command()
    
    async def say(self, ctx, *, texts, amount=1):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(title=texts, color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Aktivoval příkaz ,say"
        print(log_message, file=open('log.txt', 'a'))
    
       

        await ctx.send(embed=embed)
       

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title=":x: **Chybí ti tam argument! Použij prosím správnou formulaci** `,say text`",
                                  color=discord.Color.red())
            ted = str(datetime.now()) 
            log_message= ted + " | "+ctx.message.author.name + " Se pokusil ktivovat příkaz ,say ale má asi 0 iq takže nenapsal co mám psát..."
            print(log_message, file=open('log.txt', 'a'))
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Say(client))
