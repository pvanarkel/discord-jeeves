import discord
from discord.ext import commands
from jeevesbot import env
import datetime
from jeevesbot.database import add_reminder
from logging import getLogger


# setup logging
log = getLogger(__name__)


class Reminders(commands.Cog):
    """ Reminder command"""
    def __init__(self, bot):
        self.bot = bot


    @discord.app_commands.command(name='remindme', description='Set a reminder - Use YY-MM-DD HH:MM:SS notation')
    @discord.app_commands.guilds(discord.Object(id=env.GUILD_ID))
    async def remindme(self, interaction: discord.Interaction, time: str, message: str):
        try:
            reminder_time = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            add_reminder(interaction.user.id, message, reminder_time.isoformat())
            await interaction.response.send_message(f'Reminder set for {reminder_time}')
            log.info(f'Reminder set by {interaction.user} for {reminder_time}: {message}')
        except ValueError:
            await interaction.response.send_message('Invalid time format. Use YYYY-MM-DD HH:MM:SS', ephemeral=True)
            log.warn(f'Reminder set by {interaction.user} went wrong.')


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')

async def setup(bot):
    await bot.add_cog(Reminders(bot))
    log.info(f'Added Reminders.remindme as command')



