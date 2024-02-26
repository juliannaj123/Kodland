import discord
import random
from discord.ext import commands
from bot_logic import rpsc, random_number

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='&', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def greet(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def repeat(ctx, count_repeat = 5):
    n= " "
    await ctx.send(n= input('Jakie słowo powtórzyć?'))
    await ctx.send(x * count_repeat)

@bot.command()
async def goodbye(ctx):
    await ctx.send(f'Do widzenia!')

@bot.command()
async def rockpaperscissors(ctx):
    await ctx.send(rpsc())

@bot.command()
async def randomnumber(ctx):
    await ctx.send(random_number())

bot.run("MTIwOTE4Njg5NjAxODkzOTkxNg.GlE_px.xw-0raYOX82np_pwzSkb7536EudhRbROZ-zFI8")
