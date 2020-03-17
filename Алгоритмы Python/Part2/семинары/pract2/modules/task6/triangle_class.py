from figure_class import FigureClass
class TriangleClass(FigureClass):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.validator():
            self.area_calculation()
            self.perimeter_calculation()
    def validator(self):
        a = self.a
        b = self.b
        c = self.c
        if a + b <= c or a + c <= b or b + c <= a:
            self.area = "Не существует"
            self.perimeter = "Не существует"
            return False
        return True
    def area_calculation(self):
        p = (self.a + self.b + self.c) / 2
        s = pow(p * (p - self.a) * (p - self.b) * (p - self.c),1/2)
        self.area = s
    def perimeter_calculation(self):
        self.perimeter = self.a + self.b + self.c