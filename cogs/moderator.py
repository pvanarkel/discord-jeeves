import discord
from discord.ext import commands
import log


# setup logging
logger = log.get_logger(__name__)


e = discord.Embed()


class Moderator(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print('##### MODERATOR module active')


def setup(bot):
    bot.add_cog(Moderator(bot))