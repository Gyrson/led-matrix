#!/usr/bin/env python3
import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv) < 2:
    image_file = "/root/rpi-rgb-led-matrix/img/Chars.png"
else:
    image_file = sys.argv[1]

image = Image.open(image_file)

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.chain_length = 1
options.gpio_slowdown = 2
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

# Make image fit our screen.
image.thumbnail((matrix.width, matrix.height), Image.ANTIALIAS)

#matrix.SetImage(image.convert('RGB'))
time_image = Image.new("RGB", (matrix.width, matrix.height), (0, 0, 0))
draw = ImageDraw.Draw(time_image)
font = ImageFont.load_default()

try:
    print("Press CTRL-C to stop.")
    while True:
        # Create a new image buffer
        buffer = Image.new("RGB", (matrix.width, matrix.height), (0, 0, 0))
        buffer_draw = ImageDraw.Draw(buffer)

        # Draw the image on the buffer
        buffer.paste(image, (0, 0))

        # Draw the time on the buffer
        current_time = time.strftime("%H:%M:%S")
        buffer_draw.text((2, 2), current_time, font=font, fill=(255, 255, 255))

        # Swap the buffer with the display
        matrix.SetImage(buffer.convert("RGB"))

        time.sleep(1)
except KeyboardInterrupt:
    sys.exit(0)
