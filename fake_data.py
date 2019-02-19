from scipy import ndimage, misc
import numpy as np
import os
from os.path import isfile, join
import cv2
from PIL import Image
import cv2 as cv

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def main():
    # path to folder with pictures
    outpath = 'C:\\Users\makis\Desktop\pic\*'
    path = "C:\\Users\makis\Desktop\pic\*"
    i = 0  # counter

    for image_path in os.listdir(path):
        input_path = os.path.join(outpath, image_path)
        image_to_gray = ndimage.imread(input_path)

        i = i + 1

        gray = cv2.cvtColor(image_to_gray, cv2.COLOR_BGR2GRAY)
        input_path = os.path.join(outpath, 'gray_' + str(i) + image_path)
        cv2.imwrite(input_path, gray)

    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(outpath, image_path)
        image_to_rotate = ndimage.imread(input_path)

        for x in range(-11, 9, 4):
            rotated = ndimage.rotate(image_to_rotate, x)
            fullpath = os.path.join(outpath, 'rotated_' + str(x) + image_path)
            misc.imsave(fullpath, rotated)


if __name__ == '__main__':
    main()
