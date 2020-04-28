"""
Задача 10:
Даны два списка/массива. Определите, совпадают ли множества их элементов.
"""
import numpy as np

class MainClass:
    def __init__(self):
        self.processing()
    
    def digital_checker(self, n):
        try:
            return int(n)
        except ValueError:
            return n

    def processing(self):

        base_list1 = []
        base_list2 = [] 
        try:
            n1 = int(input("Введите размерноcть массива №1 -> "))
            n2 = int(input("Введите размерность массива №2 -> "))
        except ValueError:
            print("Некорректный ввод данных!")
            return
        
        print("\n*Заполнение массива №1*")
        for i in range(n1):
            base_list1.append(self.digital_checker(input("Введите элемент №{} -> ".format(i+1))))
        
        print("\n*Заполнение массива №2*")
        for i in range(n2):
            base_list2.append(self.digital_checker(input("Введите элемент №{} -> ".format(i+1))))
        
        print("\nВведенный массив №1: {}\nВведенный массив №2: {}".format(base_list1, base_list2))
        print("\nРезультат: {}".format(self.comparer(base_list1, base_list2)))
    
    def comparer(self, arr1, arr2):
        d = { True : "массивы совпадают", False : "массивы НЕ совпадают"}
        return d[np.array_equal(np.unique(arr1), np.unique(arr2))]

if __name__ == "__main__":
    MainClass()
