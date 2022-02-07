from random import randint

from .ball_class import BallClass
from .parallelepiped_class import ParallelepipedClass
from .pyramid_class import PyramidClass


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
