#Importer
import discord

from discord.ext import commands

#variables
bot = commands.Bot(command_prefix = "!")

jeton = "NzI2NTUxMTAxODEzMjkzMDU4.Xvj0Ug.L8fHPFp6uayqXujpuhrLWasfO38"



@bot.event
async def on_ready():
    print("BoT opérationnel")
    await bot.change_presence(activity=discord.Game("Mon créateur boss a fond !")
    )
    print("ne pas déranger svp")

# créer la commande !regles

@bot.command()
async def vénèrele18(ctx):
     await ctx.send("vivele 18 alehluia houuu 18 18 18 18")

@bot.command()
async def présentetoi(ctx):
     await ctx.send(""" 18 . Bonjour je suis Pyrabot, un bot proggramé en Python et crée par Pyranox, ce dont je suis fier car Pyranox est vraiment un boss. Et je suis d'autant plus fier que mon premier mot que j'ai envoyé soit 18.  18""")



#18 . Bonjour je suis Pyrabot, un bot proggramé en Python et crée par Pyranox, ce dont je suis fier car Pyranox est vraiment un boss. Et je suis d'autant plus fier que mon premier mot que j'ai envoyé soit 18.  18

print("lancement du bot...")

bot.run(jeton)