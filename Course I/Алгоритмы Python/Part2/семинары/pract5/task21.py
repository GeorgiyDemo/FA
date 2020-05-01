"""
Задача 21:
Сгенерировать 2000 случайных целых чисел в диапазоне от -5 до 4, записать их в ячейки
массива. Посчитать сколько среди них положительных, отрицательных и нулевых значений.
Вывести на экран элементы массива и посчитанные количества. Рассмотрите возможность
использования numpy.set_printoptions для полноценного вывода занчений массива на экран.

List
Положительных: 7998842
Отрицательных: 10001230
Равных нулю: 1999929
Время: 2.9530217049999976

Numpy
Положительных: 7996617
Отрицательных: 10002649
Равных нулю: 2000735
Время: 0.47020314399999563
"""

import sys
import numpy as np
from random import randint
import timeit

def default():
    l = [randint(-5, 4) for _ in range(2001)]
    #print("Элементы списка:\n{}".format(l))
    print("List")
    a = timeit.default_timer()
    print("Положительных: {}".format(len([e for e in l if e > 0])))
    print("Отрицательных: {}".format(len([e for e in l if e < 0])))
    print("Равных нулю: {}".format(len([e for e in l if e == 0])))
    print("Время: {}".format(timeit.default_timer()-a))

def numpy():
    arr = np.array([randint(-5, 4) for _ in range(2001)])
    np.set_printoptions(threshold=sys.maxsize)
    #print("Элементы массива:\n{}".format(arr))
    print("\nNumpy:")
    a = timeit.default_timer()
    print("Положительных: {}".format(arr[arr > 0].shape[0]))
    print("Отрицательных: {}".format(arr[arr < 0].shape[0]))
    print("Равных нулю: {}".format(arr[arr == 0].shape[0]))
    print("Время: {}".format(timeit.default_timer()-a))

if __name__ == "__main__":
    default()
    numpy()