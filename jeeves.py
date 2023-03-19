#!/usr/bin/env python3.9

import discord
from discord.ext import commands
from jeevesbot import env
import os
import log
import logging.config
from logging import getLogger
import asyncio


# setup root logger handlers
logging.config.dictConfig(log.LOGGING)
# setup logging
log = getLogger(__name__)


# setup discord.py bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
e = discord.Embed()


@bot.command(name='load', hidden=True)
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    log.info(f'{ctx.message.author} loaded the {extension} module')


@bot.command(name='unload', hidden=True)
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    log.info(f'{ctx.message.author} unloaded the {extension} module')


@bot.command(name='reload', hidden=True)
@commands.has_permissions(administrator=True)
async def reload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    log.info(f'{ctx.message.author} reloaded the {extension} module')


async def load_extensions():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


@bot.event
async def on_ready():
    log.info(f'Active with ID:{bot.user.id} as {bot.user.name}')
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)


async def main():
    async with bot:
        await load_extensions()
        await bot.start(env.TOKEN)


asyncio.run(main())