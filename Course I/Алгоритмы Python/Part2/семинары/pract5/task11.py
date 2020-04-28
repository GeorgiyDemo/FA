"""
Задача 11:
Дан список/массив. После каждого элемента добавьте предшествующую ему часть списка.
"""
import numpy as np

#a = [int(i) for i in input("Список: ").split()]
arr_a = np.array([1, 2, 3]) #[1, 1, 2, 1, 2, 3]
arr_b = np.array([])
print("Исходный массив:", arr_a)
for i in range(len(arr_a)):
    for j in range(i+1):
        arr_b = np.append(arr_b, arr_a[j])
print("Результат:", arr_b)