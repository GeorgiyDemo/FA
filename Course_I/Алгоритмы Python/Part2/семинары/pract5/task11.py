"""
Задача 11:
Дан список/массив. После каждого элемента добавьте предшествующую ему часть списка.
np.array([1, 2, 3]) -> [1, 1, 2, 1, 2, 3]
"""
import numpy as np


class MainClass:
    def __init__(self, arr=None):

        self.result = None
        if arr is None:
            self.arr_input()
        else:
            self.arr = arr

        self.processing()
        self.printer()

    def digital_checker(self, n):
        try:
            return int(n)
        except ValueError:
            return n

    def arr_input(self):
        base_arr = np.array([])
        try:
            n = int(input("Введите размерноcть массива -> "))
        except ValueError:
            print("Некорректный ввод данных!")
            return

        print("\n*Заполнение массива №1*")
        for i in np.arange(n):
            base_arr = np.append(
                base_arr,
                self.digital_checker(input("Введите элемент №{} -> ".format(i + 1))),
            )

        self.arr = np.array(base_arr)

    def processing(self):
        arr_a = self.arr
        arr_b = np.array([])
        for i in range(len(arr_a)):
            for j in range(i + 1):
                arr_b = np.append(arr_b, arr_a[j])
        self.result = arr_b

    def printer(self):
        print("Исходный массив:\n{}".format(self.arr))
        print("Результат:\n{}".format(self.result))


if __name__ == "__main__":
    MainClass(np.array([1, 2, 3]))
    MainClass()
