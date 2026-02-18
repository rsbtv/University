from random import random

class NeuralNetwork:
    def __init__(self, operation, x_train, y_train, speed=0.3, epoch_count=15):
        self.start_weights = self.init_weights()
        self.weights = self.start_weights.copy()
        self.x_train = x_train

        self.operation         = operation
        self.y_train           = y_train
        self.speed             = speed
        self.epoch_count       = epoch_count
        self.start_error_count = 0
        self.final_error_count = 0
        self.current_epoch     = 0
        self.result            = []

        self.epoch()

        print(f"""Операция: {self.operation}
Стартовые веса: {self.start_weights}
Скорость обучения: {self.speed}
Кол-во ошибок на старте: {self.start_error_count}
Кол-во ошибок в финале: {self.final_error_count}
Эпох потребовалось: {self.epoch_count}
Итоговые веса: {self.weights}
              """)

        for x in self.x_train:
            result = self.predict(x)
            print(f"{x} -> {result}")
            self.result.append(result)
        if self.result == self.y_train:
            print("\nМодель успешно обучилась. Результат соответствует проверочным данным.")
            print("-" * 75)
        else:
            print("\nОбучение модели провалено. Результат не соответствует проверочным данным.")
            print("-"*75)

    def init_weights(self, num_weights=2):
        return [random() for _ in range(num_weights)]

    def predict(self, x):
        summator = x[0] * self.weights[0] + x[1] * self.weights[1]
        return 1 if summator >= 1 else 0

    def train(self):
        for i in range(len(self.x_train)):
            error = self.y_train[i] - self.predict(self.x_train[i])
            if error != 0:
                self.weights[0] = self.weights[0] + error * self.x_train[i][0] * self.speed
                self.weights[1] = self.weights[1] + error * self.x_train[i][1] * self.speed

                if self.current_epoch == 0:
                    self.start_error_count += 1
                elif self.current_epoch == self.epoch_count-1:
                    self.final_error_count += 1

    def epoch(self):
        for i in range(self.epoch_count):
            self.current_epoch = i
            self.train()

class InverseNeuralNetwork(NeuralNetwork):
    def __init__(self, operation, x_train, y_train, speed=0.3, epoch_count=15):
        super().__init__(operation, x_train, y_train, speed, epoch_count)

    def predict(self, x):
        summator = x[0] * self.weights[0] + x[1] * self.weights[1]
        return 1 if summator >= 0 else -1

class BiasNeuralNetwork(NeuralNetwork):
    def __init__(self, operation, x_train, y_train, speed=0.3, epoch_count=15):
        super().__init__(operation, x_train, y_train, speed, epoch_count)

    def init_weights(self, num_weights=3):
        return [random() for _ in range(num_weights)]

    def predict(self, x):
        summator = x[0] * self.weights[0] + x[1] * self.weights[1] + x[2] * self.weights[2]
        return 1 if summator >= 0 else -1

    def train(self):
        for i in range(len(self.x_train)):
            error = self.y_train[i] - self.predict(self.x_train[i])
            if error != 0:
                self.weights[0] = self.weights[0] + error * self.x_train[i][0] * self.speed
                self.weights[1] = self.weights[1] + error * self.x_train[i][1] * self.speed
                self.weights[2] = self.weights[2] + error * self.x_train[i][2] * self.speed

                if self.current_epoch == 0:
                    self.start_error_count += 1
                elif self.current_epoch == self.epoch_count-1:
                    self.final_error_count += 1

def main():
    x_train         = [[1, 1],    [1, 0],     [0, 1],     [0, 0]]
    inverse_x_train = [[1, 1],    [1, -1],    [-1, 1],    [-1, -1]]
    bias_x_train    = [[1, 1, 1], [1, -1, 1], [-1, 1, 1], [-1, -1, 1]]

    conjunction   = NeuralNetwork("Конъюнкция", x_train,[1, 0, 0, 0])
    disjunction   = NeuralNetwork("Дизъюнкция", x_train,[1, 1, 1, 0])
    not_x1_and_x2 = NeuralNetwork("Конъюнкция отрицания х1 и х2", x_train,[0, 0, 1, 0])
    x1_and_not_x2 = NeuralNetwork("Конъюнкция х1 и отрицания х2", x_train,[0, 1, 0, 0])
    inverse_conjunction = InverseNeuralNetwork("Конъюнкция", inverse_x_train, [1, -1, -1, -1])
    bias_conjunction = BiasNeuralNetwork("Конъюнкция", bias_x_train, [1, -1, -1, -1])

def task_5():
    x_train = [[1, 1], [1, 0], [0, 1], [0, 0]]
    x1_and_not_x2 = NeuralNetwork("Конъюнкция х1 и отрицания х2", x_train,[0, 1, 0, 0])
    not_x1_and_x2 = NeuralNetwork("Конъюнкция отрицания х1 и х2", x_train,[0, 0, 1, 0])

    # Выходной нейрон XOR = OR(A, B)
    outputs = []
    for i in range(len(x_train)):
        a = x1_and_not_x2.predict(x_train[i])
        b = not_x1_and_x2.predict(x_train[i])
        outputs.append([a, b])

    print(outputs)
    xor = NeuralNetwork("Исключающее ИЛИ", outputs, [0, 1, 1, 0])

    for x in x_train:
            a = x1_and_not_x2.predict(x)
            b = not_x1_and_x2.predict(x)
            y = xor.predict([a, b])
            print(f"{x} -> {y}")

task_5()