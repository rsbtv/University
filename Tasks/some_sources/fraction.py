from math import gcd, lcm


class Fraction():
    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю!")
        else:
            self.numerator   = int(numerator)
            self.denominator = int(denominator)
            self.shorten_fraction()

    def shorten_fraction(self):
        fraction_gcd = gcd(int(self.numerator), int(self.denominator))
        self.numerator /=  fraction_gcd
        self.denominator /= fraction_gcd
        # print(self.__repr__())

    def __add__(self, other):
        fraction_lcm = lcm(int(self.denominator), int(other.denominator))
        numerator = self.numerator * (fraction_lcm  / self.denominator)
        other_numerator = other.numerator * (fraction_lcm / other.denominator)
        return Fraction(numerator + other_numerator, fraction_lcm)

    def __sub__(self, other):
        fraction_lcm = lcm(int(self.denominator), int(other.denominator))
        numerator = self.numerator * (fraction_lcm / self.denominator)
        other_numerator = other.numerator * (fraction_lcm / other.denominator)
        return Fraction(numerator - other_numerator, fraction_lcm)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        try:
            return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        except ZeroDivisionError:
            print('На ноль делить нельзя!')

    def __eq__(self, other):
        other.shorten_fraction()
        if self.numerator == other.numerator and self.denominator == other.denominator:
            return True
        else:
            return False

    def __ne__(self, other):
        return not(self.__eq__(other))

    def __lt__(self, other):
        other.shorten_fraction()
        if self.numerator / self.denominator < other.numerator / other.denominator:
            return True
        else:
            return False

    def __le__(self, other):
        if self.numerator / self.denominator <= other.numerator / other.denominator:
            return True
        else:
            return False

    def __gt__(self, other):
        return not(self.__le__(other))

    def __ge__(self, other):
        return not(self.__lt__(other))

    def __float__(self):
        return self.numerator / self.denominator

    def reciprocal(self):
        return Fraction(self.denominator, self.numerator)

    def __str__(self):
        if self.denominator == 1:
            return f'{int(self.numerator)}'
        else:
            return f'{int(self.numerator)}/{int(self.denominator)}'

    def __repr__(self):
        return f'Fraction({int(self.numerator)}, {int(self.denominator)})'

    def from_float(num):
        numerator = decimal_part(num)
        denominator = 10**decimal_length(num)
        fraction_gcd = gcd(int(numerator), int(denominator))
        numerator /= fraction_gcd
        denominator /= fraction_gcd
        return Fraction(numerator, denominator)

def decimal_length(num: float):
    if '.' in str(num):
        return len(str(num).split('.')[1])
    else:
        return None

def decimal_part(num):
    if '.' in str(num):
        return int(str(num).split('.')[1])

# Создание дробей
f1 = Fraction(3, 4)
f2 = Fraction(5, 6)

# Сложение дробей
f3 = f1 + f2
print(f3)  # Ожидаемый вывод: 19/12

# Вычитание дробей
f4 = f1 - f2
print(f4)  # Ожидаемый вывод: -1/12

# Умножение дробей
f5 = f1 * f2
print(f5)  # Ожидаемый вывод: 5/8

# Деление дробей
f6 = f1 / f2
print(f6)  # Ожидаемый вывод: 9/10

# Проверка равенства
print(f1 == Fraction(6, 8))   # Ожидаемый вывод: True

# Сравнение дробей
print(f1 > f2)    # Ожидаемый вывод: False
print(f1 < f2)    # Ожидаемый вывод: True

# Преобразование к float
print(float(f1))  # Ожидаемый вывод: 0.75

# Обратная дробь
f7 = f1.reciprocal()
print(f7)         # Ожидаемый вывод: 4/3

# Создание дроби из float
f8 = Fraction.from_float(0.75)
print(f8)         # Ожидаемый вывод: 3/4

# Проверка обработки исключений
try:
    f_invalid = Fraction(5, 0)
except ValueError as e:
    print(e)  # Ожидаемый вывод: Знаменатель не может быть нулем

# Строковое и официальное представление
print(str(f1))    # Ожидаемый вывод: 3/4
print(repr(f1))   # Ожидаемый вывод: Fraction(3, 4)