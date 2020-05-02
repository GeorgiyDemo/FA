import numpy as np
import random
#Матрица Nnumpy с объектами Field - это идеально!

class UtilClass:
    """Класс со всякой фигней"""
    @staticmethod
    def xint2char(xint):
        """Конвертирование числа в букву"""
        d = {0:"A",1:"B", 2:"C", 3:"D", 4:"E", 5: "F", 6: "G", 7: "H"}
        
        if xint in d:
            return d[xint]
        else:
            raise ValueError("Нет ключа для полученного xint {}".format(xint))
     
    @staticmethod
    def char2xint(char):
        """Конвертирование буквы в число"""
        d = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E":4, "F":5, "G":6 , "H":7}
        if char in d:
            return d[char]
        else:
            raise ValueError("Нет ключа для полученного char {}".format(char))
     
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
    def __init__(self, coord_x, coord_y, figure_obj=None):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.figure_obj = figure_obj
        self.color_generator()
    
    def color_generator(self):
        """Генератор цвета ячейки на основе ее координат"""
        x = UtilClass.char2xint(self.coord_x)
        y = self.coord_y

        if (x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
            color = "white"
        else:
            color = "black"
        
        self.color = color
    
    def isfree(self):
        """Проверяет, свободна ли текущая ячейка"""
        if self.figure_obj == None:
            return True
        return False

    def __str__(self):
        """Вывод ячейки на экран"""

        color2print_dict = {"black" : "⬛️", "white": "⬜️"}
        #Если ячейка свободная -> выводим просто ее цвет на экран
        if self.isfree:
            return color2print_dict[self.color]
        #Если ячейка занята -> выводим цвет шашки, которую она занимает


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


class BoardClass:
    """Класс игровой доски"""
    def __init__(self):
        self.board = None
        self.creator()

    def creator(self):
        """Создание чистого игрового поля без фигур"""
        xint2char_dict = {0:"A",1:"B", 2:"C", 3:"D", 4:"E", 5: "F", 6: "G", 7: "H"}
        board = np.array([])
        for x in np.arange(8):
            for y in np.arange(8):
                field_obj = FieldClass(UtilClass.xint2char(x), y) 
                board = np.append(field_obj, board)
        

        self.board = np.array(board.reshape(8,8))

        print(board)   
        
        #board.shape
        #board = np.append()



    def __str__(self):
        """Вывод игровой доски не экран"""
        board = self.board
        for i in np.arange(board.shape[0]):
            for j in np.arange(board.shape[1]):
                print('{}'.format(board[i][j]), end="")
            print("")
        return ""

        


if __name__ == "__main__":
    board = BoardClass()
    print(board)