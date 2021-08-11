import discord
from discord.ext import commands
import log


# setup logging
logger = log.get_logger(__name__)


e = discord.Embed()


class Links(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def youtube(self, ctx):
        await ctx.send('https://www.youtube.com/channel/UCTAnkjUOud_HdKhY_hi2ISA')


    @commands.command()
    async def donatie(self, ctx):
        await ctx.send('<https://bunq.me/larpzomerfestival>')


    @commands.Cog.listener()
    async def on_ready(self):
        print('##### LINKS module active')


def setup(bot):
    bot.add_cog(Links(bot))

