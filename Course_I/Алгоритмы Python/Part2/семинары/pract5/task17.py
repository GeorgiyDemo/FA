"""
Задача 17:
Сдвинуть элементы массива в указанном направлении (влево или вправо) и на указанное число
шагов. Освободившиеся ячейки заполнить нулями. Выводить массив после каждого шага.
"""
from random import randint

import numpy as np


class ChangerClass:
    def __init__(self):
        try:
            n = int(input("Введите кол-во элементов в массиве -> "))
        except ValueError:
            print("Некорректный ввод данных!")
            return
        np_arr = np.array([randint(-100, 100) for _ in range(n)])

        print("Исходный массив:", np_arr)
        self.np_arr = np_arr

        while True:
            try:
                offset_num = int(
                    input(
                        "Введите кол-во шагов для смещения или введите 0 для выхода из программы\n-> "
                    )
                )
                if offset_num == 0:
                    break
                self.offset = offset_num
                offset_input = input(
                    "В какую стороны вы хотите сдвинуть элементы массива?\n1. Влево\n2. Вправо\n-> "
                )
                if offset_input == "1":
                    self.left_offset()
                elif offset_input == "2":
                    self.right_offset()

            except ValueError:
                print("Некорректный ввод данных!")

    def right_offset(self):
        """Смещение вправо"""
        arr = self.np_arr
        offset = self.offset
        new_arr = arr[:-offset]
        new_arr = np.pad(new_arr, (arr.shape[0] - new_arr.shape[0], 0))
        print("Массив после смещения на {} вправо:\n{}".format(offset, new_arr))
        self.np_arr = new_arr

    def left_offset(self):
        """Смещение влево"""

        arr = self.np_arr
        offset = self.offset
        # Обрезаем c помощью slices
        new_arr = arr[offset:]
        # Добавляем нули
        new_arr = np.pad(new_arr, (0, arr.shape[0] - new_arr.shape[0]))
        print("Массив после смещения на {} влево:\n{}".format(offset, new_arr))
        self.np_arr = new_arr


if __name__ == "__main__":
    ChangerClass()
