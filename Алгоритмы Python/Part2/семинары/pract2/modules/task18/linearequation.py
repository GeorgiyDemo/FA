from equationclass import EquationClass
class LinearEquation(EquationClass):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.calculation()
    def calculation(self):
        self.result = (self.c - self.b) / self.a
    def info(self):
        a = self.a
        b = self.b
        c = self.c
        equation_str = str(a) + "x+" + str(b) + "=" + str(c)
        return "*Информация о простом линейном уравнении*\nОбщий вид: " + equation_str + "\nКоэффициент a = " + str(
            a) + "\nКоэффициент b = " + str(b) + "\nКоэффициент c = " + str(c) + "\nОтвет:\n" + str(self.result)