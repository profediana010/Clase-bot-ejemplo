import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def gen_pass(x):
    elements = "+-/*!&$#?=@<>123456789ABDFIODMSIAMqiedmosoawidm"
    password = ""

    for i in range(x):
        password += random.choice(elements)

    return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def bye(ctx):
    await ctx.send('chau')
    
@bot.command()
async def psw(ctx, longitud= 10):
    await ctx.send(f'Tu contraseña es 🙊: {gen_pass(longitud)}')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


bot.run("")
