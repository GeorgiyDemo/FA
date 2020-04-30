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
        input_value = ""

        d_ways = {"1" : self.summ, "2" : self.diff, "3" : self.mul}
        while input_value != "0":
            input_value = input("\nКакое действие с матрицами вы хотите сделать?\n1. Сложение\n2. Вычитание\n3. Умножение\n0. Выход из меню\n-> ")
            if input_value in d_ways:
                d_ways[input_value]()
            elif input_value != "0":
                print("Некорректный ввод, повторите попытку")

    def summ(self):
        print("А + B:\n{}".format(self.m1 + self.m2))
        print("B + A:\n{}".format(self.m2 + self.m1))
    
    def diff(self):
        print("А - B:\n{}".format(self.m1 - self.m2))
        print("B - A:\n{}".format(self.m2 - self.m1))

    def mul(self):
        print("А * B:\n{}".format(self.m1 * self.m2))
        print("B * A:\n{}".format(self.m2 * self.m1))

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

    def manual_input(self):
        """Ручной ввод матриц"""
        r1, r2 = self.range_input()
        m1, m2 = np.array([]), np.array([])

        d = {"А" : [r1, m1], "B" : [r2, m2]}

        for m_name, m_items in d.items():
            print("*Заполнение матрицы {}*".format(m_name))
            for i in range(m_items[0][0]):
                for j in range(m_items[0][1]):
                    bool_flag = True
                    while bool_flag:
                        try:
                            input_e = int(input("Введите элемент [{}][{}] -> ".format(i, j)))
                            m_items[1] = np.append(m_items[1], input_e)
                            bool_flag = False
                        except ValueError:
                            print("Некорректный ввод данных, повторите попытку")

        m1 = d["А"][1]
        m2 = d["B"][1]

        self.m1 = np.matrix(m1).reshape(*r1)
        self.m2 = np.matrix(m2).reshape(*r2)  

    def printer(self):
        print("Матрица А:\n",self.m1)
        print("Матрица B:\n", self.m2)

if __name__ == "__main__":
    Calculation()