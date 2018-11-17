# -*-coding:utf-8-*-

import os
from PIL import Image

tmp_dir = os.path.join(os.path.curdir, 'tmp')


def crop_image(file_path, label):
    image = Image.open(file_path)
    size = image.size
    # print("Size: {}".format(size))

    # make sure temp directory exists
    check_temp_dir()

    digit_width = 10
    digit_height = 16
    digit_box = [
        (1, 1),
        (11, 1),
        (21, 1),
        (31, 1),
    ]
    # Crop to 4 digits
    digits = [image.crop(
        (x, y, x + digit_width, y + digit_height)
    ) for (x, y) in digit_box]

    paths = [generate_temp_file_path("{}-digit_{}.jpg".format(label, i)) for i in range(len(digits))]
    for i in range(len(digits)):
        digits[i].save(paths[i])
    return paths


def generate_temp_file_path(file_name):
    return os.path.join(tmp_dir, file_name)


def check_temp_dir():
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)
    return tmp_dir
