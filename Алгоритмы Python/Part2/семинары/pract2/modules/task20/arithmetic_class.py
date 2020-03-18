from .progression_class import ProgressionClass
class ArithmeticClass(ProgressionClass):
    def __init__(self, a1, a2, n):
        self.a1 = a1
        self.a2 = a2
        self.n = n
        self.calculate()
    def calculate(self):
        self.s = (self.a1 + self.a2) * self.n / 2
    def info(self):
        return "[Арифметическая прогрессия]\n1-й элемент: " + str(self.a1) + "\n2-й элемент: " + str(self.a2) + "\nШаг: " + str(self.n) + "\nСумма: " + str(self.s)