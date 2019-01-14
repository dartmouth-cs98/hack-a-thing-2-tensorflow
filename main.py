import numpy as np
import tensorflow as tf
from tensorflow.keras import layers

model = tf.keras.Sequential([
  layers.Dense(64, activation='relu'),
  layers.Dense(64, activation='relu'),
  layers.Dense(10, activation='softmax')
])

model.compile(optimizer=tf.train.AdamOptimizer(0.001),
  loss='categorical_crossentropy',
  metrics=['accuracy'])

data = np.random.random((1000, 32))
labels = np.random.random((1000, 10))

model.fit(data, labels, epochs=10, batch_size=32)

dataset = tf.data.Dataset.from_tensor_slices((data, labels))
dataset = dataset.batch(32)
dataset = dataset.repeat()

model.fit(dataset, epochs=10, steps_per_epoch=20)

model.evaluate(data, labels, batch_size=32)
model.evaluate(dataset, steps=30)

result = model.predict(data, batch_size=32)
print(result.shape)