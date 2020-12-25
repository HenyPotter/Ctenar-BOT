import discord
from datetime import datetime
import random
from discord.ext import commands

dil = [
"Katty perry \n https://www.televizeseznam.cz/video/onemanshow/kazma-ukradl-slavu-svetove-megastar-180152",
"Jim carrey \n https://www.televizeseznam.cz/video/onemanshow/odhaleni-nejvetsiho-ceskeho-podvodu-ktery-obletel-celou-planetu-180187",
"Yes Man \n https://www.televizeseznam.cz/video/onemanshow/jedinecny-experiment-co-se-stane-kdyz-10-dni-na-vsechny-vyzvy-odpovidate-ano-180217",
"Casting \n https://www.televizeseznam.cz/video/onemanshow/takhle-vypada-nejsilenejsi-pracovni-pohovor-180257",
"MS v hokeji 2016 \n https://www.televizeseznam.cz/video/onemanshow/dva-cesi-se-trestuhodnym-zpusobem-nabourali-na-zahajeni-ms-2016-v-moskve-180287",
"Dacjukova Brusle \n https://www.televizeseznam.cz/video/onemanshow/ruska-televize-vyhlasila-za-dopadeni-kazmy-odmenu-1-000-000-rublu-180342",
"OMS pack teaser <3 \n https://www.televizeseznam.cz/video/onemanshow/1000x-oms-pack-za-24hod-to-odstartuje-180117",
"Justin Bieber \n https://www.televizeseznam.cz/video/onemanshow/novy-dil-plny-neuveritelnych-zvratu-skoncil-zalobou-justina-biebera-180362",
"Prostřeno \n https://www.televizeseznam.cz/video/onemanshow/odhaleni-nejvetsiho-televizniho-skandalu-v-cesku-180407",
"Leoš Mazec \n https://www.televizeseznam.cz/video/onemanshow/odhaleni-skandalu-prohrane-sazky-o-ferrari-za-8-000-000-kc-180552",
"BucketList \n https://www.televizeseznam.cz/video/onemanshow/jagr-pomohl-kazmovi-napalit-davida-copperfielda-a-je-z-toho-skandal-po-celem-svete-64036056",
"Trippleshot \n https://www.televizeseznam.cz/video/onemanshow/prezident-milos-zeman-se-stal-obeti-dlouho-utajovane-mystifikace-64093182",
"s Honzou Zelenkou \n https://www.televizeseznam.cz/video/onemanshow/honza-zelenka-180047"
]


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    # loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("OMS - ✔️")

    # command

    @commands.command()
    async def oms(self, ctx):
        embed = discord.Embed(title="OMS", color=0xffff00,)
        embed.add_field(name="Doporučuji díl", value=f"{random.choice(dil)}")

        ted = str(datetime.now()) 
        log_message= ted + " | "+ctx.message.author.name + " Aktivoval příkaz ,oms asi nevi na co se divat :thonk"
        print(log_message, file=open('log.txt', 'a'))
        
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
