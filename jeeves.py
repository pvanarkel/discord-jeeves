#!/usr/bin/env python3

import discord
from discord.ext import commands
import logging
from jeevesbot import bothelp, functions, env
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('jeeves')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='jeeves.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# setup discord.py
client = discord.Client()
e = discord.Embed()
# setup gspread
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jeevesbot/secret.json', scope)
gclient = gspread.authorize(creds)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.content.startswith('!help'):
        parameters = message.content.split(' ', 1)
        if len(parameters) == 2:
            msg = format(bothelp.help(parameters[1]))
        else:
            msg = format(bothelp.help())
        await message.author.send(msg)
    # giphy and tenor both have different structures to their links
    if message.content.startswith('https://tenor.com/'):
        roles = functions.checkrole(message.author.roles)
        channel = functions.checkchannel(message.channel.id)
        embed_url = message.content
        follow_url = embed_url + '.gif'
        full_url = functions.resolve(follow_url)
        gif_url = full_url.split('?')[0]
        embed = e.set_image(url=gif_url)
        if channel is True:
            if roles is not True:
                await message.channel.send(embed=embed)
                logger.info(message.author)
                logger.info(gif_url)
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
                logger.info(message.author)
                logger.info(gif_url)
    if message.content.startswith('!roll'):
        parameters = message.content.split(' ', 1)
        if len(parameters) == 2:
            param = parameters[1]
            roll,result = functions.roll(param)
            msg = 'Rolling %s for {0.author.mention}: `%s`'.format(message) % (param,roll)
            await message.channel.send(msg)
            
@client.event
async def on_ready():
    print('### Active with id %s as %s ###' % (client.user.id,client.user.name) )
    activity = discord.Activity(name='Listening to !help', type=discord.ActivityType.listening)

if __name__ == '__main__':
    client.run(env.TOKEN)
