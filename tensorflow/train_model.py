import tensorflow as tf
from tensorflow import keras
import numpy as np
import os

from prepare_image import prepare_image

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

def test_model(test_images, test_labels)
test_loss, test_acc = model.evaluate(test_images, test_labels)

print('Test accuracy:', test_acc)

