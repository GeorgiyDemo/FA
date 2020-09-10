import tkinter as tk
import math


def calculate_position(data):
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


def move_object(object_id, data):
    """Перемещение объекта"""
    # Вычисление координат овала
    x1, y1, x2, y2 = calculate_position(data)

    # Перемещение овала
    c.coords(object_id, x1, y1, x2, y2)


def animate():
    # перемещение точки - угол += угловая скорость
    point_figure[4] += point_figure[5]
    move_object(e_id, point_figure)

    # анимация
    root.after(1, animate)


if __name__ == "__main__":

    WIDTH = 600
    HEIGHT = 600
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # [центр x и y, радиус, расстояние от центра, текущий угол, угловая скорость]
    # Начальные координаты двух объектов
    main_figure = [center_x, center_y, 200, 0, 0, 0]
    point_figure = [center_x, center_y, 10, 200, 0, 1]

    root = tk.Tk()

    c = tk.Canvas(root, width=WIDTH, heigh=HEIGHT)
    c.pack()

    # Создание объектов
    x1, y1, x2, y2 = calculate_position(main_figure)
    s_id = c.create_oval(x1, y1, x2, y2, fill="red")
    x1, y1, x2, y2 = calculate_position(point_figure)
    e_id = c.create_oval(x1, y1, x2, y2, fill="black")
    animate()
    root.mainloop()
