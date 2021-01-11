"""
Практика 3 Кривая Коха (93)
Деменчук Георгий ПИ19-4

Реализуйте при помощи рекурсивного алгоритма отрисовку снежинки Коха. Отрегулируйте глубину рекурсии в зависимости от размера получаемых на текущей итерации элементов.
Реализуйте похожим образом другие известные фрактальные кривые, например, кривую дракона.
Отрефакторите код таким образом, чтобы алгоритм построения фрактала и логика отрисовки были изолированными частями программы.
"""

import tkinter as tk
from tkinter import ttk

# Начальные позиции
width = 750
height = 750
root = tk.Tk()
checkbox_flag = tk.BooleanVar()

# Основной канвас
c = tk.Canvas(root, width=width, heigh=height)
# Список всех линий, чтоб их удалять
alllines_list = []


class PointF:
    """Класс точки"""

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __str__(self):
        return "Точка ({}, {})".format(self.X, self.Y)


def Draw(number):
    """Отрисовка снежинки"""
    global alllines_list

    # Если уже что-то отрисовано - удаляем это
    if len(alllines_list) != 0:
        for line in alllines_list:
            c.delete(line)
        alllines_list = []

    # Определим начальные коорднаты исходного треугольника и проводим линии
    begin_line1 = c.create_line(66, 559, 694, 559, fill="white")
    begin_line2 = c.create_line(694, 559, 380, 14, fill="white")
    begin_line3 = c.create_line(380, 14, 66, 559, fill="white")

    point1 = PointF(66, 559)
    point2 = PointF(694, 559)
    point3 = PointF(380, 14)

    begin_list = [begin_line1, begin_line2, begin_line3]
    alllines_list.extend(begin_list)

    # Вызываем функцию Fractal для того, чтобы
    # нарисовать три кривых Коха на сторонах треугольника

    Fractal(point1, point2, point3, number, begin_list)
    Fractal(point2, point3, point1, number, begin_list)
    Fractal(point3, point1, point2, number, begin_list)


def Fractal(p1, p2, p3, iter, buflines_list=[]):
    """Рекурсивная функция для вычисления фрактальных точек"""

    if iter > 0:

        # Если отключено полное построение, то удаляем линии с предыдущей итерации
        if not checkbox_flag.get():
            if len(buflines_list) != 0:
                for line in buflines_list:
                    c.delete(line)
                buflines_list = []

        p4 = PointF((p2.X + 2 * p1.X) / 3, (p2.Y + 2 * p1.Y) / 3)
        c.create_oval(p4.X - 5, p4.Y - 5, p4.X + 5, p4.Y + 5, fill="cyan")
        p5 = PointF((2 * p2.X + p1.X) / 3, (p1.Y + 2 * p2.Y) / 3)
        c.create_oval(p5.X - 5, p5.Y - 5, p5.X + 5, p5.Y + 5, fill="blue")
        ps = PointF((p2.X + p1.X) / 2, (p2.Y + p1.Y) / 2)
        c.create_oval(ps.X - 5, ps.Y - 5, ps.X + 5, ps.Y + 5, fill="red")
        pn = PointF((4 * ps.X - p3.X) / 3, (4 * ps.Y - p3.Y) / 3)
        c.create_oval(pn.X - 5, pn.Y - 5, pn.X + 5, pn.Y + 5, fill="yellow")

        # Рисуем линии
        line1 = c.create_line(p4.X, p4.Y, pn.X, pn.Y, fill="white")
        line2 = c.create_line(p5.X, p5.Y, pn.X, pn.Y, fill="white")
        line3 = c.create_line(p4.X, p4.Y, p5.X, p5.Y, fill="white")

        # Добавляем в список всех линий, которые потом удалим в Drawer
        alllines_list.extend([line1, line2, line3])

        # Если не включено полное построение
        if not checkbox_flag.get():
            # Добавляем временные линии, которые потом удалим в Fractal
            buflines_list.extend([line1, line2, line3])

        # Рекурсивно вызываем эту же функцию нужное число раз
        Fractal(p4, pn, p5, iter - 1, buflines_list)
        Fractal(pn, p5, p4, iter - 1, buflines_list)
        Fractal(
            p1,
            p4,
            PointF((2 * p1.X + p3.X) / 3, (2 * p1.Y + p3.Y) / 3),
            iter - 1,
            buflines_list,
        )
        Fractal(
            p5,
            p2,
            PointF((2 * p2.X + p3.X) / 3, (2 * p2.Y + p3.Y) / 3),
            iter - 1,
            buflines_list,
        )

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

    # Распаковка checkbox'а
    checkbox_flag.set(0)
    checkbox = ttk.Checkbutton(
        text="Полное построение", variable=checkbox_flag, onvalue=1, offvalue=0
    )
    checkbox.pack(side=tk.LEFT)
    root.mainloop()


if __name__ == "__main__":
    main()
