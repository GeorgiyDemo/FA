"""
Вычислить суму членов того же ряда с заданной точностью ε.
Разработать блок-схему алгоритма и произвести расчёты для ε=10-3 и ε=10-5.
Вычислить точное значение суммы с помощью стандартной математической функции, приведённой в задании.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
"""

from math import log


class MainClass:
    def __init__(self):
        self.x_processing_flag = False
        self.e_processing_flag = False
        self.result_sum = 0

        # Ввод данных
        while not self.x_processing_flag:
            self.x_values_input()
        while not self.e_processing_flag:
            self.e_values_input()

        self.calculating(1, self.x)
        print("Общая сумма: " + str(self.result_sum))

        self.math_calculating()

    def x_values_input(self):
        """
        Метод для ввода данных по x
        """
        try:
            x = float(input("Введите x -> "))
            if x > 1 or x < -1:
                print("Введённое значение не удовлетворяет заданному ограничению")
            else:
                self.x_processing_flag = True
                self.x = x
        except ValueError:
            print("Некорректный ввод данных")

    def math_calculating(self):
        result = log(1 + self.x)
        print("Результат математической функции: " + str(result))

    def e_values_input(self):
        """
        Метод для ввода данных по n
        """
        try:
            self.e = int(input("Введите степень погрешности ε=10^-e -> "))
            self.e_processing_flag = True

        except ValueError:
            print("Некорректный ввод данных")

    def calculating(self, i, x, previous_result=0):
        """
        Рекурсивный метод для вычисления N элемента (так требует задание)
        """
        result = pow(-1, i + 1) * (pow(x, i) / i)
        self.result_sum += result
        print("i = " + str(i) + ", результат: " + str(result))
        # Остановка
        if abs(result - previous_result) < pow(10, -self.e):
            return

        self.calculating(i + 1, x, result)


if __name__ == "__main__":
    MainClass()
