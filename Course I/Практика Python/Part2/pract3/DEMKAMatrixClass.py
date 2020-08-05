"""Самописный класс для удобной работы с матрицами"""

from copy import deepcopy
from random import randint


class MatrixClass:
    """Класс матрицы"""

    def __init__(self, generation_way=None, matrix_list=None, n=None, m=None):
        """
        generation_way - флаг ввода данных. 1 - автоматический ввод, 2 - ручной ввод
        matrix_list - создание объекта MatrixClass из существующей матрицы в list
        """

        self.generation_way = generation_way
        self.n, self.m = n, m
        # Генерируем новую матрицу
        if matrix_list == None:
            self._matrix = []
            self._matrix_range_input()
            self._matrix_values_input()
        # Выставляем текущую матрицу
        else:
            self._matrix = matrix_list
            if self.n == None and self.m == None:
                self.n = len(matrix_list)
                self.m = len(matrix_list[0])

    def _matrix_range_input(self):
        """Ввод данных матрицы в зависимости от флага"""
        if self.n != None and self.m != None:
            return
        boolean_flag = True
        # Размерность матрицы
        while boolean_flag:
            n = input("Введите кол-во строк в матрице -> ")
            m = input("Введите кол-во столбцов в матрице -> ")
            if self._digital_checker(n) and self._digital_checker(m):
                boolean_flag = False
                self.n, self.m = int(n), int(m)
            else:
                print("Некорректный ввод данных!")

    def _matrix_values_input(self):
        """Ввод матрицы"""
        allowed_ways = ["1", "2"]
        n = self.n
        m = self.m
        matrix = self._matrix

        if self.generation_way == None:
            boolean_flag = True
            while boolean_flag:
                generation_way = input(
                    "Каким способом вы хотите задать значения матрицы?\n1. Автоматический ввод\n2. Ручной ввод\n-> "
                )
                if generation_way in allowed_ways:
                    boolean_flag = False
                    generation_way = int(generation_way)
                else:
                    print("Некорректный ввод данных!")
        else:
            generation_way = self.generation_way

        if generation_way == 1:
            # Генерируем матрицу из диапазона
            for i in range(n):
                buf_matrix = []
                for j in range(m):
                    buf_matrix.append(randint(1, 10))
                matrix.append(buf_matrix)

        elif generation_way == 2:
            # Ручной ввод матрицы
            for i in range(n):
                buf_matrix = []
                for j in range(m):

                    boolean_flag = True
                    while boolean_flag:
                        e = input("Введите элемент [{}][{}] -> ".format(i + 1, j + 1))
                        if self._digital_checker(e):
                            boolean_flag = False
                            buf_matrix.append(float(e))
                        else:
                            print(
                                "Некорректный ввод элемента [{}][{}], повторите попытку.".format(
                                    i + 1, j + 1
                                )
                            )

                matrix.append(buf_matrix)
        self._matrix = matrix

    def __str__(self):
        """Вывод матрицы"""
        matrix = self._matrix
        return "\n" + "\n".join(
            ["\t".join([str(cell) for cell in row]) for row in matrix]
        )

    def __mul__(self, m2):
        """Умножение матриц"""

        if self.m != m2.n:
            raise ValueError("Кол-во столбцов матрицы != кол-ву строк")

        a = self._matrix
        b = m2.matrix
        c = []

        for i in range(self.n):
            c.append([])
            for j in range(m2.m):
                c[i].append(0)
                for k in range(self.m):
                    c[i][j] += a[i][k] * b[k][j]
        return MatrixClass(matrix_list=c)

    def __add__(self, m2):
        """Сложение матриц"""
        if self.n != m2.n or self.m != m2.m:
            raise ValueError("Матрицы разного порядка!")
        c = [
            list(map(lambda x, y: x + y, self._matrix[i], m2.matrix[i]))
            for i in range(self.n)
        ]
        return MatrixClass(matrix_list=c)

    def __sub__(self, m2):
        """Вычитание матриц"""
        if self.n != m2.n or self.m != m2.m:
            raise ValueError("Матрицы разного порядка!")
        c = [
            list(map(lambda x, y: x - y, self._matrix[i], m2.matrix[i]))
            for i in range(self.n)
        ]
        return MatrixClass(matrix_list=c)

    def _matrix_transposed(self):
        """Вычисление транспонированной матрицы"""
        matrix = self._matrix
        return MatrixClass(matrix_list=list(zip(*matrix)))

    def _matrix_determinant(self, A=None, total=0):
        """Вычисление определителя матрицы"""
        # Если первая итерация
        if A == None:
            A = self._matrix

        indices = list(range(len(A)))

        # Когда доехали до матрицы 2 на 2
        if len(A) == 2 and len(A[0]) == 2:
            val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
            return val

        # Определяем подматрицу
        for fc in indices:

            As = deepcopy(A)
            As = As[1:]  # Удаляем первую строку
            height = len(As)

            for i in range(height):
                As[i] = As[i][0:fc] + As[i][fc + 1 :]

            sign = (-1) ** (fc % 2)
            sub_det = self._matrix_determinant(As)
            total += sign * A[0][fc] * sub_det

        return total

    def _matrix_minor(self, i, j):
        """Вычисление минора матрицы"""
        m = self._matrix
        return [row[:j] + row[j + 1 :] for row in (m[:i] + m[i + 1 :])]

    def _matrix_inverse(self):
        """Вычисление обратной матрицы (сделать проверку умножением на исходную матрицу)"""
        m = self._matrix
        # Определитель матрицы
        determinant = self._matrix_determinant()

        # Вычисления для матрицы 2x2
        if len(m) == 2:
            return MatrixClass(
                matrix_list=[
                    [m[1][1] / determinant, -1 * m[0][1] / determinant],
                    [-1 * m[1][0] / determinant, m[0][0] / determinant],
                ]
            )

        # Результат
        result_matrix = []
        for r in range(len(m)):
            cofactorRow = []
            for c in range(len(m)):
                minor = self._matrix_minor(r, c)
                cofactorRow.append(((-1) ** (r + c)) * self._matrix_determinant(minor))
            result_matrix.append(cofactorRow)

        # Транспонированная матрица
        result_matrix = list(map(list, zip(*result_matrix)))

        for r in range(len(result_matrix)):
            for c in range(len(result_matrix)):
                result_matrix[r][c] = result_matrix[r][c] / determinant
        return MatrixClass(matrix_list=result_matrix)

    def _digital_checker(self, number):
        """Метод для проверки элемента на число"""
        try:
            float(number)
            return True
        except ValueError:
            return False

    @property
    def matrix(self):
        return self._matrix

    @property
    def matrix_transposed(self):
        """Свойство для транспонированной матрицы"""
        return self._matrix_transposed()

    @property
    def matrix_determinant(self):
        """Свойство для определителя матрицы"""
        return self._matrix_determinant()

    @property
    def matrix_inverse(self):
        """Свойство для обратной матрицы"""
        return self._matrix_inverse()
