"""Прочие методы для работы"""
import math

# Функции-помощь для преобразований
def angle_to_vector(ang):
    """Преобразование угла в вектор"""
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    """Дистанция"""
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
