import discord
from discord.ext import commands
from jeevesbot import functions, babbelbingo
from logging import getLogger


# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Games(commands.Cog):
    """ Deze commando's zijn gerelateerd aan spelletjes op de Discord server. """
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.guild_only()
    async def bingo(self, ctx):
        """ Maak een babbelbingo kaart (staat niet altijd aan) """
        name = ctx.message.author.name
        bingocard = babbelbingo.bingo(name)
        await ctx.author.send(file=discord.File(bingocard))
    
    
    @commands.command()
    async def roll(self, ctx):
        """ Roll the dice! 

        Simple rolls
            !roll 1d20+6
            !roll 1d20-(2+6)
            !roll 1d20-4+(1d4+3)

        Advanced rolls
            !roll 1d20x(N)
                exploding dice, will add extra dice on each roll above threshold N. If N is not defined, will default to maximum possible roll.
            !roll 6d6^(N)
                highest N dicerolls will be kept, so 6d6^2 will keep the highest two dice.
            !roll 6d6m(N)
                middle N dicerolls will be kept, so 6d6m2 will keep the middle two dice.
            !roll 6d6v(N)
                lowest N dicerolls will be kept, so 6d6l2 wil keep the lowest two dice.
            !roll 2d6r(N)
                will reroll any dice that are below threshold N. The reroll is possible to be below the threshold N.
            !roll 2d6rr(N)
                will reroll any dice that are below threshold N. The reroll will be at the very minimum threshold N.
            !roll 10d10s
                will sort the rolls in order, this will not change the result.
        
        """
        parameters = ctx.message.content.split(' ', 1)
        if len(parameters) == 2:
            param = parameters[1]
            roll,result = functions.roll(param)
            msg = f'Rolling %s for {ctx.message.author.mention}: `%s`'.format(roll) % (param,roll)
            logline = f'Rolling %s for {ctx.message.author}: `%s`'.format(roll) % (param,roll)
            log.info(logline)
            await ctx.send(msg)


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Games(bot))