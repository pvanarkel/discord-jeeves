import discord
from discord.ext import commands
from logging import getLogger

# setup logging
log = getLogger(__name__)
e = discord.Embed()


class CustomHelp(commands.Cog):
    """ Help """
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):
        """ Help """
        await ctx.message.delete()
        with open("help/help.md", "r") as f:
            contents = f.read()
        embed = discord.Embed(title="Help", description=contents, color=discord.Color.blue())
        await ctx.author.send(embed=embed)
        log.warn(f'{ctx.message.author} asked for help!')


    @commands.command()
    async def info(self, ctx):
        """ Info about Jeeves """
        await ctx.message.delete()
        with open("help/info.md", "r") as f:
            contents = f.read()
        embed = discord.Embed(title="Info over Jeeves", description=contents, color=discord.Color.yellow())
        await ctx.author.send(embed=embed)
        log.warn(f'{ctx.message.author} asked for info!')


    @commands.command(hidden=True)
    @commands.is_owner()
    async def adminhelp(self, ctx):
        """ Admin Help """
        await ctx.message.delete()       
        with open("help/adminhelp.md", "r") as f:
            contents = f.read()
        embed = discord.Embed(title="Admin Help", description=contents, color=discord.Color.red())
        await ctx.author.send(embed=embed)
        log.warn(f'{ctx.message.author} asked for adminhelp!')
    

    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')

async def setup(bot):
    await bot.add_cog(CustomHelp(bot))
