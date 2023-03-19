import discord
from discord.ext import commands
from logging import getLogger
from jeevesbot import env


# setup logging
log = getLogger(__name__)

embed = discord.Embed()

class BotSetup(commands.Cog):
    """ Admin Commands, Use at own risk. """
    def __init__(self, bot):
        self.bot = bot
        self.botchannel = int(env.BOTCHANNEL[0])
    

    @commands.command(hidden=True)
    @commands.is_owner()
    async def flairsetup(self, ctx):
        """ Setup reaction post as embed. """
        await ctx.message.delete()
        channel_id = ctx.channel.id
        if (channel_id) == (self.botchannel):
            embed = discord.Embed(title="Kies je rollen!", 
                description="Klik op de emoji onder het bericht om de rol te krijgen.")
            embed.add_field(name="", value="", inline=False)
            embed.add_field(name="Voornaamwoorden:", value="", inline=False)        
            embed.add_field(name=":one:", value="hij/hem")
            embed.add_field(name=":two:", value="zij/haar")
            embed.add_field(name=":three:", value="hen/hun")
            embed.add_field(name=":four:", value="die/hun")
            embed.add_field(name=":five:", value="die/diens")
            embed.add_field(name=":six:", value="iedere/all")
            embed.add_field(name="Sta je open voor Direct Messages van andere serverleden?", value="", inline=False)
            embed.add_field(name=":thumbsup:", value="DM: ja")
            embed.add_field(name=":thumbsdown:", value="DM: nee")
            embed.add_field(name="Rollen voor toegang tot opt-in kanalen.", value="", inline=False)
            embed.add_field(name=":underage:", value="serieuze-onderwerpen")
            embed.set_footer(text="Mis je een voornaamwoord of heb je ideeën voor een andere rol? Laat het de mods weten in de #ideeënbus!\nJe kan zelf je rollen verwijderen door opnieuw op de emoji te drukken.")
            message = await ctx.send(embed=embed)
            await message.add_reaction("1️⃣")
            await message.add_reaction("2️⃣")
            await message.add_reaction("3️⃣")
            await message.add_reaction("4️⃣")
            await message.add_reaction("5️⃣")
            await message.add_reaction("6️⃣")
            await message.add_reaction("👍")
            await message.add_reaction("👎")
            await message.add_reaction("🔞")
            log.warn(f'{ctx.message.author} reset the flair embed, new message_id = {message.id}')
        else:
            log.warn(f'{ctx.message.author} tried setting up the flair in the wrong channel')


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(BotSetup(bot))