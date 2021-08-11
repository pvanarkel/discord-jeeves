import discord
from discord.ext import commands
from logging import getLogger


# setup logging
log = getLogger(__name__)


embed = discord.Embed()


class Admin(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        log.warn(f'{ctx.message.author.name} cleared {amount} messages')
        

    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


def setup(bot):
    bot.add_cog(Admin(bot))