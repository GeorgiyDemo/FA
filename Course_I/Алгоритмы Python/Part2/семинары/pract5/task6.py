"""
Задача 6:
Сжать массив, удалив из него все элементы, величина которых находится в интервале [а, b].
Освободившиеся в конце массива элементы заполнить нулями.
"""
from random import randint

import numpy as np


def main():
    try:
        n = int(input("Введите кол-во элементов в массиве -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return
    np_arr = np.array([randint(1, 10) for _ in range(n)])
    print("Исходный массив:", np_arr)

    boolean_flag = True
    while boolean_flag:
        try:
            a = int(input("Введите начало интервала (число a) -> "))
            b = int(input("Введите конец интервала (число b) -> "))
            if a > b:
                b, a = a, b
            boolean_flag = False
        except ValueError:
            print("Некорректный ввод данных!")

    # Ухух, магия numpy
    new_arr = np_arr[(np_arr < a) | (np_arr > b)]
    new_arr = np.pad(new_arr, (0, np_arr.shape[0] - new_arr.shape[0]))
    print(new_arr)


if __name__ == "__main__":
    main()
