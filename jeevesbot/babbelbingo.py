#!/usr/bin/env python3

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import random
from PIL import Image, ImageFont, ImageDraw
import textwrap

# setup gspread
scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('jeevesbot/secret.json', scope)
gclient = gspread.authorize(creds)

# load babbelbingofile
def babbelbingo_file():
    file = gclient.open_by_key("1zdWl17fhdT2P96ZgjSwB_2wsCHi_ZVA42JroX5d1ylc")
    babbelbingo = file.get_worksheet(1)
    values =  babbelbingo.get_all_values()
    list_values = [item for sublist in values for item in sublist]
    questions = random.sample(list_values, k=24)
    return questions

def make_bingocard(name, questions):
    image = Image.open('jeevesbot/files/bingokaart.png')
    font_name = ImageFont.truetype('jeevesbot/files/Overpass-regular.ttf', 13)
    draw = ImageDraw.Draw(image)
    wrapper = textwrap.TextWrapper(width=20, break_on_hyphens=True)
    box01 = '\n'.join(wrapper.wrap(questions[0]))
    box02 = '\n'.join(wrapper.wrap(questions[1]))
    box03 = '\n'.join(wrapper.wrap(questions[2]))
    box04 = '\n'.join(wrapper.wrap(questions[3]))
    box05 = '\n'.join(wrapper.wrap(questions[4]))
    box06 = '\n'.join(wrapper.wrap(questions[5]))
    box07 = '\n'.join(wrapper.wrap(questions[6]))
    box08 = '\n'.join(wrapper.wrap(questions[7]))
    box09 = '\n'.join(wrapper.wrap(questions[8]))
    box10 = '\n'.join(wrapper.wrap(questions[9]))
    box11 = '\n'.join(wrapper.wrap(questions[10]))
    box12 = '\n'.join(wrapper.wrap(questions[11]))
    box13 = '\n'.join(wrapper.wrap(questions[12]))
    box14 = '\n'.join(wrapper.wrap(questions[13]))
    box15 = '\n'.join(wrapper.wrap(questions[14]))
    box16 = '\n'.join(wrapper.wrap(questions[15]))
    box17 = '\n'.join(wrapper.wrap(questions[16]))
    box18 = '\n'.join(wrapper.wrap(questions[17]))
    box19 = '\n'.join(wrapper.wrap(questions[18]))
    box20 = '\n'.join(wrapper.wrap(questions[19]))
    box21 = '\n'.join(wrapper.wrap(questions[20]))
    box22 = '\n'.join(wrapper.wrap(questions[21]))
    box23 = '\n'.join(wrapper.wrap(questions[22]))
    box24 = '\n'.join(wrapper.wrap(questions[23]))
    draw.multiline_text((95, 280.5),  box01, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((229, 280.5), box02, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((363, 280.5), box03, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((497, 280.5), box04, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((631, 280.5), box05, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((95, 399.5),  box06, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((229, 399.5), box07, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((363, 399.5), box08, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((497, 399.5), box09, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((631, 399.5), box10, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((95, 518.5),  box11, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((229, 518.5), box12, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((497, 518.5), box13, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((631, 518.5), box14, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((95, 637.5),  box15, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((229, 637.5), box16, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((363, 637.5), box17, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((497, 637.5), box18, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((631, 637.5), box19, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((95, 756.5),  box20, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((229, 756.5), box21, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((363, 756.5), box22, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((497, 756.5), box23, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    draw.multiline_text((631, 756.5), box24, (0, 0, 0), font=font_name, align='center', anchor='mm', spacing=8)
    image.save('jeevesbot/files/generated_bingocards/' + name + '.png')

def bingo(name):
    questions = babbelbingo_file()
    make_bingocard(name, questions)
    bingoimage = ('jeevesbot/files/generated_bingocards/' + name + '.png')
    return bingoimage
