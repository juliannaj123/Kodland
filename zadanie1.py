import discord
import os
import random
import requests
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
# Create a bot instance with the intents enabled
bot = commands.Bot(command_prefix='!', intents=intents)

# zalogowano
@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

# ping pong
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# powiedz
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)

# papierkamiennozyce
@bot.command()
async def pkn(ctx, choice: str):
    choices = ['kamień', 'papier', 'nożyce']
    bot_choice = random.choice(choices)
    player_choice = choice.lower()

    if player_choice not in choices:
        await ctx.send("Masz do wyboru tylko 'kamień', 'papier', lub 'nożyce'.")
        return

    if player_choice == bot_choice:
        await ctx.send(f'Obydwoje wybraliśmy {bot_choice}. Remis!')
    elif (player_choice == 'kamień' and bot_choice == 'nożyce') or \
         (player_choice == 'papier' and bot_choice == 'kamień') or \
         (player_choice == 'nożyce' and bot_choice == 'papier'):
        await ctx.send(f'Wybrałeś/aś {player_choice}, a ja wybrałem {bot_choice}. Wygrywasz!')
    else:
        await ctx.send(f'Wybrałeś/aś {player_choice}, a ja wybrałem {bot_choice}. Wygrałem!')

# rzut monmeta
@bot.command()
async def coinflip(ctx, choice: str):
    choices = ['orzeł', 'reszka']
    bot_choice = random.choice(choices)
    player_choice = choice.lower()

    if player_choice not in choices:
        await ctx.send("Wybierz 'orzeł' lub 'reszka'.")
        return

    if player_choice == bot_choice:
        await ctx.send(f'Wybrałeś/aś {player_choice} a wypadł/a {bot_choice}. Wygrywasz')
    else:
        await ctx.send(f'Wybrałeś/aś {player_choice} a wypadł/a {bot_choice}. Przegrywasz!')

@bot.command()
async def losowymem(ctx):

    image_files = os.listdir('images')

    if image_files:
        chosen_image = random.choice(image_files)
        image_path = os.path.join('images', chosen_image)
        with open(image_path, 'rb') as file:
            await ctx.send(file=discord.File(file))
    else:
        await ctx.send("No images found in the 'images' folder.")

# Command: Random Dog Picture
@bot.command()
async def dog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    if response.status_code == 200:
        data = response.json()
        image_url = data['message']
        await ctx.send(image_url)
    else:
        await ctx.send("nie udało mi się załadować tego obrazu. ")

# recyklign
@bot.command()
async def recycle(ctx, item: str):
    bins = {
        'plastik': 'Żółty kosz',
        'szkło': 'Zielony kosz',
        'papier': 'Niebueski kosz',
        'bioodpady': 'Brązowy kosz',
        'baterie': 'Kosz na elektronikę',
        'elektronika': 'Kosz na elektronikę'
    }

    item = item.lower()

    if item in bins:
        await ctx.send(f'{item.capitalize()} powinieneś wyrzucić do  {bins[item]}.')
    else:
        await ctx.send("Przepraszam, nie znam takiego przedmiotu. Podaj inny.")

#token bota
bot.run('MTIwOTE4Njg5NjAxODkzOTkxNg.GP0i6w.WEOEV_m2emyXMhwLqZEjf4nuh3QxDNiD1E8ZxM')
