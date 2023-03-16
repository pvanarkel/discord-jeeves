import discord
from discord.ext import commands
from logging import getLogger
from jeevesbot import env

# setup logging
log = getLogger(__name__)
e = discord.Embed()


class Flair(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.message_id = 1084937456819908679
        self.reactions = {
            '1️⃣' : env.FLAIRROLES[0],
            '2️⃣' : env.FLAIRROLES[1],
            '3️⃣' : env.FLAIRROLES[2],
            '4️⃣' : env.FLAIRROLES[3],
            '5️⃣' : env.FLAIRROLES[4],
            '6️⃣' : env.FLAIRROLES[5],
            '👍' : env.FLAIRROLES[6],
            '👎' : env.FLAIRROLES[7],
            '🔞' : env.FLAIRROLES[8],
        }
  
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        try:
            if payload.message_id == self.message_id and str(payload.emoji) in self.reactions:
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                role_id = self.reactions[str(payload.emoji)]
                role = guild.get_role(role_id)
                flairrole = guild.get_role(env.FLAIRROLE[0])
                await member.add_roles(flairrole)
                await member.add_roles(role)
                log.info(f'Added role "{role}" to {member}')
        except:
            log.debug("Reaction not found.")

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        try:
            if payload.message_id == self.message_id and str(payload.emoji) in self.reactions:
                guild = self.bot.get_guild(payload.guild_id)
                member = guild.get_member(payload.user_id)
                role_id = self.reactions[str(payload.emoji)]
                role = guild.get_role(role_id)
                await member.remove_roles(role)
                log.info(f'Removed role "{role}" from {member}')
        except:
            log.debug("Could not remove role")

    @commands.command(name='flairsetup', hidden=True)
    @commands.is_owner()
    async def flairsetup(self, ctx):
        """ Setup reaction post as embed. """
        await ctx.message.delete()
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

    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')

async def setup(bot):
    await bot.add_cog(Flair(bot))
