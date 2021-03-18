import numpy as np
from numpy.linalg import matrix_power

def task1(matrix, k):
    """
    Получаем матрицу вероятностей
    k - кол-во шагов
    """
    return matrix_power(matrix, k)

def task2(matrix, n, a0):
    """
    Вероятности состояний системы через n шагов с начальными данными
    """
    p_power = matrix_power(matrix, n)
    #Умножение матриц
    return np.dot(p_power, a0)

class MatrixGenerator:
    """Генерация матрицы переходов"""
    def __init__(self, length : int) -> None:
        
        self.length = length
        self.data = []
        self.null_matrix_gen()
    
    def null_matrix_gen(self):
        """
        Инициализация элементов матрицы
        """
        for i in range(self.length):
            self.data.append([])
            for j in range(self.length):
                self.data[i].append(0)

    def __str__(self) -> str:
        return "\n".join(map(str,self.data))
    
    def add(self, step_from : int, step_to : int, koeff : float):
        """
        Добвление данных
        """
        self.data[step_from-1][step_to-1] = koeff
    
def main():
    
    #вероятность того, что за 10 шагов система перейдет из состояния 1 в состояние 12;
    matrix = MatrixGenerator(17)
    matrix.add(1, 2, 0.28)
    matrix.add(1, 6, 0.41)

    matrix.add(2, 1, 0.51)
    matrix.add(2, 3, 0.1)
    matrix.add(2, 5, 0.02)

    matrix.add(3, 1, 0.11)
    matrix.add(3, 4, 0.16)
    matrix.add(3, 8, 0.58)

    matrix.add(4, 3, 0.31)
    matrix.add(4, 7, 0.43)
    matrix.add(4, 8, 0.19)

    matrix.add(5, 2, 0.05)
    matrix.add(5, 4, 0.14)
    matrix.add(5, 8, 0.2)
    matrix.add(5, 9, 0.2)

    matrix.add(6, 1, 0.44)
    matrix.add(6, 9, 0.5)

    matrix.add(7, 6, 0.15)
    matrix.add(7, 8, 0.25)
    matrix.add(7, 13, 0.21)
    matrix.add(7, 12, 0.13)
    matrix.add(7,10, 0.03)

    matrix.add(8, 5, 0.25)
    matrix.add(8, 6, 0.14)
    matrix.add(8, 13, 0.3)
    matrix.add(8, 11, 0.27)

    matrix.add(9, 3, 0.14)
    matrix.add(9, 4, 0.06)
    matrix.add(9, 5, 0.21)
    matrix.add(9, 6, 0.19)
    matrix.add(9, 13, 0.08)
    matrix.add(9, 11, 0.02)

    matrix.add(10, 7, 0.12)
    matrix.add(10, 8, 0.33)
    matrix.add(10, 17, 0.17)
    matrix.add(10, 16, 0.04)
    matrix.add(10, 15, 0.3)

    matrix.add(11, 12, 0.28)
    matrix.add(11, 16, 0.27)
    matrix.add(11, 15, 0.18)
    matrix.add(11, 14, 0.13)
    matrix.add(11, 10, 0.11)

    matrix.add(12, 17, 0.22)
    matrix.add(12, 14, 0.18)
    matrix.add(12, 11, 0.5)

    matrix.add(13, 9, 0.27)
    matrix.add(13, 8, 0.16)
    matrix.add(13, 7, 0.27)
    matrix.add(13, 14, 0.02)
    matrix.add(13, 15, 0.24)

    matrix.add(14, 11, 0.29)
    matrix.add(14, 15, 0.37)

    matrix.add(15, 10, 0.06)
    matrix.add(15, 12, 0.31)
    matrix.add(15, 13, 0.2)
    matrix.add(15, 14, 0.34)

    matrix.add(16, 10, 0.22)
    matrix.add(16, 17, 0.68)

    matrix.add(17, 12, 0.79)
    print(matrix)

    VECTOR = ([0.1,0.2, 0.3])

    k = 7 #Кол-во шагов
    result_1 = task1(P, k)
    
    print("Исходная матрица:")
    print(P)
    print("Матрица вероятностей:")
    print(result_1)

    A0 = 2 #спустя 2 шага
    result_2 = task2(P, steps_after,VECTOR)
    print("Задание 2")
    print(f"2. Вероятности состояний системы спустя {steps_after} шагов с заданными начальными вероятностями:\n{VECTOR} = {result_2}")


if __name__ == "__main__":
    main()