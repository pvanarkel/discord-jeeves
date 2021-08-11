import discord
from discord.ext import commands
import log


# setup logging
logger = log.get_logger(__name__)


e = discord.Embed()


class Misc(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def hug(self, ctx):
        msg = f'Jeeves geeft {ctx.message.author.mention} een grote knuffel'
        await ctx.send(msg)


    @commands.command()
    async def eirik(self, ctx):
        await ctx.send('Deze vraag heeft Eirik Fatland al beantwoord in 1997.')


    @commands.Cog.listener()
    async def on_ready(self):
        print('##### RANDOM module active')


def setup(bot):
    bot.add_cog(Misc(bot))