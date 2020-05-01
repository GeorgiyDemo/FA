"""
Задача 21:
Сгенерировать 2000 случайных целых чисел в диапазоне от -5 до 4, записать их в ячейки
массива. Посчитать сколько среди них положительных, отрицательных и нулевых значений.
Вывести на экран элементы массива и посчитанные количества. Рассмотрите возможность
использования numpy.set_printoptions для полноценного вывода занчений массива на экран.
"""

import sys
import numpy as np
from random import randint

def main():

    arr = np.array([randint(-5, 4) for _ in range(2001)])
    np.set_printoptions(threshold=sys.maxsize)

    print("Элементы массива:\n{}".format(arr))
    print("Положительных: {}".format(arr[arr > 0].shape[0]))
    print("Отрицательных: {}".format(arr[arr < 0].shape[0]))
    print("Равных нулю: {}".format(arr[arr == 0].shape[0]))

if __name__ == "__main__":
    main()