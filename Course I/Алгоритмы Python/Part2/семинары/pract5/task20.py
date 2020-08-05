"""
Задача 20:
Заполнить один массив случайными числами, другой - введенными с клавиатуры числами, в
ячейки третьего записать суммы соответствующих ячеек первых двух. Вывести содержимое
массивов на экран.
"""

from random import randint

import numpy as np


class ArrayProcessingClass:
    def __init__(self):
        self.inputer()
        self.array_generator()
        self.array_input()
        self.processing()

    def inputer(self):
        """Ввод размерности массива"""
        boolean_flag = True
        while boolean_flag:

            try:
                self.n = int(input("Введите размерность массивов -> "))
                boolean_flag = False

            except ValueError:
                print("Некорректный ввод!")

    def array_generator(self):
        """Генерация массива рандомными числами"""
        arr = np.array([randint(-100, 100) for _ in range(self.n)])
        print("\nСгенерированный массив №1:\n{}".format(arr))
        self.arr1 = arr

    def array_input(self):
        """Ввод элементов массива"""
        arr = np.array([])
        print("*Ввод данных массива №2*")
        for i in range(self.n):
            boolean_flag = True
            while boolean_flag:
                try:
                    element = int(
                        input("Введите элемент массива №{} -> ".format(i + 1))
                    )
                    arr = np.append(arr, element)
                    boolean_flag = False
                except ValueError:
                    print("Некорректный ввод данных!")

        print("\nВведенный массив №2:\n{}".format(arr))
        self.arr2 = arr

    def processing(self):
        """Сумма первых двух массивов"""
        result = self.arr1 + self.arr2
        print("\nСумма двух массивов:\n{}".format(result))


if __name__ == "__main__":
    ArrayProcessingClass()
