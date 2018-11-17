# -*-coding:utf-8-*-

from PIL import Image


def feature_extract(file_path):
    image = Image.open(file_path)
    size = image.size
    px = image.load()

    features = []
    for x in range(size[0]):
        for y in range(size[1]):
            features.append(binarize(px[x, y]))

    return features


"""
:param rgb: pixel in RGB format
:returns: 0 or 1
"""
def binarize(rgb):
    threshold = 127
    r, g, b = rgb
    if r >= threshold or g >= threshold or b >= threshold:
        return 1
    else:
        return 0
