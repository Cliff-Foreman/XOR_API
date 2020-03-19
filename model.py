from keras.models import Sequential
from keras.layers.core import Dense
import numpy as np
from keras.models import load_model


xs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
ys = np.array([[0], [1], [1], [0]])
'''

model = Sequential()
model.add(Dense(5, input_dim=(2), activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="sgd")

for i in range(100):
    model.fit(xs, ys, epochs=100)

model.save("model.h5")
'''

model = load_model("model.h5")

model.predict(xs)
