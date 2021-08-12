#!/usr/bin/env python3.9

import discord
from discord.ext import commands
from jeevesbot import env
import os
import log
import logging.config
from logging import getLogger



# setup root logger handlers
logging.config.dictConfig(log.LOGGING)

# setup logging
log = getLogger(__name__)


# setup discord.py bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)
e = discord.Embed()


@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    log.info(f'{ctx.message.author} loaded the {extension} module')


@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    log.info(f'{ctx.message.author} unloaded the {extension} module')


@bot.command()
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    log.info(f'{ctx.message.author} reloaded the {extension} module')


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

