"""
1) Выполнить программную реализацию умножения матрицы на вектор (матрица задается пользователем: задается размерность и вводятся с элементы с клавиатуры),
как и вектор (задается размерность с клавиатуры и вводятся элементы с клавиатуры), реализуйте проверку корректности введенных данных.
"""


class MainClass:
    def __init__(self):
        self.matrix = []
        self.vector = []
        boolean_flag = True
        # Размерность матрицы
        while boolean_flag:
            n = input("Введите кол-во строк в матрице -> ")
            m = input("Введите кол-во столбцов в матрице -> ")

            if self.digital_checker(n) and self.digital_checker(m):
                boolean_flag = False
                self.n, self.m = int(n), int(m)

            else:
                print("Некорректный ввод данных!")

        self.matrix_input()
        self.vector_input()

        self.matrix_print()
        self.vector_print()

        self.calculating()
        self.result_print()

    def vector_input(self):
        """Ввод вектора"""
        # Т.к. вектор - это тоже матрица с кол-вом столбцов 1
        vector = self.vector
        for i in range(self.n):
            boolean_flag = True
            while boolean_flag:
                e = input("Введите элемент вектора №{} -> ".format(i + 1))
                if self.digital_checker(e):
                    boolean_flag = False
                    vector.append(float(e))
                else:
                    print(
                        "Некорректный ввод элемента вектора №{}, повторите попытку.".format(
                            i + 1
                        )
                    )

        self.vector = vector

    def matrix_input(self):
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

    def digital_checker(self, number):
        """Метод для проверки элемента на число"""
        try:
            float(number)
            return True
        except ValueError:
            return False

    def matrix_print(self):
        """Вывод матрицы"""
        print("Введенная матрица: ")
        matrix = self.matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{:4}".format(matrix[i][j]), end=" ")
            print()

    def vector_print(self):
        """Вывод вектора"""
        print("Введенный вектор: ")
        for e in self.vector:
            print(e)

    def result_print(self):
        """Вывод реузльтирующей матрицы"""
        print("Результат: ")
        result = self.result
        for e in result:
            print(e)

    def calculating(self):
        """Перемножение матрицы на вектор"""
        matrix = self.matrix
        vector = self.vector
        result = []
        for i in range(len(matrix)):

            current_line = matrix[i]
            line_sum = 0
            for e in current_line:
                line_sum += e * vector[i]

            result.append(line_sum)
        self.result = result


if __name__ == "__main__":
    MainClass()
