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

    for f in os.listdir(abspath):
        im = Image.open(abspath +"/" + f)

        # get the numeric data from the image
        image_data = np.array(list(im.getdata()))

        # divide all the data by 255
        image_data = np.divide(image_data, 255)

        images = np.append(images, np.array([image_data]), axis=0)


    # for as many train_images as there are, set all of their labels to be 1
    labels = np.ones(images.shape[0])
    
    return (images, labels)

def train_model(train_images, train_labels):
    # build the model architecture
    model = keras.Sequential([
        keras.layers.Dense(128, activation=tf.nn.relu),
        keras.layers.Dense(10, activation=tf.nn.sigmoid)
    ])

    # compile the model
    model.compile(optimizer=tf.train.AdamOptimizer(),
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

    # train the model
    model.fit(train_images, train_labels, epochs=5)

    return model

def test_model(test_images, test_labels):
    test_loss, test_acc = model.evaluate(test_images, test_labels)

    print('Test accuracy:', test_acc)

if __name__ == "__main__":
    (images, labels) = import_training_data("./tensorflow/training_data_prepared")

    print(images)
    print(labels)
