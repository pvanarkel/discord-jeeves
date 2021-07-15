import discord
from discord.ext import commands
import logging
from jeevesbot import functions, babbelbingo

e = discord.Embed()

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('jeeves')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='jeeves.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


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
            logger.info(logline)
            await ctx.message.channel.send(msg)


    @commands.command()
    @commands.guild_only()
    async def bingo(self, ctx):
        name = ctx.message.author.name
        bingocard = babbelbingo.bingo(name)
        guild = ctx.message.guild
        member = discord.utils.get(guild.members, id=ctx.message.author.id)
        role = discord.utils.get(guild.roles , name='babbelbingo')
        await ctx.author.send(file=discord.File(bingocard))
        await member.add_roles(role)


    @commands.Cog.listener()
    async def on_ready(self):
        print('##### GAMES module active')

def setup(bot):
    bot.add_cog(Games(bot))