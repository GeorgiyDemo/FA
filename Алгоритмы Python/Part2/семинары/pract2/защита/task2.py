"""
2)Выполнить программную реализацию умножения матрицы на число (матрица задается пользователем
(задается размерность и вводятся элементы с клавиатуры),
как и число, реализуйте проверку корректности введенных данных.
"""
import copy


class MainClass():
    def __init__(self):
        self.matrix = []
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
        self.number_input()
        self.matrix_print()
        self.calculating()
        self.result_print()

    def number_input(self):
        """Ввод числа"""
        boolean_flag = True
        while boolean_flag:
            number = input("Введите число для умножения -> ")
            if self.digital_checker(number):
                self.number = float(number)
                boolean_flag = False
            else:
                print("Некорректный ввод данных!")

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
                        print("Некорректный ввод элемента [{}][{}], повторите попытку.".format(i + 1, j + 1))

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
                print('{:4}'.format(matrix[i][j]), end=" ")
            print()
        print("Введенное число для умножения: {}".format(self.number))

    def result_print(self):
        """Вывод результирующей матрицы"""
        print("Результат: ")
        result = self.result
        for i in range(len(result)):
            for j in range(len(result[i])):
                print('{:4}'.format(result[i][j]), end=" ")
            print()

    def calculating(self):
        """Перемножение матрицы на число"""
        result = copy.deepcopy(self.matrix)
        for i in range(len(result)):
            for j in range(len(result)):
                result[i][j] *= self.number

        self.result = result


if __name__ == "__main__":
    MainClass()
