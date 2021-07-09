#!/usr/bin/env python3

import discord
from discord.ext import commands
from discord.ext.commands import bot
from discord.utils import get
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
client = commands.Bot(command_prefix='!', intents=intents)
e = discord.Embed()

# listen for emojis (set message id and role id in env.py)
@client.event
async def on_raw_reaction_add(payload):
    message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
    member = discord.utils.get(guild.members, id=payload.user_id)
    role = guild.get_role(env.EMOJIREACTROLE)
    reaction = discord.utils.get(message.reactions, emoji="☎️")
    if message.id in env.EMOJIREACTMSG and reaction is not None:
        await member.add_roles(role)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
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
    if message.content.startswith('https://c.tenor.com/'):
        roles = functions.checkrole(message.author.roles)
        channel = functions.checkchannel(message.channel.id) 
        embed_url = message.content
        embed = e.set_image(url=embed_url)
        if channel is True:
            if roles is not True:
                await message.channel.send(embed=embed)
                logline = (str(message.author) + ' requested a gif: ' + str(embed_url))
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
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        member = discord.utils.get(guild.members, id=message.author.id)
        role = discord.utils.get(guild.roles , name='babbelbingo')
        print(role)
        await message.author.send(file=discord.File(bingocard))
        await member.add_roles(role)    
        

@client.event
async def on_ready():
    print('### Active with id %s as %s ###' % (client.user.id,client.user.name) )
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)

if __name__ == '__main__':
    client.run(env.TOKEN)


    #     message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    # guild_id = payload.guild_id
    # guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
    # member = discord.utils.get(guild.members, id=payload.user_id)
    # role = guild.get_role(env.EMOJIREACTROLE)
    # reaction = discord.utils.get(message.reactions, emoji="☎️")
    # if message.id in env.EMOJIREACTMSG and reaction is not None:
    #     await member.add_roles(role)