from math import pi

from .body_class import BodyClass


class BallClass(BodyClass):
    def __init__(self, r):
        self.r = r
        self.volume_calculation()
        self.surface_area_calculation()

    def surface_area_calculation(self):
        self.surface_area = 4 * pi * pow(self.r, 2)

    def volume_calculation(self):
        self.volume = (4 / 3) * pi * pow(self.r, 3)
