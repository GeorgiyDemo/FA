"""
Деменчук Г.М., вариант 6, задания со звёздочкой *
"""
import math
import matplotlib.pyplot as plt
import numpy as np

class LineGraphClass():
    """
    Функции y=y(x), заданные графически*

    """
    def __init__(self, d):
        self.d = d
        self.graph()

    def graph(self):

        x = [1,2,3,4,5]
        y = [1,2,3,4,5]

        fig = plt.figure()
        ax = fig.gca()
        ax.plot(x, y, linewidth=2)
        plt.show()

class MathUpper():
    """
    Вариант задания на условные операторы

    Класс для работы с первым заданием
    на условные операторы
    """
    def __init__(self, x):
        self.x = x
        self.getter()
    
    def getter(self):

        x = self.x
        upper = x**3*math.e**(x-1)
        lower = x**3-math.fabs(x)
        if lower == 0:
            print("Знаменатель равен нулю, деление на 0!")
            self.result = 0
            return

        first = upper/lower
        
        log_sqrt = math.sqrt(x)-x
        
        if log_sqrt >= 0:
            buf_log = math.log(log_sqrt,2)
        else:
            print("Выражение в log[sqrt(x)-x,2] меньше 0!")
            self.result = 0
            return

        self.result = first-buf_log

class CycleClass():
    """
    Вариант задания для операторов цикла

    Класс для вызова MathUpper в цикле
    """
    def __init__(self):
        self.cycle()
    
    def cycle(self):
        x = 0.2
        end_cycle = 0.8

        while x != end_cycle:
            obj = MathUpper(x)
        
            print("x=",x, "result = ",obj.result)
            x = round(x + 0.1, 2)

    pass

def main():

    try:
        d = float(input("Введите -d: "))
    except:
        print("Проблема ввода данных!")
        return

    LineGraphClass(d)


if __name__ == "__main__":
    main()