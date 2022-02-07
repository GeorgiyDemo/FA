"""
3) Выполнить программную реализацию умножения матрицы на матрицу (матрица задается пользователем
(задается размерность и вводятся элементы с клавиатуры),
как и вторая матрица, реализуйте проверку корректности введенных данных)
"""


class MatrixClass:
    """Класс матрицы"""

    def __init__(self, matrix_number=1):
        # К нему обращаться за матрицей
        self.matrix = []
        self.matrix_number = matrix_number
        self.matrix_range_input()
        self.matrix_values_input()

    def matrix_range_input(self):
        boolean_flag = True
        # Размерность матрицы
        while boolean_flag:
            n = input(
                "Введите кол-во строк в матрице №{} -> ".format(self.matrix_number)
            )
            m = input(
                "Введите кол-во столбцов в матрице №{} -> ".format(self.matrix_number)
            )
            if self.digital_checker(n) and self.digital_checker(m):
                boolean_flag = False
                self.n, self.m = int(n), int(m)
            else:
                print("Некорректный ввод данных!")

    def matrix_values_input(self):
        """Ввод матрицы"""
        n = self.n
        m = self.m
        matrix = self.matrix
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
                        print(
                            "Некорректный ввод элемента [{}][{}], повторите попытку.".format(
                                i + 1, j + 1
                            )
                        )

            matrix.append(buf_matrix)
        self.matrix = matrix

    def matrix_output(self):
        """Вывод матрицы"""
        print("Матрица №{}".format(self.matrix_number))
        matrix = self.matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:4}".format(matrix[i][j]), end=" ")
            print()

    def digital_checker(self, number):
        """Метод для проверки элемента на число"""
        try:
            float(number)
            return True
        except ValueError:
            return False


class MainClass:
    def __init__(self):
        if self.matrix_creator():
            self.matrix_multiplication()
            self.out_result()
        else:
            print("Умножение матриц невозможно!")

    def matrix_multiplication(self):
        """Метод для перемножения матриц"""
        # raw = n
        # cal = m
        m1 = self.m1
        m2 = self.m2

        a = m1.matrix
        b = m2.matrix
        c = []

        for i in range(m1.n):
            c.append([])
            for j in range(m2.m):
                c[i].append(0)
                for k in range(m1.m):
                    c[i][j] += a[i][k] * b[k][j]

        self.result = c

    def matrix_creator(self):
        """
        Метод для работы с матрицами,
        Проверяет их на совместимость
        """
        m1, m2 = MatrixClass(1), MatrixClass(2)
        if m1.n != m2.m:
            return False
        m1.matrix_output()
        m2.matrix_output()
        self.m1, self.m2 = m1, m2
        return True

    def out_result(self):
        """Вывод результирующией матрицы"""
        print("Результирующая матрица:")
        r = self.result
        for i in range(len(r)):
            for j in range(len(r[i])):
                print("{:4}".format(r[i][j]), end=" ")
            print()


if __name__ == "__main__":
    MainClass()
