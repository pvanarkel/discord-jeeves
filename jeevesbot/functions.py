#!/usr/bin/env python 3

from jeevesbot import env
import urllib
import dice

# This function is necessary for tenor, because they do not allow linking directly to the gif and need resolving.
def resolve(url):
    return urllib.request.urlopen(url).url

# use the dice module for rolling
def roll(notation):
    roll = dice.roll(notation)
    result = int(roll)
    return roll,result

def checkrole(roles):
    for role in roles:
        if str(role) == env.ADMIN_ROLE:
            return True

def checkchannel(channelid):
    if channelid in env.GIFCHANNELS:
        return True
    else:
        return False
