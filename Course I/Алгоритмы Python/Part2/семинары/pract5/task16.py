"""
Задача 16*:
Выполнить программную реализацию калькулятора матриц.
"""
import numpy as np

class MatrixClass:
    def __init__(self, value):
        self.value = np.matrix(value)

    def __str__(self):
        """Вывод на экран"""
        pass
    
    def __mul__(self):
        """Умножение матриц"""
    
    

class ClacClass():
    def __init__(self, matrix1=None, matrix2=None):
        if matrix1 == None and matrix2 == None:
            self.generator()
        else:
            self.matrix1 = matrix1
            self.matrix2 = matrix2


if __name__ == "__main__":
    #ClacClass
    