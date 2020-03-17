from equationclass import EquationClass
from parse_exp import parse_exp
import math
from quadraticequation_calculation import calculation
class QuadraticEquation(EquationClass):
    def __init__(self, input_str):
        self.equation_results_list = []
        self.input_str = input_str
        self.index_a, self.index_b, self.index_c = parse_exp(input_str)
        self.equation_results_list = calculation(self.index_a, self.index_b, self.index_c)
    def info(self):
        locale_list = self.equation_results_list
        if len(locale_list) == 1:
            result_msg = "".join(locale_list)
        elif len(locale_list) == 2:
            result_msg = "Корень А1 = " + str(locale_list[0]) + "\nКорень А2 = " + str(locale_list[1])
        else: result_msg = "Ошибка вычисления"
        return "*Информация о квадратном уравнении*\nОбщий вид: " + self.input_str + "\nКоэффициент a = " + str(
            self.index_a) + "\nКоэффициент b = " + str(self.index_b) + "\nКоэффициент c = " + str(
            self.index_c) + "\nОтвет:\n" + result_msg