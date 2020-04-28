"""
Задача 10:
Даны два списка/массива. Определите, совпадают ли множества их элементов.
"""
import numpy as np

class MainClass:
    def __init__(self):
        self.processing()
    

    def processing(self):

        base_list1 = []
        base_list2 = [] 
        try:
            n1 = int(input("Введите размернсоть массива №1 -> "))
            n2 = int(input("Введите размернсоть массива №2 -> "))
        except ValueError:
            print("Некорректный ввод данных!")
            return
        
        print("*Заполнение массива №1*")
        for i in range(n1):
            input("Введите элемент №{} -> ".format(i+1))
        arr1 = np.array([1,2,3,4,5])
        arr2 = np.array([1,2,3,4,3,5,3])
        r = np.array_equal(np.unique(arr1), np.unique(arr2))
        print()
    
    def comparer(self, arr1, arr2):
        return np.array_equal(np.unique(arr1), np.unique(arr2))

if __name__ == "__main__":
    pass
