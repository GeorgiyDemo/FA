"""
Практика 3 Кривая Коха (93)
Деменчук Георгий ПИ19-4

Реализуйте при помощи рекурсивного алгоритма отрисовку снежинки Коха. Отрегулируйте глубину рекурсии в зависимости от размера получаемых на текущей итерации элементов.
Реализуйте похожим образом другие известные фрактальные кривые, например, кривую дракона.
Отрефакторите код таким образом, чтобы алгоритм построения фрактала и логика отрисовки были изолированными частями программы.
"""

import tkinter as tk
import time
from math import sin, cos, pi

# Начальные позиции
width = 600
height = 600
root = tk.Tk()
# Основной канвас
c = tk.Canvas(root, width=width, heigh=height)

class PointF:
    """Класс точки"""
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def Draw():

    #Определим коорднаты исходного треугольника
    point1 = PointF(200, 200)
    point2 = PointF(500, 200)
    point3 = PointF(350, 400)

    #Вызываем функцию Fractal для того, чтобы
    #нарисовать три кривых Коха на сторонах треугольника
    Fractal(point1, point2, point3, 5)
    Fractal(point2, point3, point1, 5)
    Fractal(point3, point1, point2, 5)

def Fractal(p1, p2, p3, iter):

    if iter > 0:
        p4 = PointF((p2.X + 2 * p1.X) / 3, (p2.Y + 2 * p1.Y) / 3)
        p5 = PointF((2 * p2.X + p1.X) / 3, (p1.Y + 2 * p2.Y) / 3)
        
        #координаты вершины угла
        ps = PointF((p2.X + p1.X) / 2, (p2.Y + p1.Y) / 2)
        pn = PointF((4 * ps.X - p3.X) / 3, (4 * ps.Y - p3.Y) / 3)
        
        #рисуем его

        c.create_line(p4.X,p4.Y, pn.X, pn.Y)
        c.create_line(p5.X,p5.Y, pn.X, pn.Y)
        c.create_line(p4.X,p4.Y, p5.X, p5.Y)
        
        #g.DrawLine(pen1, p4, pn)
        #g.DrawLine(pen1, p5, pn)
        #g.DrawLine(pen2, p4, p5)
        
        #рекурсивно вызываем функцию нужное число раз
        Fractal(p4, pn, p5, iter - 1)
        Fractal(pn, p5, p4, iter - 1)
        Fractal(p1, p4, PointF((2 * p1.X + p3.X) / 3, (2 * p1.Y + p3.Y) / 3), iter - 1)
        Fractal(p5, p2, PointF((2 * p2.X + p3.X) / 3, (2 * p2.Y + p3.Y) / 3), iter - 1)

    else:
        return iter





def main():

    root.title("Снежинка Коха")

    # Распаковка канваса
    c.configure(bg="white")
    c.pack(fill=tk.BOTH, expand=1)

    Draw()
    root.mainloop()


if __name__ == "__main__":
    main()

