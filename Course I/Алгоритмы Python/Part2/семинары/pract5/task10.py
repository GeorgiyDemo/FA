"""
Задача 10:
Даны два списка/массива. Определите, совпадают ли множества их элементов.
"""
import numpy as np

class MainClass:
    def __init__(self, arr1=None, arr2=None):
        if any(map(lambda x: x is None,[arr1, arr2])):
            self.arr_input()
        else:
            self.arr1 = arr1
            self.arr2 = arr2
        self.comparer()
    
    def digital_checker(self, n):
        try:
            return int(n)
        except ValueError:
            return n

    def arr_input(self):

        base_arr1, base_arr2 = np.array([]), np.array([])
        try:
            n1 = int(input("Введите размерноcть массива №1 -> "))
            n2 = int(input("Введите размерность массива №2 -> "))
        except ValueError:
            print("Некорректный ввод данных!")
            return

        print("\n*Заполнение массива №1*")
        for i in np.arange(n1):
            base_arr1 = np.append(base_arr1, self.digital_checker(input("Введите элемент №{} -> ".format(i+1))))
        
        print("\n*Заполнение массива №2*")
        for i in np.arange(n2):
            base_arr2 = np.append(base_arr2, self.digital_checker(input("Введите элемент №{} -> ".format(i+1))))
        
        self.arr1 = np.array(base_arr1)
        self.arr2 = np.array(base_arr2)

    def comparer(self):
        d = { True : "массивы совпадают", False : "массивы НЕ совпадают"}
        arr1, arr2 = self.arr1, self.arr2
        print("\nВведенный массив №1: {}\nВведенный массив №2: {}".format(arr1, arr2))
        r = d[np.array_equal(np.unique(arr1), np.unique(arr2))]
        print("\nРезультат: {}".format(r))

if __name__ == "__main__":
    MainClass()
    MainClass(np.array([1,2,3]), np.array([2,2,2,2,1,2,2,2,2,1,1,1,3]))
