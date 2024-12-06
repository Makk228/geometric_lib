import math


def area(a, b, c):
    """Функция принимает 3 аргумента a, b, c (все int) и возвращает
    площадь треугольника по формуле Герона:
    math.sqrt(p * (p - a) * (p - b) * (p - c)) (float).
    """
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def perimeter(a, b, c):
    """Функция принимает 3 аргумента a, b, c (все int) и возвращает
    периметр треугольника по формуле a + b + c (int).
    """
    return a + b + c
