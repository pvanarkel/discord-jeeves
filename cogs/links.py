import discord
from discord.ext import commands
from logging import getLogger


# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Links(commands.Cog):
    """ Handige linkjes! """

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def youtube(self, ctx):
        """ LARP Platform YouTube kanaal """
        await ctx.send('https://www.youtube.com/channel/UCTAnkjUOud_HdKhY_hi2ISA')


    @commands.command()
    async def donatie(self, ctx):
        """ LARP Platform / Stichting Verhaal in Uitvoering Donatie"""
        await ctx.send('<https://bunq.me/larpplatform>')


    @commands.command()
    async def agenda(self, ctx):
        """ LARP Agenda"""
        await ctx.send('<https://www.larp-platform.nl/kalender/>')


    @commands.command()
    async def evenementen(self, ctx):
        """ LARP Agenda Evenementenoverzicht"""
        await ctx.send('<https://www.larp-platform.nl/evenementenoverzicht/>')


    @commands.command()
    async def organisaties(self, ctx):
        """ LARP Agenda Organisatieoverzicht"""
        await ctx.send('<https://www.larp-platform.nl/organisaties/>')


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Links(bot))

