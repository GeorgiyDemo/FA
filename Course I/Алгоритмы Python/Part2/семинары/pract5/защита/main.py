import numpy as np
#Матрица Nnumpy с объектами Field - это идеально!

class FieldClass:
    """
    Класс 1 клетки доски
    Поля:
    - Координата X
    - Координата Y
    - Занята или нет, если занята то кем?
    - Цвет клетки
    - Ссылка на объект фигуры, которая стоит на клетке
    
    Методы:
    - Занятие/резервация клетки фигурой
    - Освобождение клетки фигурой
    """
    def __init__(self, coord_x, coord_y,):
        self.isfree  = True

       #TODO генерация цвета ячейки на основе их кооррдинат?
       pass

class FigureClass:
    """
    Класс фигуры (шашки)
    Поля:
    - Цвет (черный/белый)
    - Координата X
    - Координата Y
    """
    def __init__(self, color, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_x
        self.color = "black"



        def field_reserve(self, fieldclass_obj):
        """
        Занятие клетки фигурой
        - Выставление поля free в False
        """
        pass

    def field_free(self, fieldclass_obj):
        """
        Освобождение клетки фигурой
        """
        pass

