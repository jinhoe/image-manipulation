# Rotate, resize, convert image

#!/usr/bin/env python3

import os

from PIL import Image

images_dir = '/usr/local/bin/images/'

for image_name in os.listdir(images_dir):
    image_path = images_dir + image_name
    im = Image.open(image_path)
    new_path = '/usr/local/bin/opt/icons/' + image_name.split('.')[0]
    im.rotate(-90).convert('RGB').resize((128, 128)).save(new_path, 'jpeg')
    im.close()
