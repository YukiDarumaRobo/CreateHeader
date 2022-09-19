import logging
import math
import os

from PIL import Image, ImageFilter

import config


logger = logging.getLogger(__name__)

img = config.img
out_path = os.path.join(config.OUTPUT_PATH, config.OUTPUT_NAME)
scale = config.SCALE
img = img.resize((math.floor(scale*img.width), math.floor(scale*img.height)))
n_width  = math.floor(config.WIDTH/img.width)
n_height = math.floor(config.HEIGHT/img.height)
dst = Image.new('RGB', (n_width*img.width, n_height*img.height))
for h in range(n_height):
    for w in range(n_width):
        dst.paste(img, (w*img.width,h*img.height))
if config.SMOOTHING:
    dst = dst.filter(ImageFilter.GaussianBlur(4.0))
dst.save(out_path)
logger.debug({'format': img.format, 
              'size':   img.size, 
              'mode':   img.mode,
              'number': (n_width,n_height)})
