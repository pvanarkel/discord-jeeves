import discord
from discord.ext import commands
from jeevesbot import functions, env
from logging import getLogger
import re
import pytube
from pytube.exceptions import RegexMatchError, VideoUnavailable, ExtractError

# setup logging
log = getLogger(__name__)


class Preview(commands.Cog):
    """ Ensures that high-risk channels don't display embedded links, but only gifs and youtube previews."""


    def __init__(self, bot):
        self.bot = bot
        self.video_id_regex = re.compile(r'(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|youtu\.be/|m\.youtube\.com/(?:watch\?v=|embed/|v/))([^"&?/ ]{11})')
        self.e = discord.Embed()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore messages from bots


        if message.content.startswith('https://tenor.com/'):
            is_admin = message.author.guild_permissions.administrator
            is_high_risk_channel = self.check_channel(message.channel.id)
            embed_url = message.content
            follow_url = embed_url + '.gif'
            full_url = await functions.resolve(follow_url)
            gif_url = full_url.split('?')[0]
            embed = self.e.set_image(url=gif_url)
            if is_high_risk_channel and not is_admin:
                await message.channel.send(embed=embed)
                logline = (str(message.author) + ' requested a gif: ' + str(gif_url))
                log.info(logline)


        if message.content.startswith('https://giphy.com/'):
            is_admin = message.author.guild_permissions.administrator
            is_high_risk_channel = self.check_channel(message.channel.id)
            embed_url = message.content
            image_code = embed_url.split('-')[-1]
            gif_url = 'https://media.giphy.com/media/' + image_code + '/giphy.gif'
            embed = self.e.set_image(url=gif_url)        
            if is_high_risk_channel and not is_admin:
                await message.channel.send(embed=embed)
                logline = (str(message.author) + ' requested a gif: ' + str(gif_url))
                log.info(logline)


        if message.content.endswith('.gif'): 
            is_admin = message.author.guild_permissions.administrator
            is_high_risk_channel = self.check_channel(message.channel.id)
            embed_url = message.content
            embed = self.e.set_image(url=embed_url)
            if is_high_risk_channel and not is_admin:
                await message.channel.send(embed=embed)
                logline = (str(message.author) + ' requested a gif: ' + str(embed_url))
                log.info(logline)   


        if 'https://youtu' in message.content or 'https://m.youtu' in message.content or 'https://www.youtu' in message.content:
            is_admin = message.author.guild_permissions.administrator
            is_high_risk_channel = self.check_channel(message.channel.id)
            if is_high_risk_channel and not is_admin:
                url = message.content
                try:
                    youtube = pytube.YouTube(url)
                    video_title = youtube.title
                    video_author = youtube.author
                    video_id = self.extract_video_id(url)
                    if video_id:
                        embed = discord.Embed()
                        embed.set_image(url=f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg")
                        embed.set_author(name=video_author)
                        embed.add_field(name="", value=f"[{video_title}]({url})")
                        await message.channel.send(embed=embed)
                        log.info(f'User {message.author} requested preview for {url}')
                except (VideoUnavailable, ExtractError, KeyError) as e:
                    log.error(f'Error extracting YouTube video details for {url}: {e}')
                    await message.channel.send('Sorry, there was an error retrieving the YouTube video details.')


    def check_channel(self, channel_id):
        high_risk_channels = env.PREVIEWCHANNELS
        return channel_id in high_risk_channels

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