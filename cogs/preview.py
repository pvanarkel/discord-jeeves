import discord
from discord.ext import commands
from jeevesbot import functions
from logging import getLogger
import re
import pytube
from pytube.exceptions import RegexMatchError

# setup logging
log = getLogger(__name__)


e = discord.Embed()


class Preview(commands.Cog):
    """ Ensures that high-risk channels don't display embedded links, but only gifs and youtube previews."""

    def __init__(self, bot):
        self.bot = bot
        self.video_id_regex = re.compile(r'(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/|m\.youtube\.com/(?:watch\?v=|embed/|v/))([^"&?/ ]{11})')


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
        if 'https://youtu' or 'https://m.youtu' or 'https://www.youtu' in message.content():
            roles = functions.checkrole(message.author.roles)
            channel = functions.checkchannel(message.channel.id)
            if channel is True:
                if roles is not True:
                    url = message.content
                    youtube = pytube.YouTube(url)
                    video_title = youtube.title
                    video_author = youtube.author
                    video_id = self.extract_video_id(url)
                    if video_id:
                        embed = discord.Embed()
                        embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg")
                        embed.set_author(name=f"{video_author}")
                        embed.add_field(name=f"", value=f"[{video_title}]({url})")
                        await message.channel.send(embed=embed)
                        log.info(f'User {message.author} requested preview for {url}')


    def extract_video_id(self, url):
        try: 
            match = self.video_id_regex.search(url)
            if match:
                return match.group(1)
        except pytube.exceptions.RegexMatchError as e:
            pass    


    @commands.Cog.listener()
    async def on_ready(self):
        log.info(f'module active')


async def setup(bot):
    await bot.add_cog(Preview(bot))