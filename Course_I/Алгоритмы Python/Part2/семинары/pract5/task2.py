"""
Задача 2:
В массиве найти максимальный элемент с четным индексом.
Другая формулировка задачи: среди элементов массива с четными индексами, найти тот,
который имеет максимальное значение.
"""
import array as ar
from random import randint

main_arr = ar.array("i", [randint(-100, 100) for _ in range(50)])
print("Исходный массив:", main_arr)
max_element = -100
for i in range(len(main_arr)):
    if i % 2 == 0 and main_arr[i] > max_element:
        max_element = main_arr[i]
        print("Индекс {}, элемент: {}".format(i, max_element))
print("Макс элемент с четным индексом: {}".format(max_element))
