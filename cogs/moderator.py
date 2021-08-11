import discord
from discord.ext import commands
from logging import getLogger


# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Moderator(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')
        

def setup(bot):
    bot.add_cog(Moderator(bot))