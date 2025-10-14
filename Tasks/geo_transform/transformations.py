from math import sqrt, atan2, sin, cos

def cartesian_to_spherical(x: float, y: float, z: float) -> tuple[float, float, float]:
    """
    Функция преобразовывает декартовы координаты в сферические
    :param x: float
    :param y: float
    :param z: float
    :return: tuple[float, float, float]
    """
    radius = sqrt(x**2 + y**2 + z**2)
    azimuths_angle = 2 * atan2(x, y + sqrt(x ** 2 + y ** 2))
    polar_angle = atan2(sqrt(x**2 + y**2), z)
    return radius, azimuths_angle, polar_angle

def spherical_to_cartesian(radius: float, azimuth_angle: float, polar_angle: float) -> tuple[float, float, float]:
    """
    Функция преобразовывает сферические координаты в декартовы
    :param radius: float
    :param azimuth_angle: float
    :param polar_angle: float
    :return: tuple[float, float, float]
    """
    x = radius * sin(polar_angle) * cos(azimuth_angle)
    y = radius * sin(polar_angle) * sin(azimuth_angle)
    z = radius * cos(polar_angle)
    return x, y, z
