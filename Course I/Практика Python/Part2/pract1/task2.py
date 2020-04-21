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

        self.calculating()
        print("x={}, n={}, sum={}\n".format(self.x, self.i, self.final_sum))

        self.math_calculating()

    def e_values_input(self):
        """
        Метод для ввода данных по e
        """
        try:
            self.e = int(input("Введите e -> "))
            self.e_processing_flag = True
        except ValueError:
            print("Некорректный ввод данных")

    def calculating(self):
        """
        Метод для вычисление по рекурентной формуле
        """
        e_input = self.e
        x_input = self.x
        locale_m = -1
        locale_c = 1
        locale_p = 1

        final_sum = 0

        i = 0

        while True:
            # Рекурентные формулы
            if i == 0:
                locale_c = 1
            else:
                locale_c += 1  # знаменатель
            locale_m = -locale_m  # знак
            locale_p = x_input * locale_p  # числитель
            locale_result = locale_m * locale_p / locale_c
            print("Итерация №{}, результат: {}".format(i, locale_result))
            final_sum += locale_result

            if abs(locale_m * locale_p / locale_c) < 10 ** -e_input:
                self.i = i
                break
            else:
                i += 1

        self.final_sum = final_sum

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
        """
        Метод для точного вычисления с помощью math
        """
        result = log(1 + self.x)
        print("Результат с помощью math.log: {}".format(result))


if __name__ == "__main__":
    MainClass()
