from abc import ABCMeta, abstractmethod
class FigureClass:
    __metaclass__ = ABCMeta
    @abstractmethod
    def perimeter_calculation(self):
        self.perimeter = 0
    @abstractmethod
    def area_calculation(self):
        self.area = 0
    def info(self, lclass):
        a = self.area
        p = self.perimeter
        if type(self.area) == float or type(self.perimeter) == float:
            a = str(round(self.area, 2))
            p = str(round(self.perimeter, 2))
        print("\nВызов от {}\nПлощадь фигуры: {}\nПериметр фигуры: {}".format(lclass, a, p))