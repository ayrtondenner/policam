import os
from PIL import Image

PRINTS_DICT = './prints'
RESIZED_PRINTS_DICT = './resized_prints'

RESIZE_WIDTH = 500
RESIZE_HEIGHT = 281

for folder in os.listdir(PRINTS_DICT):

    original_path = os.path.join(PRINTS_DICT, folder)
    resized_path = os.path.join(RESIZED_PRINTS_DICT, folder)

    if os.path.exists(resized_path):
        for frame in os.listdir(resized_path):
            os.remove(os.path.join(resized_path, frame))
        os.rmdir(resized_path)

    os.makedirs(resized_path)

    for image_path in os.listdir(original_path):
        image = Image.open(os.path.join(original_path, image_path))
        image.thumbnail((RESIZE_WIDTH, RESIZE_HEIGHT), Image.ANTIALIAS)
        image.save(os.path.join(resized_path, image_path))