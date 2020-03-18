from body_class import BodyClass
class PyramidClass(BodyClass):
    def __init__(self, S_main, S_back, h):
        # S_main - площадь основания пирамиды
        # S_back - площадь боковой поверхности
        # h - высота пирамиды
        self.S_main = S_main
        self.S_back = S_back
        self.h = h
        self.volume_calculation()
        self.surface_area_calculation()
    def surface_area_calculation(self):
        self.surface_area = self.S_main + 4 * self.S_back
    def volume_calculation(self):
        self.volume = (1 / 3) * self.S_main * self.h