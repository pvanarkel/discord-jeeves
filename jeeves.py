#!/usr/bin/env python3.9

import discord
from discord.ext import commands
import logging
from jeevesbot import env
import os

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('jeeves')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='jeeves.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# setup discord.py bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
e = discord.Embed()


@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    print(extension, 'module loaded')


@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    print(extension, 'module unloaded')


@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    print(extension, 'module reloaded')


@bot.event
async def on_ready():
    print('### Active with id %s as %s ###' % (bot.user.id,bot.user.name) )
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


if __name__ == '__main__':
    bot.run(env.TOKEN)
