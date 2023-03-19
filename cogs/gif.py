import discord
from discord.ext import commands
from jeevesbot import functions
from logging import getLogger


# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Gif(commands.Cog):
    """ Ensures that high-risk channels don't display embedded links, but only gifs."""

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('https://tenor.com/'):
            roles = functions.checkrole(message.author.roles)
            channel = functions.checkchannel(message.channel.id)
            embed_url = message.content
            follow_url = embed_url + '.gif'
            full_url = await functions.resolve(follow_url)
            gif_url = full_url.split('?')[0]
            embed = e.set_image(url=gif_url)
            if channel is True:
                if roles is not True:
                    await message.channel.send(embed=embed)
                    logline = (str(message.author) + ' requested a gif: ' + str(gif_url))
                    log.info(logline)
        if message.content.endswith('.gif'): 
            roles = functions.checkrole(message.author.roles)
            channel = functions.checkchannel(message.channel.id) 
            embed_url = message.content
            embed = e.set_image(url=embed_url)
            if channel is True:
                if roles is not True:
                    await message.channel.send(embed=embed)
                    logline = (str(message.author) + ' requested a gif: ' + str(embed_url))
                    log.info(logline)       
        if message.content.startswith('https://giphy.com/'):
            roles = functions.checkrole(message.author.roles)
            channel = functions.checkchannel(message.channel.id)
            embed_url = message.content
            image_code = embed_url.split('-')[-1]
            gif_url = 'https://media.giphy.com/media/' + image_code + '/giphy.gif'
            embed = e.set_image(url=gif_url)        
            if channel is True:
                if roles is not True:
                    await message.channel.send(embed=embed)
                    logline = (str(message.author) + ' requested a gif: ' + str(gif_url))
                    log.info(logline)


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Gif(bot))