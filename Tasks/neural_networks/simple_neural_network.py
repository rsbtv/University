import random

def init_weights(num_weights=2):
    return [random.random() for _ in range(num_weights)]

def predict(x, w):
    summator = x[0] * w[0] + x[1] * w[1]
    return 1 if summator >= 1 else 0

def train(x_train, y_train, w, speed):
    for i in range(len(x_train)):
        error = y_train[i] - predict(x_train[i], w)
        if error != 0:
            w[0] = w[0] + error * x_train[i][0] * speed
            print(w)
            w[1] = w[1] + error * x_train[i][1] * speed
            print(w)
        else:
            print("Веса не изменились.")

def epoch(count, func_train, x_train, y_train, w, speed):
    print("\tПараметры весов:")
    for i in range(count):
        print(f"\t\tЭпоха №{i}\t")
        func_train(x_train, y_train, w, speed)



# Данные для обучения
x_train = [[1, 1], [1, 0], [0, 1], [0, 0]]
datasets = {
    "Конъюнкция":                   [[1, 0, 0, 0],[]],
    "Дизъюнкция":                   [[1, 1, 1, 0],[]],
    "Конъюнкция отрицания х1 и х2": [[0, 0, 1, 0],[]],
    "Конъюнкция х1 и отрицания х2": [[0, 1, 0, 0],[]],
    # "Исключающее ИЛИ":              [[0, 1, 1, 0],[]],
}

def main():
    speed = 0.3  # Скорость обучения

    for key, value in datasets.items():
        w = init_weights()  # Инициализация весов
        print("Стартовые веса: ", w)

        print("\n",key)
        epoch(5, train, x_train, value[0], w, speed)
    # Запуск обучения
    # epoch(5, train, x_train, y_train, w, speed)
        print("\nКонечные веса: ", w)
        value[1] = w
        # Вывод результатов после обучения
        print("A B F")
        for x in x_train:
            print(f"{x[0]} {x[1]}", predict(x, w))

    for key, value in datasets.items():
        print(key, value[1])
if __name__ == '__main__':
    main()