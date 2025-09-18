from math import pi


def deg_to_rad(degrees: float) -> float:
    """
    Функция преобразовывает угол в градусах в угол в радианах
    :param degrees:
    :return: float
    """
    return degrees * pi / 180


def rad_to_deg(radians: float) -> float:
    """
    Функция преобразовывает угол в радианах в угол в градусах
    :param radians:
    :return: float
    """
    return radians * 180 / pi
