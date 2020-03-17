import math
from triangle_class import TriangleClass
class EquilateralTriangleClass(TriangleClass):
    def __init__(self, a_side, b_side, angle):
        super().__init__(a_side, b_side, angle)
        self.a_side = a_side
    def perimeter_calculation(self):
        self.perimeter = self.a_side * 3
    def area_calculation(self):
        try:
            a = self.a_side
            h = math.sqrt(pow(a, 2) - (pow(a, 2) / 4))
            self.area = (1 / 2) * a * h
        except ValueError:
            self.area = "Ошибка вычисления"