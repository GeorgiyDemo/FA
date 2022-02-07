import math


def area_calculation(a, b, c):
    # Вычисление полупериметра
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


def perimeter_calculation(a, b, angle):
    c = math.sqrt(b ** 2 + a ** 2 - 2 * b * a * math.cos(math.radians(angle)))
    return c, a + b + c
