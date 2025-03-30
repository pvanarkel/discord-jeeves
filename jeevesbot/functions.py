#!/usr/bin/env python 3

from jeevesbot import env
import aiohttp
import dice

# This function is necessary for tenor, because they do not allow linking directly to the gif and need resolving. ASYNC VERSION
async def resolve(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            message = response.url
    return str(message)

# use the dice module for rolling.
def roll(notation):
    roll = dice.roll(notation)
    result = int(roll)
    return roll,result

<<<<<<< HEAD
# check if user has admin role and output True if it's the case.
def checkrole(roles):
    for role in roles:
        if str(role) == env.ADMIN_ROLE:
            return True

# check if the source channel is in the list of channels that are watched by the bot.
def checkchannel(channelid):
    if channelid in env.GIFCHANNELS:
        return True
    else:
        return False

=======
>>>>>>> d194332843b93f36e724aeca0dcd41c96a10ae95
