"""
Деменчук Г.М., вариант 6, задания со звёздочкой *
"""
import math
import matplotlib.pyplot as plt

class LineGraphClass():
    """
    Функции y=y(x), заданные графически*
    """
    def __init__(self, c, d):

        self.c = c
        self.d = d
        self.graph()

    def graph(self):
        c = self.c
        d = self.d

        #Необходимо для адекватного масштаба
        #TODO
        buf_с = abs(c)
        
        #Координаты осей
        m = ([-20, 20],[0, 0])
        x = [-10,-c,0]
        y = [0,0,d]

        plt.style.use('seaborn-dark')
        ax = plt.figure().gca()

        #Ось координат X
        ax.plot(m[0], m[1], linewidth=1, color="k")
        #Ось координат Y
        ax.plot(m[1], m[0], linewidth=1, color="k")
        #Линия левая
        ax.plot(x, y, linewidth=2, marker="o", color="b")
        #Линия правая 
        ax.plot([-e for e in reversed(x)], [-e for e in reversed(y)] , linewidth=2, marker="o", color="b")
        plt.show()

def main():

    try:
        d = float(input("Введите d: "))
        c = float(input("Введите c: "))
    except:
        print("Проблема ввода данных!")
        return

    LineGraphClass(c, d)


if __name__ == "__main__":
    main()