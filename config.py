import logging
import os
import sys

from PIL import Image


logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
IMG_PATH     = os.path.join(PROJECT_ROOT, 'img')
INPUT_PATH   = os.path.join(IMG_PATH, 'input')
OUTPUT_PATH  = os.path.join(IMG_PATH, 'output')

WIDTH, HEIGHT = 1500, 500
SCALE = 1/5
IMG_NAME = 'yukidaruma.png'
OUTPUT_NAME = str(1/SCALE)+'-'+IMG_NAME

SMOOTHING = False

if SMOOTHING:
    OUTPUT_NAME = 'smoothing-'+OUTPUT_NAME

img = Image.open(os.path.join(INPUT_PATH, IMG_NAME))
