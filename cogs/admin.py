from discord.ext import commands
from logging import getLogger
import typing
from datetime import timedelta
from discord import User, errors, TextChannel, Forbidden

# setup logging
log = getLogger(__name__)


class Admin(commands.Cog):
    """ Admin Commands, Use at own risk. """
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='purge', hidden=True)
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, amount=1):
        """ Purge <n> messages from current channel"""
        await ctx.message.delete()
        await ctx.channel.purge(limit = amount)
        log.warn(f'{ctx.message.author} purged {amount} messages')
    

    @commands.command(name='purge_from', hidden=True)
    @commands.has_permissions(administrator=True)
    async def purge_from(self, ctx, message_id: int):
        """Purge all messages after the given message.id"""
        try:
            message = await ctx.channel.fetch_message(message_id)
        except errors.NotFound:
            log.warn(f'{ctx.message.author} tried purging {message_id}, but id was not found.')
            return
        await ctx.message.delete()
        await ctx.channel.purge(after=message)
        log.info(f'{ctx.message.author} purged all messages after {message_id}')
        return True


    @commands.command(name='purge_user', hidden=True)
    @commands.is_owner()
    async def purge_user(self, ctx, user: User, num_minutes: typing.Optional[int] = 5):
        """Clear all messages of <user.id> in all channels within the last [n=5] minutes"""
        after = ctx.message.created_at - timedelta(minutes=num_minutes)
        def check(msg):
            return msg.author.id == user.id
        for channel in await ctx.guild.fetch_channels():
            if type(channel) is TextChannel:
                try:
                    await channel.purge(limit=10*num_minutes, check=check, after=after)
                    log.info(f'{ctx.message.author} purged all messages from {user.id} that were posted within the last {num_minutes}')
                except Forbidden:
                    continue

    
    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Admin(bot))