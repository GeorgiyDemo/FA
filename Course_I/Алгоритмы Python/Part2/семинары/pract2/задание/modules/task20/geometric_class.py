from .progression_class import ProgressionClass


class GeometricClass(ProgressionClass):
    def __init__(self, b1, q):
        self.b1 = b1
        self.q = q
        self.calculate()

    def calculate(self):
        try:
            self.s = self.b1 / (1 - self.q)
        except ZeroDivisionError:
            self.s = -1

    def info(self):
        return (
            "[Геометрическая прогрессия]\nЗнаменатель прогрессии: "
            + str(self.q)
            + "\n1-й элемент: "
            + str(self.b1)
            + "\nСумма: "
            + str(self.s)
        )
