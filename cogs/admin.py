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


class Admin(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    @commands.is_owner()
    async def clear(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)
        logger.warn(f'{ctx.message.author.name} cleared {amount} messages')
        

    @commands.Cog.listener()
    async def on_ready(self):
        print('##### ADMIN module active')


def setup(bot):
    bot.add_cog(Admin(bot))