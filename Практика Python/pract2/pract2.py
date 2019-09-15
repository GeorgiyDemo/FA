"""
Деменчук Г.М., вариант 6, задания со звёздочкой *
"""
import math
import matplotlib.pyplot as plt

def get_scale(x,y):
    """
    Метод для возврата точки на основании c и d
    Для динамического масштаба
    """
    x = abs(x)
    y = abs(y)
    if x > y:
        return x
    return y

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
        p = get_scale(c, d)
        
        #Координаты основной оси
        m = ([-p*4, p*4],[0, 0])
        #Исходные точки
        x = [-p*2,-c,0]
        y = [0,0,d]
        #Аннотации к слевой линии
        n1 = ["","-c","d"]
        #Аннотации к правой линии
        n2 = ["-d","c",""]

        plt.style.use('seaborn-dark')
        ax = plt.figure().gca()

        #Ось координат X
        ax.plot(m[0], m[1], linewidth=1, color="k")
        #Ось координат Y
        ax.plot(m[1], m[0], linewidth=1, color="k")
        
        #Линия левая
        ax.plot(x, y, linewidth=2, marker="o", color="b")
        for i in range(len(x)):
            ax.annotate(n1[i],(x[i],y[i]+0.5))
        
        #Линия правая 
        x = [-e for e in reversed(x)]
        y = [-e for e in reversed(y)]
        
        ax.plot(x, y , linewidth=2, marker="o", color="b")
        for i in range(len(x)):
            ax.annotate(n2[i],(x[i],y[i]+0.5))
        plt.show()

def main():

    try:
        d = float(input("Введите d -> "))
        c = float(input("Введите c -> "))
    except:
        print("Проблема ввода данных!")
        return

    LineGraphClass(c, d)

if __name__ == "__main__":
    main()