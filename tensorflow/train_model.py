import tensorflow as tf
from tensorflow import keras
from PIL import Image
import numpy as np
import os

def import_training_data(path):
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

def train_model(train_images, train_labels):
    # build the model architecture
    model = keras.Sequential([
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(2, activation='sigmoid')
    ])

    # compile the model
    model.compile(optimizer=tf.train.AdamOptimizer(),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # train the model
    model.fit(train_images, train_labels, epochs=5)

    return model

def test_model(model, test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print('Test accuracy:', test_acc)

if __name__ == "__main__":
    # ######### used to train and save the labels ###########
    # (train_images, train_labels) = import_training_data("./tensorflow/training_data_prepared")
    # (test_images, test_labels) = import_training_data("./tensorflow/test_data_prepared")

    # np.save("training_data.npy", train_images)
    # np.save("training_labels.npy", train_labels)
    # np.save("test_data.npy", test_images)
    # np.save("test_labels.npy", test_labels)

    # #######################################################

    train_data = np.load("training_data.npy")
    train_labels = np.load("training_labels.npy")
    test_data = np.load("test_data.npy")
    test_labels = np.load("test_labels.npy")

    model = train_model(train_data, train_labels)
    test_model(model, test_data, test_labels)

