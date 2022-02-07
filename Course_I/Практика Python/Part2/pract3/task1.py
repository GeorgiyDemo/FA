"""
Задание 1 Матричные операции

Задать две произвольные матрицы {3*3}
Найти сумму и разность матриц
Для матриц вычислить:
Определитель
Транспонированную матрицу
Обратную матрицу (сделать проверку умножением на исходную матрицу)
Задать матрицы А(2*2), В(2*3), С(3*2), D(2*1) генератором случайных чисел из интервала [1;10]
Найти произведения AB, CD, BC, CB.
"""
from DEMKAMatrixClass import MatrixClass


class MainClass:
    def __init__(self):
        self.processing()

    def processing(self):
        # Задание двух произвольных матриц {3*3}
        m1, m2 = MatrixClass(1, n=3, m=3), MatrixClass(1, n=3, m=3)
        print("Матрица №1:{}\nМатрица №2:{}".format(m1, m2))

        # Найти сумму и разность матриц
        print("\nСумма матриц:{}\nРазность матриц:{}".format(m1 + m2, m1 - m2))

        m_list = [m1, m2]
        for i in range(len(m_list)):
            print("\n**Матрица №{}**".format(i + 1))
            print("Определитель: {}".format(m_list[i].matrix_determinant))
            print("Транспонированная матрица:{}".format(m_list[i].matrix_transposed))
            print("Обратная матрица: {}".format(m_list[i].matrix_inverse))
            r = m_list[i] * m_list[i].matrix_inverse
            check = MatrixClass(
                matrix_list=[[round(y, 3) for y in x] for x in r.matrix]
            )
            print("Проверка: {}".format(check))

        # Задать матрицы А(22), В(23), С(32), D(21) генератором случайных чисел из интервала [1;10]
        A = MatrixClass(1, n=2, m=2)
        B = MatrixClass(1, n=2, m=3)
        C = MatrixClass(1, n=3, m=2)
        D = MatrixClass(1, n=2, m=1)

        # Вывод всех сгенерированных матриц
        matrix_list = [{"A": A}, {"B": B}, {"C": C}, {"D": D}]
        [
            [print("\nМатрица {}: {}".format(key, value)) for key, value in e.items()]
            for e in matrix_list
        ]

        # Найти произведения AB, CD, BC, CB.
        calculate_list = [
            {"A": A, "B": B},
            {"C": C, "D": D},
            {"B": B, "C": C},
            {"C": C, "B": B},
        ]
        for e in calculate_list:
            try:
                print("\n[" + "*".join(e.keys()) + "]")
                x, y = e.values()
                print(x * y)

            # Если возникла ошибка разных размерностей матриц
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    MainClass()
