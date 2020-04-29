"""
Задача 16*:
Выполнить программную реализацию калькулятора матриц.
"""

import numpy as np
import array as ar
from random import randint

class Calculation:
    def __init__(self, m1 = None, m2 = None):
        if any(map(lambda e: e is None, [m1, m2])):
            bool_flag = True
            d_ways = {"1" : self.generator_input, "2" : self.manual_input}
            while bool_flag:
            
                value = input("Как вы хотите внести элементы матрицы?\n1. Автоматическая генерация\n2. Ручной ввод\n-> ")
                if value in d_ways:
                    d_ways[value]()
                    bool_flag = False
                else:
                    print("Некорректный ввод, повторите попытку")
        else:
            self.m1 = np.matrix(m1)
            self.m2 = np.matrix(m2)

        #Выводим данные
        self.printer()
    
    def range_input(self):
        """Ввод размерностей двух матриц с фильтрацией данных"""
        return_list = []
        matrixname_list = ["А","B"]
        for e in matrixname_list:
            print("*Работа с матрицей {}*".format(e))
            bool_flag = True
            while bool_flag:
                try:
                    n = int(input("Введите кол-во строк -> "))
                    m = int(input("Введите кол-во столбцов -> "))
                    return_list.append((n,m))
                    bool_flag = False
                except ValueError:
                    print("Некорректный ввод данных, повторите попытку")
        return return_list

    def generator_input(self):
        """Автоматическая генерация матриц"""
        r1, r2 = self.range_input()
        m1 = np.random.randint(-100,100,(r1[0],r1[1]))
        m2 = np.random.randint(-100,100,(r2[0],r2[1]))
        self.m1 = m1
        self.m2 = m2

    """
    Адекватный ручной ввод 
    # User input of entries in a  
    # single line separated by space 
    entries = list(map(int, input().split())) 
    
    # For printing the matrix 
    matrix = np.array(entries).reshape(R, C) 
    print(matrix) 
    """
    def manual_input(self):
        """Ручной ввод матриц"""
        r1, r2 = self.range_input()
        m1, m2 = np.matrix([]), np.matrix([])

        for m_name, m_items in {"А" : [r1, m1], "B" : [r2, m2]}.items():
            print("*Заполнение матрицы {}*".format(m_name))
            for i in range(m_items[0][0]):
                buf_arr = np.array([])
                for j in range(m_items[0][1]):
                    bool_flag = True
                    while bool_flag:
                        try:
                            input_e = int(input("Введите элемент [{}][{}] -> ".format(i, j)))
                            buf_arr = np.append(buf_arr, input_e)
                            bool_flag = False
                        except ValueError:
                            print("Некорректный ввод данных, повторите попытку")
                m_items[1] = np.append(m_items[1], buf_arr)

    def printer(self):
        print("Матрица А:\n",self.m1)
        print("Матрица B:\n", self.m2)

if __name__ == "__main__":
    Calculation()

"""

m1 = np.matrix([[1,2,3],[5,6,3],[4,2,5]])
m2 = np.matrix([[7,4,2],[5,6,3],[4,2,5]])

print("Исходная матрица А")
print(m1)
print("Исходная матрица B")
print(m2)

print("Умножение")
r = m1 * m2
print(r)

print("Сумма: ")
print(m1 + m2)

print("Разность:")
print(m1 - m2)

"""