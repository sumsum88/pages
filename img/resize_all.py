import os
import glob
from PIL import Image


def convert(in_path, out_path, size=(1400, 2000)):
    files = glob.glob(os.path.join(in_path, '*'))
    for file in files:
        img = Image.open(file)
        img = img.resize(size)
        img.save(file.replace(in_path, out_path))


if __name__ == '__main__':
    convert('./services', './services_resized')