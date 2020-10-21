"""
Практика 3 Кривая Коха (93)
Деменчук Георгий ПИ19-4

Реализуйте при помощи рекурсивного алгоритма отрисовку снежинки Коха. Отрегулируйте глубину рекурсии в зависимости от размера получаемых на текущей итерации элементов.
Реализуйте похожим образом другие известные фрактальные кривые, например, кривую дракона.
Отрефакторите код таким образом, чтобы алгоритм построения фрактала и логика отрисовки были изолированными частями программы.
"""

import tkinter as tk

# Начальные позиции
width = 750
height = 750
root = tk.Tk()

# Основной канвас
c = tk.Canvas(root, width=width, heigh=height)
alllines_list = []

class PointF:
    """Класс точки"""
    def __init__(self, x, y):
        self.X = x
        self.Y = y

def Draw(number):
    """Отрисовка снежинки"""
    global alllines_list

    #Если уже что-то отрисовано - удаляем это
    if len(alllines_list) != 0:
        for line in alllines_list:
            c.delete(line)
        alllines_list = []
    
    #Определим коорднаты исходного треугольника
    point1 = PointF(66, 559)
    point2 = PointF(694, 559)
    point3 = PointF(380, 14)

    #Вызываем функцию Fractal для того, чтобы
    #нарисовать три кривых Коха на сторонах треугольника
    
    Fractal(point1, point2, point3, number)
    Fractal(point2, point3, point1, number)
    Fractal(point3, point1, point2, number)

    

def Fractal(p1, p2, p3, iter):
    """Рекурсивная функция для вычисления фрактальных точек"""
    
    if iter > 0:

        #print(buflines_list)
        #if len(buflines_list) != 0:
        #    for line in buflines_list:
        #        c.delete(line)
        #    buflines_list = []

        p4 = PointF((p2.X + 2 * p1.X) / 3, (p2.Y + 2 * p1.Y) / 3)
        p5 = PointF((2 * p2.X + p1.X) / 3, (p1.Y + 2 * p2.Y) / 3)
        
        #Координаты вершины угла
        ps = PointF((p2.X + p1.X) / 2, (p2.Y + p1.Y) / 2)
        pn = PointF((4 * ps.X - p3.X) / 3, (4 * ps.Y - p3.Y) / 3)
        
        #рисуем его

        line1 = c.create_line(p4.X,p4.Y, pn.X, pn.Y,fill="white")
        line2 = c.create_line(p5.X,p5.Y, pn.X, pn.Y, fill="white")
        line3 = c.create_line(p4.X,p4.Y, p5.X, p5.Y, fill="white")

        #buflines_list.extend([line1,line2,line3])
        alllines_list.extend([line1,line2,line3])


        
        
        #рекурсивно вызываем функцию нужное число раз
        Fractal(p4, pn, p5, iter - 1)
        Fractal(pn, p5, p4, iter - 1)
        Fractal(p1, p4, PointF((2 * p1.X + p3.X) / 3, (2 * p1.Y + p3.Y) / 3), iter - 1)
        Fractal(p5, p2, PointF((2 * p2.X + p3.X) / 3, (2 * p2.Y + p3.Y) / 3), iter - 1)

    else:
        return iter

def scale_processing(number):
    """Обработка значения ползунка"""

    number = int(number)
    Draw(number)

def main():

    root.title("Снежинка Коха")
    # Распаковка канваса
    c.configure(bg="black")
    c.pack(fill=tk.BOTH, expand=1)

    # Распаковка ползунка
    scale = tk.Scale(
        root,
        from_=0,
        to=6,
        command=scale_processing,
        orient=tk.HORIZONTAL,
    )

    scale.pack(side=tk.LEFT, padx=5)
    root.mainloop()


if __name__ == "__main__":
    main()