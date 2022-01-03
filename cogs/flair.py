import discord
from discord.ext import commands
from logging import getLogger
import asyncio


# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Flair(commands.Cog):
    """ The Flair functionality enables the user to setup flair for their profile.

    Currently, the flair-roles available are:
    - gender pronouns
    - willingness to join mature discussions
    - whether or not they are open for DMs

    """

    def __init__(self, bot):
        self.bot = bot
        self.msg1 = ['✅', '❌', '❔']

    @commands.command()
    async def flair(self, ctx):
        msg1 = (
            f'Welkom bij de flair-wizard! Gebruik onderstaande opties om verder te gaan. \n\n'
            f'Druk op ✅ als je verder wil gaan met de wizard.\n'
            f'Als je niet je flair opnieuw wilt instellen, druk dan op ❌.\n'
            f'Gebruik ❔ als je wil weten hoe je via een tekstcommando alles kan instellen.\n\n'
        )
        dm = await ctx.author.send(msg1)
        log.info(f'{ctx.author} started the flair wizard')
        for emoji in self.msg1:
            await dm.add_reaction(emoji)


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


def setup(bot):
    bot.add_cog(Flair(bot))



    # numbers_reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣']
