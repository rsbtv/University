from tensorflow.keras.models import Sequential
from keras.layers import Conv2D       # Свёрточный слой
from keras.layers import MaxPooling2D # Пулинг, берет максимум из блока пикселей
from keras.layers import Flatten      # Выравнивает 2D-изображение в 1D-вектор

from keras.layers import Dense        # Полносвязный слой, каждый новый связан...
                                      # с предыдущим, должен быть после Flatten...
                                      # (т.к. обрабатывает 1D-вектор)
FILTERS_COUNT = 64
FILTERS_SHAPE = (3,3)
PADDING = 'same' # Рамка из нулей, чтобы выход был 28×28, а не 26×26
model = Sequential([
    Conv2D(FILTERS_COUNT,
           FILTERS_SHAPE,
           padding=PADDING,
           activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2), strides=2),
    Conv2D(32, (3,3), padding='same', activation='relu'),
    MaxPooling2D((2, 2), strides=2),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10,  activation='softmax')
])