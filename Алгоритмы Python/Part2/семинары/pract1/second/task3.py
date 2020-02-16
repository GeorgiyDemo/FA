"""
TODO Задача  3. Создайте класс ТРЕУГОЛЬНИК, заданный длинами двух сторон и угла между ними,
с методами вычисления площади и периметра треугольника, а также методом,
выводящим информацию о фигуре на экран.

Создайте дочерние классы ПРЯМОУГОЛЬНЫЙ, РАВНОБЕДРЕННЫЙ, РАВНОСТОРОННИЙ со своими
методами вычисления площади и периметра.

Создайте список п треугольников и выведите полную информацию о треугольниках на экран.
"""

from abc import ABCMeta, abstractmethod
import math
from random import randint

class TriangleClass:
    """
    Базовый класс треугольника
    """
    def __init__(self, a_side, b_side, angle):
        self.a_side = a_side
        self.b_side = b_side
        self.angle = angle

        self.c_side_calculation()

        if self.validator():
            self.perimeter_calculation()
            self.area_calculation()

    def c_side_calculation(self):
        b = self.b_side
        a = self.a_side
        c = math.sqrt(b**2 + a**2 - 2*b*a * math.cos(self.angle))
        print(c)
        self.c_side = c
    
    def validator(self):
        a = self.a_side
        b = self.b_side
        c = self.c_side

        if a + b <= c or a + c <= b or b + c <= a:
            
            print("Треугольника со сторонами {}, {}, {} не существует".format(a, b, c))
            self.area = "Не существует"
            self.perimeter = "Не существует"
            
            return False
        
        return True

    def perimeter_calculation(self):
        self.perimeter = self.a_side + self.b_side + self.c_side

    def area_calculation(self):

        #Вычисление полупериметра
        a = self.a_side
        b = self.b_side
        c = self.c_side

        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        self.area = s

    def info(self):

        a = self.area
        p = self.perimeter

        if type(self.area) == float and type(self.perimeter) == float:
            a = str(round(self.area,2))
            p = str(round(self.perimeter,2))
        print("\nВызов от {}\nПлощадь фигуры: {}\nПериметр фигуры: {}".format(1, a, p))

class TectangularClass(TriangleClass):
    """
    Прямоугольный треугольник
    """
    def __init__(self, a_side, b_side, angle):
        super().__init__(a_side, b_side, angle)
        self.a_side = a_side
        self.b_side = b_side

        if self.validator():
            self.perimeter_calculation()
            self.area_calculation()

        self.area_calculation()

    def area_calculation(self):
        self.area = (1/2)*self.a_side*self.b_side


def main():
    obj1 = TriangleClass(5,11,111)
    obj1.info()

"""
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
"""
if __name__ == "__main__":
    main()