from tensorflow import keras
import tensorflow as tf
import numpy as np
import prepare_dataset

# Much of this code adapted from https://www.tensorflow.org/tutorials/keras/basic_classification

class NN(object):
    def __init__(self):
        self.model = None

    def train_model(self, train_images, train_labels):
        # build the model architecture
        self.model = keras.Sequential([
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(2, activation='softmax')
        ])

        # compile the model
        self.model.compile(optimizer=tf.train.AdamOptimizer(),
                    loss='sparse_categorical_crossentropy',
                    metrics=['accuracy'])

        # train the model
        self.model.fit(train_images, train_labels, epochs=5)

    def test_model(self, test_images, test_labels):
        test_loss, test_acc = self.model.evaluate(test_images, test_labels)

        print('Test accuracy:', test_acc)

    def get_prediction(self, file):
        im = prepare_dataset.prepare_image(file)

        # get the numeric data from the image
        image_data = np.array(list(im.getdata()))

        image_data = (np.expand_dims(image_data,0))

        prediction = self.model.predict(image_data)
        return np.argmax(prediction)

def configure_nn():
    train_data = np.load("training_data.npy")
    train_labels = np.load("training_labels.npy")
    test_data = np.load("test_data.npy")
    test_labels = np.load("test_labels.npy")

    print(train_labels)
    print(test_labels)

    nn = NN()
    nn.train_model(train_data, train_labels)
    nn.test_model(test_data, test_labels)

    return nn