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

if __name__ == "__main__":

    P = np.array(
        [[0.1, 0.4, 0.5],  # Переход из 1 состояния в N
        [0.3, 0.2, 0.5],   # Переход из 2 состояния в N
        [0.6, 0.35, 0.05]] # Переход из 3 состояния в N
    )

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