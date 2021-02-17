"""
Практика 2 Суперэллипс
Деменчук Георгий ПИ19-4
"""

import tkinter as tk
from math import sin, cos, pi

# Начальные позиции
width = 600
height = 600
root = tk.Tk()
# Основной канвас
c = tk.Canvas(root, width=width, heigh=height)
# Текущие точки, которые отрисованы
points_list = []


def drawer(canvas, x, y, a, b):
    """Создание точки"""

    # Смещение, чтоб относительно центра
    x = a + x
    y = b + y

    x1, y1 = (x - 1), (y - 1)
    x2, y2 = (x + 1), (y + 1)

    point = canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")

    # Добавляем точку в список точек
    points_list.append(point)


def sign(x):
    """Отдача знака для processing"""
    return ((x > 0) - (x < 0)) * 1


def processing(canvas, n):
    """Метод отрисовки суперэллипса"""

    a, b = width // 2, height // 2
    na = 2 / n

    # шаг отрисовки точек-овалов. если лагает - исправить на меньший коэфф
    step = 1000
    piece = (pi * 2) / step
    xp = []
    yp = []

    t = 0
    for _ in range(step + 1):

        # т.к sin ^ n(x)  математически это то же самое, что (sin(x))^n...
        x = (abs((cos(t))) ** na) * a * sign(cos(t))
        y = (abs((sin(t))) ** na) * b * sign(sin(t))
        xp.append(x)
        yp.append(y)
        t += piece

    if len(xp) == len(yp):
        for i in range(len(xp)):
            drawer(canvas, xp[i], yp[i], a, b)
    else:
        raise ValueError("Точки x и y не совпадают")


def scale_processing(number):
    """Обработка ползунка"""

    # Удаляем предыдущие точки, если они есть
    if len(points_list) != 0:
        for point in points_list:
            c.delete(point)

    # Отрисовываем эллипс
    processing(c, float(number))


def main():

    root.title("Суперэллипс")

    # Распаковка канваса
    c.configure(bg="black")
    c.pack(fill=tk.BOTH, expand=1)

    # Распаковка ползунка
    scale = tk.Scale(
        root,
        from_=0.01,
        to=3.75,
        digits=3,
        resolution=0.01,
        command=scale_processing,
        orient=tk.HORIZONTAL,
    )
    scale.pack(side=tk.LEFT, padx=5)

    root.mainloop()


if __name__ == "__main__":
    main()
