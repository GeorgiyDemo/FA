"""
Задача  12. Создайте класс ТЕЛО с методами вычисления площади поверхности и объема,
а также методом, выводящим информацию о фигуре на экран.

Создайте дочерние классы ПАРАЛЛЕЛЕПИПЕД, ШАР, ПИРАМИДА со своими методами вычисления площади и объема.

Создайте список п фигур и выведите полную информацию о фигурах на экран.
"""

from abc import ABCMeta, abstractmethod
from math import pi
from random import randint


class BodyClass:
    """
    Абстрактный класс тела
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def surface_area_calculation(self):
        self.surface_area = 0

    @abstractmethod
    def volume_calculation(self):
        self.volume = 0

    def info(self, lclass=None):
        a = self.surface_area
        v = self.volume

        if type(self.surface_area) == float or type(self.volume) == float:
            a = str(round(self.surface_area, 2))
            v = str(round(self.volume, 2))
        print("\nВызов от {}\nПлощадь поверхности фигуры: {}\nОбъем фигуры: {}".format(lclass, a, v))


class ParallelepipedClass(BodyClass):
    """
    Класс параллелепипед
    """

    def __init__(self, a, b, c):
        # a,b,c - ребра параллелепипеда
        self.a = a
        self.b = b
        self.c = c
        self.volume_calculation()
        self.surface_area_calculation()

    def surface_area_calculation(self):
        # S = 2(ab + bc + ac)
        a = self.a
        b = self.b
        c = self.c
        self.surface_area = 2 * (a * b + b * c + a * c)

    def volume_calculation(self):
        self.volume = self.a * self.b * self.c


class BallClass(BodyClass):
    """
    Класс шар
    """

    def __init__(self, r):
        self.r = r
        self.volume_calculation()
        self.surface_area_calculation()

    def surface_area_calculation(self):
        self.surface_area = 4 * pi * pow(self.r, 2)

    def volume_calculation(self):
        self.volume = (4 / 3) * pi * pow(self.r, 3)


class PyramidClass(BodyClass):
    """
    Класс пирамида
    """

    def __init__(self, S_main, S_back, h):
        # S_main - площадь основания пирамиды
        # S_back - площадь боковой поверхности
        # h - высота пирамиды
        self.S_main = S_main
        self.S_back = S_back
        self.h = h

        self.volume_calculation()
        self.surface_area_calculation()

    def surface_area_calculation(self):
        self.surface_area = self.S_main + 4 * self.S_back

    def volume_calculation(self):
        self.volume = (1 / 3) * self.S_main * self.h


def main():
    try:
        n = int(input("Введите количество фигур -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: ParallelepipedClass,
        2: BallClass,
        3: PyramidClass,
    }

    figures_list = []

    for _ in range(n):
        d_args = {
            1: [randint(1, 1000), randint(1, 1000), randint(1, 1000)],
            2: [randint(1, 1000)],
            3: [randint(1, 1000), randint(1, 1000), randint(1, 1000)],
        }

        r_number = randint(1, 3)
        figures_list.append(d[r_number](*d_args[r_number]))

    for figure in figures_list:
        figure.info(type(figure).__name__)


if __name__ == "__main__":
    main()
