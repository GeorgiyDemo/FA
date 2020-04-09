"""
Задание 1 Матричные операции

Задать две произвольные матрицы {3*3}
Найти сумму и разность матриц
Для матриц вычислить:
Определитель
Транспонированную матрицу
Обратную матрицу (сделать проверку умножением на исходную матрицу)
Задать матрицы А(22), В(23), С(32), D(21) генератором случайных чисел из интервала [1;10]
Найти произведения AB, CD, BC, CB.
"""
from random import randint

"""
    def out_result(self):
        #Вывод результирующией матрицы
        print("Результирующая матрица:")
        r = self.result
        for i in range(len(r)):
            for j in range(len(r[i])):
                print('{:4}'.format(r[i][j]), end=" ")
            print()
"""

#TODO заранее 1 раз прокалькулировать все параметры, а затем просто к ним обращаться
class MatrixClass():
    """Класс матрицы"""
    
    def __init__(self, matrix_number=1, input_flag=None):
        """
        matrix_number - номер матрицы для красивого print, в вычислениях никакой роли не играет
        input_flag - флаг ввода данных. 1 - 
        """
        self.matrix = []
        self.matrix_number = matrix_number
        self.input_flag = input_flag
        self._matrix_range_input()
        self._matrix_values_input()

    def _matrix_range_input(self):
        """Ввод данных матрицы в зависимости от флага"""
        boolean_flag = True
        # Размерность матрицы
        while boolean_flag:
            n = input("Введите кол-во строк в матрице №{} -> ".format(self.matrix_number))
            m = input("Введите кол-во столбцов в матрице №{} -> ".format(self.matrix_number))
            if self.digital_checker(n) and self.digital_checker(m):
                boolean_flag = False
                self.n, self.m = int(n), int(m)
            else:
                print("Некорректный ввод данных!")

    def _matrix_values_input(self):
        """Ввод матрицы"""
        allowed_ways = ["1","2"]
        n = self.n
        m = self.m
        matrix = self.matrix

        if self.input_flag == None:
            boolean_flag = True
            while boolean_flag:
                input_flag = input("Каким способом вы хотите задать значения матрицы?\n1. Автоматический ввод\n2. Ручной ввод\n-> ")
                if input_flag in allowed_ways:
                    boolean_flag = False
                    input_flag = int(input_flag)
                else:
                    print("Некорректный ввод данных!")
        else:
            input_flag = self.input_flag
        
        if input_flag == 1:
            #Генерируем матрицу из диапазона
            for i in range(n):
                buf_matrix = []
                for j in range(m):
                    buf_matrix.append(randint(1,10))
                matrix.append(buf_matrix)

        elif input_flag == 2:
            #Ручной ввод матрицы
            for i in range(n):
                buf_matrix = []
                for j in range(m):

                    boolean_flag = True
                    while boolean_flag:
                        e = input("Введите элемент [{}][{}] -> ".format(i + 1, j + 1))
                        if self.digital_checker(e):
                            boolean_flag = False
                            buf_matrix.append(float(e))
                        else:
                            print("Некорректный ввод элемента [{}][{}], повторите попытку.".format(i + 1, j + 1))

                matrix.append(buf_matrix)
        self.matrix = matrix

    def __str__(self):
        """Вывод матрицы"""
        matrix = self.matrix
        s = "Матрица №{}:\n".format(self.matrix_number)
        s += '\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix])
        return s


    def __mul__(self, m2):
        """Умножение матриц"""

        if self.n != m2.m:
            raise ValueError("Кол-во столбцов матрицы != кол-ву строк")

        a = self.matrix
        b = m2.matrix
        c = []

        for i in range(self.n):
            c.append([])
            for j in range(m2.m):
                c[i].append(0)
                for k in range(self.m):
                    c[i][j] += a[i][k] * b[k][j]
        return c
    
    def __add__(self, m2):
        """Сложение матриц"""
        if self.n != m2.n or self.m != m2.m:
            raise ValueError("Матрицы разного порядка!")
        return [list(map(lambda x,y: x+y, self.matrix[i], m2.matrix[i])) for i in range(self.n)]


    def __sub__(self, m2):
        """Вычитание матриц"""
        if self.n != m2.n or self.m != m2.m:
            raise ValueError("Матрицы разного порядка!")
        return [list(map(lambda x,y: x-y, self.matrix[i], m2.matrix[i])) for i in range(self.n)]

    #TODO
    @property
    def matrix_transposed(self):
        """Вычисление транспонированной матрицы"""
        pass
    
    #TODO
    @property
    def matrix_determinant(self):
        """Вычисление определителя матрицы"""
        pass
    
    #TODO
    @property
    def ddd(self):
        """Вычисление обратной матрицы (сделать проверку умножением на исходную матрицу)"""

    def digital_checker(self, number):
        """Метод для проверки элемента на число"""
        try:
            float(number)
            return True
        except ValueError:
            return False


class MainClass():
    def __init__(self):
        self.processing()
    
    def processing(self):
        m1 = MatrixClass(1,1)
        m2 = MatrixClass(2,1)
        print(m1)
        print(m2)
        print("Вычитание: ", m1 - m2)
        print("Сложение: ", m1 + m2)
        print("Умножение: ", m1 * m2)

if __name__ == "__main__":
    MainClass()
