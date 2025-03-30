import discord
from discord.ext import commands
from logging import getLogger

# setup logging
log = getLogger(__name__)

e = discord.Embed()


class Misc(commands.Cog):
    """ Van alles en nog wat. """

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def eirik(self, ctx):
        await ctx.send('Deze vraag heeft Eirik Fatland al beantwoord in 1997.')


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Misc(bot))
