"""
Задача 12:
Пусть элементы списка/массива хранят символы предложения. Замените каждое вхождение слова
"itmathrepetitor" на "silence".
"""
import numpy as np
np_arr = np.array([*list("привет itmathrepetitor мяв")])
for i 
arr = np.where(np_arr =="itmathrepetitor", "silence", np_arr)
print(arr)