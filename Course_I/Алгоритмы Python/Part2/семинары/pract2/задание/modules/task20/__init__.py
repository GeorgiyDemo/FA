from random import randint

from .arithmetic_class import ArithmeticClass
from .geometric_class import GeometricClass


def main():
    try:
        n = int(input("Введите кол-во прогрессий для генерации -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {
        1: ArithmeticClass,
        2: GeometricClass,
    }
    progression_list = []
    for _ in range(n):
        d_args = {
            1: [randint(-1000, 1000), randint(-1000, 1000), randint(1, 10)],
            2: [randint(-1000, 1000), randint(-1000, 1000)],
        }
        r_number = randint(1, 2)
        progression_list.append(d[r_number](*d_args[r_number]))
    for e in progression_list:
        # print(e.get_sum())
        print(e.info() + "\n")
