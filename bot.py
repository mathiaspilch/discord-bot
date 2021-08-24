import discord
from discord.ext import commands
import json
import logging
import re

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
    #print(bot.user.id)
    print('------')

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


@bot.command()
async def week(ctx, arg: int):
    """Enter '!week 12' and the bot will react with weekday emojis"""
    if arg in range(1, 52+1):
        await ctx.send(f'Week {arg}')
    else:
        await ctx.send('Number must be between 1 and 52.')


@week.error
async def week_error(ctx, error):
    await ctx.send('Something went wrong. Check if input number is an integer.')


@bot.event
async def on_message(message):
    """Reacts with all seven weekdays to messages starting with 'Week'."""
    if message.channel.name in ("test", "rocksmith-practice"):
        msg = message.content

        match = re.search(r"(?i)^week\s(\d+)", msg) # (?1): case insensitive modifier
        if match:
            calendar_week = int(match.group(1))
            if calendar_week in range(1, 52+1):

                weekdays = ['<:monday:875851243191418991>',
                    '<:tuesday:875851259217846272>',
                    '<:wednesday:875851270521487400>',
                    '<:thursday:875851282110357564>',
                    '<:friday:875851291694346301>',
                    '<:saturday:875851306110156830>',
                    '<:sunday:875851318055534602>']

                #if msg.startswith("Week"):
                for emoji in weekdays:
                    await message.add_reaction(emoji)

            else:
                await message.reply('Number must be between 1 and 52.')

        await bot.process_commands(message)


'''
@bot.event
async def on_message(message):
    if message.channel.name in ("test", "rocksmith-practice"):
        if message.content.startswith("!week"):
            await bot.message.delete()
'''

bot.run(TOKEN)