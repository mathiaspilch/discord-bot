import discord
from discord.ext import commands

import json

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

TOKEN = config_data['token']

description = """Description text"""
bot = commands.Bot(command_prefix='!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    """ Says world"""
    await ctx.send("world")

@bot.command()
async def turist(ctx):
    """ Says Turist"""
    await ctx.send("Turist")

@bot.command()
async def add(ctx, left : int, right : int):
    """Adds two integers together."""
    await ctx.send(left + right)

@add.error # <- the name of the command + .error
async def add_error(ctx, error):
    #if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Enter two integers, stupid!")

@bot.command()
async def div(ctx, numerator: float, denominator: float):
    """Divides two floats."""
    await ctx.send(numerator / denominator)


emoji_numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]

@bot.event
async def week(message):
    if message.channel.name == ("test"):
        if message.content.startswith("Week"):
            for emoji in emoji_numbers:
                await message.add_reaction(emoji)
        await bot.process_commands(message)

bot.run(TOKEN)