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


def import_training_data(path):
    """
    Helper function to create numpy arrays for all the necessary training data
    """
    size = (64,64)
    abspath = os.path.abspath(path)

    # preprocess the image data and compile it for training
    images = np.empty((0, size[0]*size[1]), float)
    labels = list()

    count = 0

    # traverse emp folder (all 1s)
    for f in os.listdir(abspath+"/emp"):
        im = Image.open(abspath +"/emp/" + f)

        # get the numeric data from the image
        image_data = np.array(list(im.getdata()))

        # divide all the data by 255
        image_data = np.divide(image_data, 255)

        images = np.append(images, np.array([image_data]), axis=0)
        labels.append(1)

        count += 1
        print("Processing files: {}".format(count), end="\r")
    
    # traverse nada folder (all 0s)
    for f in os.listdir(abspath+"/nada"):
        im = Image.open(abspath +"/nada/" + f)

        # get the numeric data from the image
        image_data = np.array(list(im.getdata()))

        # divide all the data by 255
        image_data = np.divide(image_data, 255)

        images = np.append(images, np.array([image_data]), axis=0)
        labels.append(0)

        count += 1
        print("Processing files: {}".format(count), end="\r")
    
    labels = np.array(labels)

    print("Done")
    return (images, labels)

def save_train_and_test_data():
    (train_images, train_labels) = import_training_data("./tensorflow/training_data_prepared")
    (test_images, test_labels) = import_training_data("./tensorflow/test_data_prepared")

    np.save("training_data.npy", train_images)
    np.save("training_labels.npy", train_labels)
    np.save("test_data.npy", test_images)
    np.save("test_labels.npy", test_labels)

if __name__ == "__main__":
    create_dataset(sys.argv[1])