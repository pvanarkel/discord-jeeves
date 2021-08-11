import discord
from discord.ext import commands
import log


# setup logging
logger = log.get_logger(__name__)

embed = discord.Embed()


class Admin(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        logger.warn(f'{ctx.message.author.name} cleared {amount} messages')
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('##### ADMIN module active')


def setup(bot):
    bot.add_cog(Admin(bot))