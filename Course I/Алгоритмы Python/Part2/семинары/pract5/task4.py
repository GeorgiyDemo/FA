"""
Задача 4:
Найти в массиве те элементы, значение которых меньше среднего арифметического, взятого от
всех элементов массива.
"""
from random import randint

import numpy as np


def main():
    try:
        n = int(input("Введите кол-во строк в матрице -> "))
        m = int(input("Введите кол-во столбцов в матрице -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return

    # Генерация данных
    matrix = np.matrix([[randint(-100, 100) for x in range(m)] for y in range(n)])
    print("Сгенерированная матрица:\n", matrix)
    mean = np.mean(matrix)
    print("Среднее арифметическое: {}".format(mean))
    for e in np.nditer(matrix):
        if e < mean:
            print("Элемент {} меньше сред. арифметического".format(e))


if __name__ == "__main__":
    main()
