from .triangleclass_calculation import *


class TriangleClass:
    def __init__(self, a_side, b_side, angle):
        self.a_side = a_side
        self.b_side = b_side
        self.angle = angle
        self.c_side, self.perimeter = perimeter_calculation(a_side, b_side, angle)
        self.area = area_calculation(a_side, b_side, self.c_side)

    def info(self, cl_name):
        a = self.area
        p = self.perimeter
        p = str(round(self.perimeter, 2))
        if type(self.area) == float:
            a = str(round(self.area, 2))
        print("\nВызов от {}\nПлощадь фигуры: {}\nПериметр фигуры: {}".format(cl_name, a, p))
