from .figure_class import FigureClass


class RectangleClass(FigureClass):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter_calculation()
        self.area_calculation()

    def perimeter_calculation(self):
        self.perimeter = (self.a + self.b) * 2

    def area_calculation(self):
        self.area = self.a * self.b
