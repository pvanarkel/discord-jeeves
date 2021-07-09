#!/usr/bin/env python3

from collections import defaultdict
import time
import discord
from discord.ext import commands
import sys
import ast
import itertools
from discord.utils import get

from pyasn1.type.constraint import PermittedAlphabetConstraint

# general @ test = 749399756752814105

# setup discord.py bot
intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)

if len(sys.argv) >= 2:
    params = sys.argv[1:]
else:
    print("Missing parameter input.")

async def score(question, score):
    e = discord.Embed(title='Emoji-VVDD', color=discord.Color.green())
    e.set_author(name='Jeeves', icon_url='https://cdn.hippogrief.nl/jeevesbot/jeeves.jpg')
    e.add_field(name=question, value='\u200b', inline=False)
    e.add_field(name='Hoogste score:', value=score, inline=False)
    e.set_thumbnail(url='https://cdn.hippogrief.nl/jeevesbot/logo.jpg')
    return score
    
async def run_script(params):
    params = params
    channel = client.get_channel(790908319005933598)  # vvdd 729667183126511617 # tech 790908319005933598 # test 749399756752814105
    emoji_numbers = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    question = params[0] # string
    answers = ast.literal_eval(params[1]) # list
    number_of_responses = len(answers) # int
    e = discord.Embed(title='Emoji-VVDD', description='Klik de emoji beneden dit bericht om te stemmen op het antwoord wat bij de emoji hoort.', color=discord.Color.blue())
    e.set_author(name='Jeeves', icon_url='https://cdn.hippogrief.nl/jeevesbot/jeeves.jpg')
    e.add_field(name=question, value='\u200b', inline=False)
    for emoji, answer in zip(emoji_numbers, answers):
        e.add_field(name=emoji, value=answer, inline=False)
    e.set_thumbnail(url='https://cdn.hippogrief.nl/jeevesbot/logo.jpg')
    message = await channel.send(embed=e)
    for i in range(number_of_responses):
        await message.add_reaction(emoji_numbers[i])
    for i in range(24, -1, -1):
        time.sleep(60)
    message = await channel.fetch_message(message.id)
    
    values = {}
    for i in message.reactions:
        itervalues = {str(i): int(i.count)}
        values.update(itervalues)
    max_key = max(values, key=values.get)
    all_values = values.values()
    max_value = max(all_values)
    highest_keys = [key for key in values if values[key] == max_value]

    if len(highest_keys) == 1:
        max_key = highest_keys[0]
        hoogste_score = 'Hoogste score:'
    elif len(highest_keys) != 1:
        max_key = highest_keys
        print(max_key)
        hoogste_score = 'Gelijkspel tussen:'

    score = (str(max_key) + '  met ' + str(max_value) + ' stemmen.')
    f = discord.Embed(title='Emoji-VVDD', color=discord.Color.green())
    f.set_author(name='Jeeves', icon_url='https://cdn.hippogrief.nl/jeevesbot/jeeves.jpg')
    f.add_field(name=question, value='\u200b', inline=False)
    f.add_field(name=hoogste_score, value=score, inline=False)
    f.set_thumbnail(url='https://cdn.hippogrief.nl/jeevesbot/logo.jpg')
    message = await channel.send(embed=f)
    
    await client.close()

@client.event
async def on_ready():
    print('### Active with id %s as %s ###' % (client.user.id,client.user.name) )
    activity = discord.Activity(name='!help', type=discord.ActivityType.listening)
    await client.change_presence(activity=activity)
    await run_script(params)

if __name__ == '__main__':
    client.run('ODE5NjMyNDg1MjU5ODA0NzU0.YEpcPA.I-i1tDIV1vP7FW6-8cA7YLH5lN4')