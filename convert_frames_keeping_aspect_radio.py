import os
from pil import Image

PRINTS_DICT = './prints'
RESIZED_PRINTS_DICT = './resized_prints'

for folder in os.listdir(PRINTS_DICT):
    for image in os.listdir(folder):

        os.mkdir(os.path.join(RESIZED_PRINTS_DICT, folder))