"""
Задача 1. Создайте класс ФИГУРА с методами вычисления площади и периметра,
а также методом, выводящим информацию о фигуре на экран.

Создайте дочерние классы ПРЯМОУГОЛЬНИК, КРУГ, ТРЕУГОЛЬНИК со своими методами вычисления площади и периметра.
Создайте список п фигур и выведите полную информацию о фигурах на экран.
"""
from abc import ABCMeta, abstractmethod
from math import pi, sqrt
from random import randint

class FigureClass:
    """
    Абстрактный класс фигуры
    """
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

        if type(self.area) == float and type(self.perimeter) == float:
            a = str(round(self.area,2))
            p = str(round(self.perimeter,2))
        print("\nВызов от {}\nПлощадь фигуры: {}\nПериметр фигуры: {}".format(lclass, a, p))

class RectangleClass(FigureClass):
    """
    Класс прямоугольника
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.perimeter_calculation()
        self.area_calculation()

    def perimeter_calculation(self):
        self.perimeter = (self.a+self.b)*2

    def area_calculation(self):
        self.area = self.a*self.b 

class CircleClass(FigureClass):
    """
    Класс круга
    """
    def __init__(self, r):
        self.r = r
        self.perimeter_calculation()
        self.area_calculation()

    def area_calculation(self):
        self.area = pi*self.r**2
    
    def perimeter_calculation(self):
        self.perimeter = 2*pi*self.r

class TriangleClass(FigureClass):
    """
    Класс треугольника
    """
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
        #Полупериметр
        p = (self.a+self.b+self.c)/2
        s = sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        self.area = s

    def perimeter_calculation(self):
        self.perimeter = self.a + self.b + self.c

def main():

    try:
        n = int(input("Введите количество фигур -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
        
    d = {
        0 : RectangleClass,
        1 : CircleClass,
        2 : TriangleClass,
    }

    figures_list = []
    for _ in range(n):
        
        d_args = {
            0 : [randint(1,100),randint(1,100)],
            1 : [randint(1,100)],
            2 : [randint(1,100),randint(1,100),randint(1,100)]
        }

        r_number = randint(0,2)
        figures_list.append(d[r_number](*d_args[r_number]))
    
    for figure in figures_list:
        figure.info(type(figure).__name__)

if __name__ == "__main__":
    main()