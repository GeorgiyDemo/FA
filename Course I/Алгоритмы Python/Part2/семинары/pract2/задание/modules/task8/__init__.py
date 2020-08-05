from random import randint

from .equilateral_triangle_class import EquilateralTriangleClass
from .isosceles_triangle_class import IsoscelesTriangleClass
from .tectangular_triangle_class import TectangularTriangleClass
from .triangle_class import TriangleClass


def main():
    try:
        n = int(input("Введите количество треугольников -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    triangle_list = []
    d = {
        0: EquilateralTriangleClass,
        1: IsoscelesTriangleClass,
        2: TectangularTriangleClass,
        3: TriangleClass,
    }
    for _ in range(n):
        r_number = randint(0, 3)
        r_args = [randint(1, 100), randint(1, 100), randint(1, 100)]
        triangle_list.append(d[r_number](*r_args))
    for triangle in triangle_list:
        triangle.info(type(triangle).__name__)
