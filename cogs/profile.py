import discord
from datetime import datetime
from discord.ext import commands

client = discord.Client()

class Profile(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Profile command - ✔️")

    # command
    @commands.command()
    async def profile(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        is_member_bot = member.bot
        if is_member_bot == True:
            is_member_bot = ":white_check_mark:*ANO* "
        else:
            is_member_bot = ":no_entry_sign:*NE* "


        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member.top_role} {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        embed.add_field(name=":id: **ID:**", value=f"||{member.id}||", inline=False)
        embed.add_field(name=":back: Account has been created:",
                        value=member.created_at.strftime("%a, %d, %B, %Y, %I: %M, %p UTC"), inline=False)
        embed.add_field(name=":trophy: Nejvyšší role:", value=member.top_role.mention, inline=False)
        embed.add_field(name=":robot: Bot?", value=is_member_bot, inline=False)

        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Je asi stalker, protože aktivoval příkaz ,profile"
        print(log_message, file=open('log.txt', 'a'))
        await ctx.send(embed=embed)

    @profile.error
    async def profile_error(self, ctx, error):
        embed = discord.Embed(title="**Chybí ti tam argument! Použij prosím správné zformulování** `,profile @zmínka`",
                              color=discord.Color.red())
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " se pokusil napsat ,profile ale má asi 0 iq, protože nenapsal jaký profil ho zajímá..."
        print(log_message, file=open('log.txt', 'a'))
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member:discord.Member):
        embed = discord.Embed(title=" ", color=discord.Color.blurple(), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member}")
        embed.set_image(url=member.avatar_url)
        embed.set_footer(text="{}".format(ctx.message.author.name), icon_url=ctx.author.avatar_url)
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Je asi stalker, protože aktivoval příkaz ,avatar"
        print(log_message, file=open('log.txt', 'a'))
        await ctx.send(embed=embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        embed = discord.Embed(title="**Chybí ti tam argument! Použij prosím správné zformulování** `,avatar @zmíka`",
                              color=discord.Color.red())
        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " se pokusil napsat ,avatar ale má asi 0 iq, protože nenapsal jaký avatar ho zajímá..."
        print(log_message, file=open('log.txt', 'a'))      
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Profile(client))
