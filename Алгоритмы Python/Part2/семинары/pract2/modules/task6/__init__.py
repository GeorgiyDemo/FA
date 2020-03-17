from math import pi, sqrt
from random import randint
from triangle_class import TriangleClass
from rectangle_class import RectangleClass
from circle_class import CircleClass
def main():
    try:
        n = int(input("Введите количество фигур -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {0: RectangleClass,1: CircleClass,2: TriangleClass,}
    figures_list = []
    for _ in range(n):
        d_args = {0: [randint(1, 100), randint(1, 100)], 1: [randint(1, 100)], 2: [randint(1, 100), randint(1, 100), randint(1, 100)]}
        r_number = randint(0, 2)
        figures_list.append(d[r_number](*d_args[r_number]))
    for figure in figures_list: figure.info(type(figure).__name__)