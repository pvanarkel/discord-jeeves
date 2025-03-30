#!/usr/bin/env python3.8

import discord
from discord.ext import commands, tasks
from jeevesbot import env
from jeevesbot.database import init_db, get_due_reminders
import os
import log
import logging.config
from logging import getLogger
import datetime
import asyncio


# Initialize the database
init_db()


# setup logging
logging.config.dictConfig(log.LOGGING)
log = getLogger(__name__)


# setup discord.py bot
intents = discord.Intents().all()
intents.message_content = True
e = discord.Embed()

class Jeeves(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents, help_command=None)
        self.guild_ids = [env.GUILD_ID]


    @commands.command(name='load', hidden=True)
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, extension):
        self.load_extension(f'cogs.{extension}')
        log.info(f'{ctx.message.author} loaded the {extension} module')


    @commands.command(name='unload', hidden=True)
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, extension):
        self.unload_extension(f'cogs.{extension}')
        log.info(f'{ctx.message.author} unloaded the {extension} module')


    @commands.command(name='reload', hidden=True)
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, extension):
        self.unload_extension(f'cogs.{extension}')
        self.load_extension(f'cogs.{extension}')
        log.info(f'{ctx.message.author} reloaded the {extension} module')


    async def load_extensions(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')


    @tasks.loop(seconds=60)
    async def check_reminders(self):
        now = datetime.datetime.now().isoformat()
        reminders = get_due_reminders(now)
        for reminder in reminders:
            user = self.get_user(reminder[1])
            if user:
                try:
                    await user.send(reminder[2])
                except Exception as e:
                    log.error(f'Error sending reminder to user {reminder[1]}: {e}')


    async def on_ready(self):
        log.info(f'Active with ID:{self.user.id} as {self.user.name}')
        activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
        await self.change_presence(activity=activity)
        # Sync commands for all guilds
        for guild_id in self.guild_ids:
            guild = discord.Object(id=guild_id)
            try:
                await self.tree.sync(guild=guild)
                log.info(f'Successfully synced commands for guild {guild_id}')
            except discord.errors.Forbidden as e:
                log.error(f'Failed to sync commands for guild {guild_id}: {e}')
        # Start the reminder check loop
        if not self.check_reminders.is_running():
            self.check_reminders.start()


    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found.')
            log.warning(f'Command not found: {ctx.message.content}')
        else:
            await ctx.send('An error occurred.')
            log.error(f'An error occurred: {error}')


async def main():
    bot = Jeeves()
    await bot.load_extensions()
    await bot.start(env.TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
