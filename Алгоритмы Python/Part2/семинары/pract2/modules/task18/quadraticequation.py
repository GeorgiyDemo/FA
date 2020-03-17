from quadraticequation import EquationClass
from parse_exp import parse_exp
class QuadraticEquation(EquationClass):
    def __init__(self, input_str):
        self.equation_results_list = []

        self.input_str = input_str
        self.index_a, self.index_b, self.index_c = parse_exp(input_str)
        self.calculation()


    def info(self):
        locale_list = self.equation_results_list
        if len(locale_list) == 1:
            result_msg = "".join(locale_list)
        elif len(locale_list) == 2:
            result_msg = "Корень А1 = " + str(locale_list[0]) + "\nКорень А2 = " + str(locale_list[1])
        else:
            result_msg = "Ошибка вычисления"
        return "*Информация о квадратном уравнении*\nОбщий вид: " + self.input_str + "\nКоэффициент a = " + str(
            self.index_a) + "\nКоэффициент b = " + str(self.index_b) + "\nКоэффициент c = " + str(
            self.index_c) + "\nОтвет:\n" + result_msg

    def calculation(self):
        a = self.index_a
        b = self.index_b
        c = self.index_c

        D = b ** 2 - 4 * a * c

        if D == 0:
            A1 = -b / (2 * a)
            A2 = A1
            self.equation_results_list.append(A1)
            self.equation_results_list.append(A2)

        elif D > 0:
            A1 = (-b + math.sqrt(D)) / (2 * a)
            A2 = (-b - math.sqrt(D)) / (2 * a)
            self.equation_results_list.append(A1)
            self.equation_results_list.append(A2)

        else:
            self.equation_results_list.append("Нет решения, D < 0")