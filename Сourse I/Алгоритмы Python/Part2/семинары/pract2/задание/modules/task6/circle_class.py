import math

from .figure_class import FigureClass


class CircleClass(FigureClass):
    def __init__(self, r):
        self.r = r
        self.perimeter_calculation()
        self.area_calculation()

    def area_calculation(self):
        self.area = math.pi * self.r ** 2

    def perimeter_calculation(self):
        self.perimeter = 2 * math.pi * self.r
