import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

from prepare_image import prepare_image

def compile_data(path, size=(64,64)):
    # preprocess the image data and compile it for training
    train_images = np.empty((0, size[0]*size[1]), float)

    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            # ignore hidden files
            if f[0] == '.':
                continue
            try:
                image_data = prepare_image("{}/{}".format(dirpath, f))
                train_images = np.append(train_images, np.array([image_data]), axis=0)
            except OSError:
                # do nothing
                continue

    # for as many train_images as there are, set all of their labels to be 1
    train_labels = np.ones(train_images.shape[0])

    return (train_images, train_labels)


def train_model(train_images, train_labels)
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

def test_model(test_images, test_labels)
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

