from abc import ABCMeta, abstractmethod


class BodyClass:
    __metaclass__ = ABCMeta

    @abstractmethod
    def surface_area_calculation(self):
        self.surface_area = 0

    @abstractmethod
    def volume_calculation(self):
        self.volume = 0

    def info(self, lclass=None):
        a = self.surface_area
        v = self.volume
        if type(self.surface_area) == float or type(self.volume) == float:
            a = str(round(self.surface_area, 2))
            v = str(round(self.volume, 2))
        print("\nВызов от {}\nПлощадь поверхности фигуры: {}\nОбъем фигуры: {}".format(lclass, a, v))
