# Flip and resize image

from PIL import Image

im = Image.open("/usr/local/bin/demo.jpg")
im.rotate(180).resize((640,480)).save("/usr/local/bin/flipped_and_resized.jpg")