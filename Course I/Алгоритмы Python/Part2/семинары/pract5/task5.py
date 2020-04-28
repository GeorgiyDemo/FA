"""
Задача 5:
В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как
равны между собой (оба являться минимальными), так и различаться.
"""
import numpy as np
from random import randint
def main():
    try:
        n = int(input("Введите кол-во элементов в массиве -> "))
    except ValueError:
        print("Некорректный ввод данных!")
        return
    np_arr = np.array([randint(-100,100) for _ in range(n)])
    print("Исходный массив:", np_arr)

    index1, e_min1 =  np_arr.argmin(), np_arr.min()
    np_arr = np.delete(np_arr, index1)
    index2, e_min2 =  np_arr.argmin(), np_arr.min()
    print("Наименьший элемент №1: {} с индексом {}\nНаименьший элемент №2: {} с индексом {}".format(e_min1, index1, e_min2, index2))

if __name__ == "__main__":
    main()