"""
Задание 2 Решение системы линейных уравнений
Персональное задание выбрать по номеру варианта в Приложении 1

Решить систему линейных уравнений двумя способами:
- С помощью обратной матрицы
- Методом Крамера
Выполнить проверку полученных решений.
"""
from DEMKAMatrixClass import MatrixClass
from copy import deepcopy

class MatrixSolver:
    def __init__(self, matrix_list, results_list):
        self.matrix = matrix_list
        self.results_list = results_list
        pass

    def cramers_rule(self):
        """Решение СЛУ методом Крамера"""
        #Главный определитель дельта
        matrix = self.matrix
        obj = MatrixClass(matrix_list=matrix)
        delta_main = obj.matrix_determinant
        print("Исходная матрица: {}\nΔ главная: {}".format(obj,delta_main))
    
        more_matrix = [matrix[i]+[self.results_list[i]] for i in range(len(matrix))]
        print("\nРасширенная исходная матрица:{}".format(MatrixClass(matrix_list=more_matrix)))
        #Список результатов остальных дельт
        sub_deltas_list = []
        #Переворачиваем матрицу для более удобной работы
        rotated_matrix = self._rotate(matrix)

        #Вычисляем остальные дельты
        for i in range(len(matrix)):
            buf_matrix = deepcopy(rotated_matrix)
            #Подставляем результаты в i столбец по методу Крамера
            buf_matrix[i] = self.results_list
            #Переворачиваем
            buf_matrix = self._rotate(buf_matrix)
            #Записываем
            sub_deltas_list.append(MatrixClass(matrix_list=buf_matrix))

        for i in range(len(sub_deltas_list)):
            print("\nΔ{}".format(i+1))
            print(sub_deltas_list[i])
            print("Определитель: {}".format(sub_deltas_list[i].matrix_determinant))
            #Делим поддельты на главную Δ
            sub_deltas_list[i] = sub_deltas_list[i].matrix_determinant/delta_main

        print("\nРезультаты:")
        for r in sub_deltas_list:
            print(r)

    def _rotate(self, matrix):
        """Метод для переворота матрицы"""
        return [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]

    def inverse_matrix(self):
        """Решение СЛУ с помощью обратной матрицы"""


def main():
    l_results = [-46,36,-19,60]
    l = [
        [6,-2,10,4],
        [-6,-4,10,10],
        [0,0,1,-4],
        [0,8,-4,10],
    ]
    obj = MatrixSolver(matrix_list=l,results_list=l_results)
    obj.cramers_rule()

if __name__ == "__main__":
    main()