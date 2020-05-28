#!/usr/bin/env python3

import time
import colorsys
import os
import sys
import ST7735
try:
    # Transitional fix for breaking change in LTR559
    from ltr559 import LTR559
    ltr559 = LTR559()
except ImportError:
    import ltr559

from bme280 import BME280
from enviroplus import gas
from subprocess import PIPE, Popen
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from fonts.ttf import RobotoMedium as UserFont
import logging

print("Running Enviro+ Weather with Adafruit.io feed!\nCurrent:Temperature, Humidity, Light & Pressure\nComing:Reduced, Oxidised, Nh3")

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'X'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username).
ADAFRUIT_IO_USERNAME = 'X'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Set up Adafruit IO Feeds.
temperature_feed = aio.feeds('temperature')
pressure_feed = aio.feeds('pressure')
humidity_feed = aio.feeds('humidity')
light_feed = aio.feeds('light')

# BME280 temperature/pressure/humidity sensor
bme280 = BME280()

# Create ST7735 LCD display class
st7735 = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

# Initialize display
st7735.begin()

WIDTH = st7735.width
HEIGHT = st7735.height

# Set up canvas and font
img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)
font_size = 20
font = ImageFont.truetype(UserFont, font_size)
text_colour = (0, 255, 0)
back_colour = (0, 0, 0)

message = "Dashboard URL"
size_x, size_y = draw.textsize(message, font)

# Text position
x = (WIDTH - size_x) / 2
y = (HEIGHT / 2) - (size_y / 2)

# Text box
draw.rectangle((0, 0, 160, 80), back_colour)
draw.text((x, y), message, font=font, fill=text_colour)
st7735.display(img)

# Data send loop
try:
    while True:
        # Test Data
        temperature_reading = bme280.get_temperature()
        pressure_reading = bme280.get_pressure()
        humidity_reading = bme280.get_humidity()
        light_reading = ltr559.get_lux()
        
        # Temp Data feed send
        aio.send_data(temperature_feed.key, temperature_reading-11) # 11 degree offset, adjust as applicable
        aio.send_data(pressure_feed.key, pressure_reading) # in hPa 950-1050 base range, 1013 normal sea level
        aio.send_data(humidity_feed.key, humidity_reading) # as a percentage 0-100
        aio.send_data(light_feed.key, light_reading) # in lux units
        
        # Delay between data sends to adafruit io in seconds
        time.sleep(60)
        
# Exit cleanly
except KeyboardInterrupt:
    sys.exit(0)
