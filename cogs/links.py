import discord
from discord.ext import commands
import logging

e = discord.Embed()

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('jeeves')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='jeeves.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


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

