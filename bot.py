import discord
from discord.ext import commands
import json
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord-bot.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

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


@bot.event
async def on_message(message):
    """Reacts with all seven weekdays to messages starting with 'Week'."""
    if message.channel.name in ("test", "rocksmith-practice"):
        print(message.content)
        #emoji = discord.utils.get(client.emojis, name=':zero:')
        #emoji_numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣"]
        weekdays = ['<:monday:875851243191418991>',
            '<:tuesday:875851259217846272>',
            '<:wednesday:875851270521487400>',
            '<:thursday:875851282110357564>',
            '<:friday:875851291694346301>',
            '<:saturday:875851306110156830>',
            '<:sunday:875851318055534602>']

        if message.content.startswith("Week"):
            #await message.channel.send("pies are better than cakes. change my mind.")
            for emoji in weekdays:
                await message.add_reaction(emoji)
        await bot.process_commands(message)

bot.run(TOKEN)