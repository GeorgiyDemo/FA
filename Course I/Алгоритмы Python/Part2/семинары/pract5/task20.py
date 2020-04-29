"""
Задача 20:
Заполнить один массив случайными числами, другой - введенными с клавиатуры числами, в
ячейки третьего записать суммы соответствующих ячеек первых двух. Вывести содержимое
массивов на экран.
"""

import numpy as np
from random import randint
def input_N():
    """Ввод числа N"""
    try:
        N = int(input("Длина массивов -> "))
        return N
    except ValueError:
        print("Вводить число!")
        return input_N()

N = input_N()
rand_arr = np.array([randint(-100, 100) for _ in range(N)])
print("Рандомный массив:", rand_arr)
# заменить на ручной ввод
my_arr = np.array([])
for i in range(N):
    my_arr = np.append(my_arr, 0)
print("Заполните массив:")
for i in range(N):
    my_arr[i] = int(input())
print("Вводный массив:", my_arr)

arr_sum = np.array([])
for i in range(N):
    arr_sum = np.append(arr_sum, 0)

for i in range(N):
    arr_sum[i] = rand_arr[i] + my_arr[i]

print(arr_sum)