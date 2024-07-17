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

