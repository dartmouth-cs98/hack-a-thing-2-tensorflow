from PIL import Image
import numpy as np
import os

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

    # # get the numeric data from the image
    # data = np.array(list(out.getdata()))

    # # divide all the data by 255
    # return np.divide(data, 255)

def create_dataset(path, size=(64,64)):
    """
    Takes a folder of images and resaves the images as processed data

    path (string): the path to the dataset
    size (tuple of ints): the 2D size of the intended image
    """
    # preprocess the image data and compile it for training
    train_images = np.empty((0, size[0]*size[1]), float)

    for dirpath, _, filenames in os.walk(path):
        print(filenames)
        for f in filenames:
            path = "{}/{}".format(dirpath, f)
            # ignore hidden files
            if f[0] == '.':
                continue
            try:
                image_data = prepare_image(path)
                image_data.save(f)
                # train_images = np.append(train_images, np.array([image_data]), axis=0)
            except OSError:
                os.remove(path)


# for as many train_images as there are, set all of their labels to be 1
# train_labels = np.ones(train_images.shape[0])

# return (train_images, train_labels)