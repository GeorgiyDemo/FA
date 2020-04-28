"""
Задача 10:
Даны два списка/массива. Определите, совпадают ли множества их элементов.
"""
import numpy as np
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,2,3,4,3,5,3])
r = np.array_equal(np.unique(arr1), np.unique(arr2))
print(r)
