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

def create_dataset(path):
    """
    Takes a folder of images and resaves the images as processed data

    path (string): the path to the dataset
    """
    path = os.path.abspath(path)
    prepared_path = path+"_prepared"
    
    try:
        os.makedirs(prepared_path + "/emp")
        os.mkdir(prepared_path + "/nada")
    except:
        pass

    count = 0

    for folder in os.listdir(path):
        dirpath = "{}/{}".format(path, folder)
        if os.path.isdir(dirpath):
            for f in os.listdir(path + "/" + folder):
                prepared_dirpath = "{}/{}".format(prepared_path, folder)
                fpath = "{}/{}".format(dirpath, f)
                # ignore hidden files
                if f[0] == '.':
                    continue
                try:
                    image_data = prepare_image(fpath)
                    image_data.save(prepared_dirpath+"/"+f)
                    print("Processing Files: {}".format(count), end="\r")
                    count += 1
                except OSError:
                    os.remove(fpath)

if __name__ == "__main__":
    create_dataset(sys.argv[1])