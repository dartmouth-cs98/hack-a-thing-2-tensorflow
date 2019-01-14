from PIL import Image
import numpy as np

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

    # get the numeric data from the image
    data = np.array(list(out.getdata()))

    # divide all the data by 255
    return np.divide(data, 255)