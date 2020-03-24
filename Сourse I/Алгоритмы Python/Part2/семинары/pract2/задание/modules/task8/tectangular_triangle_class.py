import math
from .triangle_class import TriangleClass
class TectangularTriangleClass(TriangleClass):
    def __init__(self, a_side, b_side, angle=90):
        self.angle = 90
        super().__init__(a_side, b_side, angle)
        self.a_side = a_side
        self.b_side = b_side
        self.perimeter_calculation()
        self.area_calculation()
        self.area_calculation()
    def area_calculation(self):
        self.area = (1 / 2) * self.a_side * self.b_side
    def perimeter_calculation(self):
        a = self.a_side
        b = self.b_side
        c = math.sqrt(pow(a, 2) + pow(b, 2))
        self.perimeter = a + b + c