import discord
from discord.ext import commands
from logging import getLogger


# setup logging
log = getLogger(__name__)


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
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Links(bot))

