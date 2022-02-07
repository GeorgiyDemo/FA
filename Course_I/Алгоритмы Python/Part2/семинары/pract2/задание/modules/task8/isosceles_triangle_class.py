import math

from .triangle_class import TriangleClass


class IsoscelesTriangleClass(TriangleClass):
    def __init__(self, a_side, b_side, angle):
        super().__init__(a_side, b_side, angle)
        self.a_side = a_side
        self.b_side = b_side

    def perimeter_calculation(self):
        self.perimeter = self.b_side * 2 + self.a_side

    def area_calculation(self):
        a = self.a_side
        b = self.b_side
        try:
            part_a = a / 2
            h = math.sqrt(pow(b, 2) - pow(part_a, 2))
            self.area = (h * a) / 2
        except ValueError:
            self.area = "Ошибка вычисления"
