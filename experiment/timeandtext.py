#!/usr/bin/env python3

import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions
from PIL import Image, ImageDraw, ImageFont

# Set up the RGB matrix options
options = RGBMatrixOptions()
options.hardware_mapping = 'adafruit-hat'
options.rows = 32
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.gpio_slowdown = 3

matrix = RGBMatrix(options=options)

# Set up fonts
font_time = ImageFont.load_default()
font_scroll = ImageFont.load_default()

# Set up initial variables
scroll_text = "This is a scrolling text. "
scroll_text += "You can customize it as per your needs. "
scroll_text += "This example loops indefinitely."

scroll_speed = 1  # Adjust scroll speed as needed

try:
    while True:
        # Clear the matrix at the beginning of each iteration
        matrix.Clear()

        # Create a new image buffer
        buffer = Image.new("RGB", (matrix.width, matrix.height), (0, 0, 0))
        draw = ImageDraw.Draw(buffer)

        # Get current time
        current_time = time.strftime("%H:%M:%S")

        # Draw time on the upper half
        draw.text((2, 2), current_time, font=font_time, fill=(255, 255, 255))

        # Scroll text on the lower half
        text_width, text_height = draw.textsize(scroll_text, font=font_scroll)
        x_offset = matrix.width

        # Create a new image buffer for scrolling text
        text_buffer = Image.new("RGB", (matrix.width, matrix.height), (0, 0, 0))
        text_draw = ImageDraw.Draw(text_buffer)

        while x_offset > -text_width:
            # Clear the scrolling buffer at the beginning of each iteration
            text_buffer.paste((0, 0, 0), (0, 0, matrix.width, matrix.height))

            # Draw scrolling text on the scrolling buffer
            text_draw.text((x_offset, matrix.height // 2), scroll_text, font=font_scroll, fill=(255, 255, 255))

            # Paste the scrolling buffer onto the main buffer
            buffer.paste(text_buffer, (0, 0))

            # Draw time on the upper half
            draw.text((2, 2), current_time, font=font_time, fill=(255, 255, 255))

            # Update the display
            matrix.SetImage(buffer.convert("RGB"))
            time.sleep(0.05)  # Adjust sleep duration for scroll speed

            x_offset -= scroll_speed

except KeyboardInterrupt:
    matrix.Clear()
