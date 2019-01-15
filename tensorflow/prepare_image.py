from PIL import Image
import numpy as np
import os
import sys

def prepare_image(img, size=(64,64)):
    """
    Prepares an image for processing by translating it to size pixels
    and converting it to greyscale

    e.g. if size is (64,64), the default, the output image will be 64x64 pixels

    returns the image data as a 1-D array
    """
    im = Image.open(img)

    out = im.convert("L").resize(size)
    out.thumbnail(size, Image.ANTIALIAS)

    return out

def create_dataset(path, size=(64,64)):
    """
    Takes a folder of images and resaves the images as processed data

    path (string): the path to the dataset
    size (tuple of ints): the 2D size of the intended image
    """
    path = os.path.abspath(path)
    prepared_path = path+"_prepared"
    
    try:
        os.mkdir(prepared_path)
    except:
        pass

    for f in os.listdir(path):
        fpath = "{}/{}".format(path, f)
        # ignore hidden files
        if f[0] == '.':
            continue
        try:
            image_data = prepare_image(fpath)
            image_data.save(prepared_path+"/"+f)
        except OSError:
            os.remove(fpath)

if __name__ == "__main__":
    create_dataset(sys.argv[1])