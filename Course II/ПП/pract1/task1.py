import tkinter as tk
import math


def obj_mover(object_id, data):
    """Перемещение объекта"""
    # Вычисление координат овала
    x1, y1, x2, y2 = position_calc(data)
    # Перемещение овала
    c.coords(object_id, x1, y1, x2, y2)


def animator():
    """Анимирование"""
    # перемещение точки - угол += угловая скорость
    point_figure[4] += point_figure[5]
    obj_mover(e_id, point_figure)

    # анимация в 1мс
    root.after(1, animator)


def position_calc(data):
    """Высчитывание новой позиции объекта"""
    # Получаем данные

    center_x, center_y, radius, distance, angle, angle_speed = data

    # Вычисление новой позиции объекта
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))

    # Вычисление координат овала
    x1 = x - radius
    y1 = y - radius
    x2 = x + radius
    y2 = y + radius

    return x1, y1, x2, y2


if __name__ == "__main__":

    width = 600
    height = 600
    center_x = width // 2
    center_y = height // 2

    # [центр x, центр y, радиус, расстояние от центра, текущий угол, угловая скорость]
    main_figure = [center_x, center_y, 200, 0, 0, 0]
    point_figure = [center_x, center_y, 10, 200, 0, 1]

    root = tk.Tk()
    c = tk.Canvas(root, width=width, heigh=height)
    c.pack()

    # Создание объектов
    x1, y1, x2, y2 = position_calc(main_figure)
    s_id = c.create_oval(x1, y1, x2, y2, fill="red")
    x1, y1, x2, y2 = position_calc(point_figure)
    e_id = c.create_oval(x1, y1, x2, y2, fill="black")

    animator()
    root.mainloop()
