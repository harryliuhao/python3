# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 22:00:02 2020

@author: Hao
"""
import PIL
from PIL import Image, ImageEnhance, ImageDraw, ImageFont

# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def create_banner(image,channel,intensity,fontpath):
    banner = Image.new("RGB", (image.width, 80))
    draw=ImageDraw.Draw(banner)
    # specified font size 
    font = ImageFont.truetype(fontpath, fontsize)  
    text = 'channel {} intensity {}'.format(channel,intensity)
    draw.text((0, 0), text, fill ="white", font = font, align ="left") 
    return banner

fontsize=75
fontpath='readonly/fanwood-webfont.ttf'
channels=[0,1,2]
intensity=[0.1,0.5,0.9]
# read image and convert to RGB


images=[]

for c in channels:
    for i in intensity:
        banner=create_banner(image,str(c),str(i),fontpath)
        combined_image=get_concat_v(image,banner)
        source = combined_image.split()
        mid = source[c].point(lambda x:x*i)
        source[c].paste(mid)
        im = Image.merge(combined_image.mode, source)
        images.append(im)
        

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0

for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)
