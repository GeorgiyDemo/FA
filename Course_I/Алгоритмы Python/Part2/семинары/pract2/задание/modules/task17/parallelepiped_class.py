from .body_class import BodyClass


class ParallelepipedClass(BodyClass):
    def __init__(self, a, b, c):
        # a,b,c - ребра параллелепипеда
        self.a = a
        self.b = b
        self.c = c
        self.volume_calculation()
        self.surface_area_calculation()

    def surface_area_calculation(self):
        # S = 2(ab + bc + ac)
        a = self.a
        b = self.b
        c = self.c
        self.surface_area = 2 * (a * b + b * c + a * c)

    def volume_calculation(self):
        self.volume = self.a * self.b * self.c
