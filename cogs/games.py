import discord
from discord.ext import commands
import logging
from jeevesbot import functions, babbelbingo
from logging import getLogger


# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Games(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def roll(self, ctx):
        parameters = ctx.message.content.split(' ', 1)
        if len(parameters) == 2:
            param = parameters[1]
            roll,result = functions.roll(param)
            msg = f'Rolling %s for {ctx.message.author.mention}: `%s`'.format(roll) % (param,roll)
            logline = f'Rolling %s for {ctx.message.author}: `%s`'.format(roll) % (param,roll)
            log.info(logline)
            await ctx.send(msg)


    @commands.command()
    @commands.guild_only()
    async def bingo(self, ctx):
        name = ctx.message.author.name
        bingocard = babbelbingo.bingo(name)
        await ctx.author.send(file=discord.File(bingocard))


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


def setup(bot):
    bot.add_cog(Games(bot))