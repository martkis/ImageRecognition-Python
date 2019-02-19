from PIL import ImageColor, Image, ImageFile
import numpy
import cv2
import glob

from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

path = "C:\\Users\\makis\\Desktop\\pic\\stop\\**"
out_path = "C:\\Users\\makis\\Desktop\\pic\\stop\\*"
name = "stop"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def resize_data(path1):
    images = [Image.open(file) for file in glob.glob(path1)]
    # print(len(images))
    i = 0
    for pic in images:
        i = i + 1
        image = pic.resize((int(200), int(200)))
        image.save(out_path + name + str(i) + '.jpg')


def main():
    resize_data(path)


if __name__ == '__main__':
    main()
