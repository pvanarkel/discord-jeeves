#!/usr/bin/env python3

import discord
from discord.ext import commands
import logging
from jeevesbot import bothelp, functions, env, babbelbingo

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('jeeves')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='jeeves.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# setup discord.py bot
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)
e = discord.Embed()

@bot.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == bot.user:
        return
    if message.content.startswith('!help'):
        parameters = message.content.split(' ', 1)
        if len(parameters) == 2:
            msg = bothelp.help(parameters[1])
        else:
            msg = bothelp.help()
        await message.author.send(msg)
        logline = (str(message.author) + ' requested help')
        logger.info(logline)
    # giphy and tenor both have different structures to their links
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
                logger.info(logline)
    if message.content.endswith('.gif'):
        roles = functions.checkrole(message.author.roles)
        channel = functions.checkchannel(message.channel.id) 
        embed_url = message.content
        embed = e.set_image(url=embed_url)
        if channel is True:
            if roles is not True:
                await message.channel.send(embed=embed)
                logline = (str(message.author) + ' requested a gif: ' + str(embed_url))
                logger.info(logline)       
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
                logger.info(logline)
    if message.content.startswith('!roll'):
        parameters = message.content.split(' ', 1)
        if len(parameters) == 2:
            param = parameters[1]
            roll,result = functions.roll(param)
            msg = 'Rolling %s for {0.author.mention}: `%s`'.format(message) % (param,roll)
            await message.channel.send(msg)
    if message.content.startswith('!bingo'):
        name = message.author.name
        bingocard = babbelbingo.bingo(name)
        guild_id = message.guild.id
        guild = discord.utils.find(lambda g: g.id == guild_id, bot.guilds)
        member = discord.utils.get(guild.members, id=message.author.id)
        role = discord.utils.get(guild.roles , name='babbelbingo')
        await message.author.send(file=discord.File(bingocard))
        await member.add_roles(role)
    if message.content.startswith('!youtube'):
        msg = 'https://www.youtube.com/channel/UCTAnkjUOud_HdKhY_hi2ISA'
        await message.channel.send(msg)     
    if message.content.startswith('!blokkenschema'):
        msg = 'https://www.larp-platform.nl/zomer-festival/blokkenschema/'
        await message.channel.send(msg)
    if message.content.startswith('!donatie'):
        msg = 'https://bunq.me/larpzomerfestival'
        await message.channel.send(msg)
        
@bot.event
async def on_ready():
    print('### Active with id %s as %s ###' % (bot.user.id,bot.user.name) )
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await bot.change_presence(activity=activity)

if __name__ == '__main__':
    bot.run(env.TOKEN)
