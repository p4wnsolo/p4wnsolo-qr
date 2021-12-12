#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-2020 Richard Hull and contributors
# See LICENSE.rst for details.
# PYTHON_ARGCOMPLETE_OK

"""
Greyscale rendering demo.
"""

import time
from pathlib import Path
from demo_opts import get_device
from luma.core.render import canvas
from PIL import Image
from subprocess import Popen, PIPE
from PIL import ImageFont
import SH1106
import RPi.GPIO as GPIO
import sys

from PIL import Image
from PIL import ImageDraw

##### Set mode here
themode = 'ssh'
#themode = 'spiderfoot'  # Experimental (spiderfoot not yet implemented)

#GPIO define
RST_PIN        = 25
CS_PIN         = 8
DC_PIN         = 24

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13

KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

#init GPIO
# for P4:
# sudo vi /boot/config.txt
# gpio=6,19,5,26,13,21,20,16=pu
GPIO.setmode(GPIO.BCM) 
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up



# 240x240 display with hardware SPI:
disp = SH1106.SH1106()
disp.Init()

# Init some variables
prefix = ''
size_x = 63
size_y = 63
sleep_time = 5
iconfont = prefix + 'DroidSansMono.ttf'  # Editor's number 1 pick
iconsize14 = ImageFont.truetype(prefix + iconfont, 14)    
font1 = 'DroidSansMono.ttf'
fontsize1 = 12
thefont1 = ImageFont.truetype(prefix + font1, fontsize1)
font2 = 'Prototype.ttf'
fontsize2 = 12
thefont2 = ImageFont.truetype(prefix + font2, fontsize2)
fonturl = 'DroidSansMono.ttf'
fontsizeurl = 8
urlfont = ImageFont.truetype(prefix + fonturl, fontsizeurl)
shape1 = [(114, 14), (126, 26)]
shape2 = [(114, 29), (126, 41)]
shape3 = [(114, 44), (126, 56)]
btn1 = '+'
btn2 = '+'
btn3 = 'X'

######## Set service variables
if 'spider' in themode:
	#### Spiderfoot
	service_name = 'Spiderfoot'
	desc_line1 = 'Use with:'
	desc_line2 = 'Browser'
	urlprefix = 'http://'  # Browser 
	port = ':8000'  # Browser
else:
	#### SSH
	service_name = '       SSH'
	desc_line1 = 'Use with:'
	desc_line2 = 'SSH App'
	urlprefix = ''
	port = ':22'  



#Loading screen init variables
font3 = 'Prototype.ttf'
fontsize3 = 18
thefont3 = ImageFont.truetype(prefix + font3, fontsize3)
font4 = 'Prototype.ttf'
fontsize4 = 12
thefont4 = ImageFont.truetype(prefix + font4, fontsize4)

######Show the Loading Screen
image1 = Image.new('1', (disp.width, disp.height), "WHITE")
draw = ImageDraw.Draw(image1)

draw.text((1,2), 'Generating', font = thefont3, fill = 0)
draw.rectangle(((0, 26), (127, 45)), fill="black")

draw.text((0,25), ' ' + service_name, font = thefont3, fill = 255)
draw.text((0,45), 'QR Code. Please wait..', font = thefont4, fill = 0)
disp.ShowImage(disp.getbuffer(image1))
######################


######Get IP
filepath = './qr.png'
part1 = '/sbin/ifconfig wlan0 | grep "inet "'  #  half of shell command
part2 = ' | cut -d "k" -f1 | cut -d "n" -f2 | cut -d "t" -f2 | cut -d " " -f2'  #2nd

path2 = part1 + part2
pipe = Popen(path2, stdout=PIPE, shell='True')  
text = pipe.communicate()[0]
myip = str(text.strip())
myip = myip.split("'")
myip = myip[1]



# Set the URL
myurl = urlprefix + myip + port
print(myurl)

path = 'qr "' + myurl + '" > ' + filepath  # Define the full command
pipe = Popen(path, stdout=PIPE, shell='True')  
text = pipe.communicate()[0]
#############


#******** Generate QR Code Begin
# Here's the shell command we're running below:
#/sbin/ifconfig wlan0 | grep "inet " | cut -d "k" -f1 | cut -d "n" -f2 | cut -d "t" -f2 | cut -d " " -f2

#filepath = './qr/qr.png'
part1 = '/sbin/ifconfig wlan0 | grep "inet "'  #  half of shell command
part2 = ' | cut -d "k" -f1 | cut -d "n" -f2 | cut -d "t" -f2 | cut -d " " -f2'  #2nd

#path = 'qr $(' + part1 + part2 + ') > ' + filepath  # Define the full command
#pipe = Popen(path, stdout=PIPE, shell='True')  
#text = pipe.communicate()[0]
#******** Generate QR Code End



# Create image with mode '1' for 1-bit color.
image = Image.new('1', (disp.width, disp.height), "WHITE")

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


# Define main function
def main():
    theqrcode = Image.open(filepath) \
        .resize((size_x, size_y)) \
        .transform(device.size, Image.AFFINE, (1, 0, 0, 0, 1, 0), Image.BILINEAR) \
        .convert("L") \
        .convert(device.mode) \
        #.rotate(180) \
    
    while True:
        # Create blank image for drawing.
        # Create image with mode '1' for 1-bit color.
        image = Image.new('1', (disp.width, disp.height), "WHITE")

        # Get drawing object to draw on image.
        draw = ImageDraw.Draw(theqrcode)

        draw.rectangle(((83, 20), (107, 44)), fill="white")

        #Add stuff here
        draw.rectangle(((63, 0), (127, 64)), fill="black")  # Clear right side
        draw.rectangle(((60, 0), (127, 12)), fill="white")  # Top bar
        draw.rectangle(((0, 56), (128, 64)), fill="white")  # Bottom bar
        draw.text((60,-2), service_name, font = thefont2, fill = 0)
        draw.text((65,12), desc_line1, font = thefont1, fill = 255)
        draw.text((65,27), desc_line2, font = thefont1, fill = 255)
        draw.text((0,57), myurl, font = urlfont, fill = 0)
        #draw.ellipse(shape1, fill =255, outline =0)
        draw.ellipse(shape2, fill =255, outline =0)
        draw.ellipse(shape3, fill =255, outline =0)
        #draw.text((116,13), btn1, font = thefont2, fill = 0)
        draw.text((116,28), btn2, font = thefont2, fill = 0)
        draw.text((117,43), btn3, font = thefont2, fill = 0)

        # Display the image
        device.display(theqrcode.rotate(180))
        #time.sleep(sleep_time)
        
        i = 19
        while i > 0:
            # with canvas(device) as draw:
            if GPIO.input(KEY3_PIN): # button is released
                #draw.polygon([(38, 5), (48, 0), (58, 5)], outline=255, fill=0)  #Up
                print("KEY3 was pressed and released")
                i = i - 1
                draw.rectangle(((85, 43), (112, 55)), fill="black")  # Top bar
                time.sleep(1)
                draw.text((85,43), '(' + str(i) + ')', font = thefont1, fill = 255)
                device.display(theqrcode.rotate(180))
                print(i)
            else:   #button is pressed:
                # Create blank image for drawing.
                print('\n KEY3 was pressed \n')
                i = 0
                #exit()
            if GPIO.input(KEY2_PIN): # button is released
                print('KEY2 Pressed')
                draw.ellipse(shape2, fill =255, outline =0)
                draw.text((116,28), btn2, font = thefont2, fill = 0)
            else:   #button is pressed:
                draw.ellipse(shape2, fill =0, outline =255)
                draw.text((116,28), btn2, font = thefont2, fill = 255)
                draw.text((65,43), btn2, font = thefont1, fill = 255)
                i = i + 20
        exit()


if __name__ == "__main__":
    try:
        device = get_device()
        main()
    except KeyboardInterrupt:
        pass
