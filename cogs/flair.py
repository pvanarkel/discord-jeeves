import discord
from discord.ext import commands
from logging import getLogger
from jeevesbot import env

# setup logging
log = getLogger(__name__)
e = discord.Embed()


class Flair(commands.Cog):
    """ This part of the bot is responsible for giving users roles! """
    def __init__(self, bot):
        self.bot = bot
        self.message_id = 1087124044119281675
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


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Flair(bot))
