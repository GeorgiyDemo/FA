import numpy as np
import random
import time
from util_module import UtilClass
from user_module import UserAnalyserClass 
from computer_module import ComputerGameClass
#Белые - это синие
#Черные - это красные

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
            color = "black"
        else:
            color = "white"
        
        self.color = color
    
    def isfree(self):
        """Проверяет, свободна ли текущая ячейка"""
        if self.figure_obj == None:
            return True
        return False

    def field_reserve(self, figure_obj):
        """
        Занятие клетки фигурой
        """
        self.figure_obj = figure_obj

    def field_free(self):
        """
        Освобождение клетки фигурой
        """
        self.figure_obj = None

    def __str__(self):
        """Вывод ячейки на экран"""
        board_color2print_dict = {"black" : "⬛️", "white": "⬜️"}
        # figure_color2print_dict = {"black" : "🔴", "white": "🔵", "TEST" : "🍺"}
        figure_color2print_dict = {"black" : "👹", "white": "🍺", "TEST" : "💩"}
        #Если ячейка свободная -> выводим просто ее цвет на экран
        if self.isfree():
            return board_color2print_dict[self.color]
        #Если ячейка занята -> выводим цвет шашки, которую она занимает
        return figure_color2print_dict[self.figure_obj.color]

class FigureClass:
    """
    Класс фигуры (шашки)
    Поля:
    - Координата X
    - Координата Y
    - Цвет (черный/белый) генерится автоматически
    """
    def __init__(self, color, coord_x, coord_y):
        self.color = color
        self.coord_x = coord_x
        self.coord_y = coord_x

class BoardClass:
    """Класс игровой доски"""
    def __init__(self, generator_way, user_color):

        self.user_color = user_color
        figuregenerator_dict = {
            1 : self.figuremanual_generator,
            2 : self.figureauto_generator,
        }
        self.board = None
        self.board_generator()

        if generator_way in figuregenerator_dict:
            figuregenerator_dict[generator_way]()
        else:
            raise ValueError("Нет запрашиваемого метода расстановки фигур {}!".format(generator_way))

    def board_generator(self):
        """Создание чистого игрового поля без фигур"""

        board = np.array([])
        for x in np.arange(8):
            for y in np.arange(8):
                field_obj = FieldClass(UtilClass.xint2char(x), y) 
                board = np.append(field_obj, board)
        self.board = np.array(board.reshape(8,8))

    def detect_element(self, search_x, search_y):
        """
        Определяем, есть ли элемент с такими координатами на доске
        Это необходимо для того, чтоб не выехать за массив
        """
        search_x = UtilClass.xint2char(search_x)
        board = self.board
        for x in np.arange(8):
            for y in np.arange(8):
                if board[x][y].coord_x == search_x and board[x][y].coord_y == search_y:
                    return True
        return False

    def figureauto_generator(self):
        """Автоматическая расстановка 12 фигур по полю"""
        uc = self.user_color
        reverse_uc = "black" if uc == "white" else "white"

        board = self.board
        for x in np.arange(8):
            for y in np.arange(8):
                if x < 3 and ((x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    board[x][y].field_reserve(FigureClass(uc, x, y))
                elif x > 4 and ((x % 2 == 0 and y % 2 == 0) or (y % 2 == 1 and x % 2 == 1)):
                    board[x][y].field_reserve(FigureClass(reverse_uc, x, y))
        self.board = board

    def boardfigure_setter(self, color, search_x, search_y):
        """
        Поиск координат фигуры и ее постановка
        Возврат True - фигура поставлена
        Возврат False - фигура с координатами не найдена
        """
        x = search_x
        y = UtilClass.char2xint(search_y)
        board = self.board

        if board[x][y].isfree() and board[x][y].color == "black":
            board[x][y].field_reserve(FigureClass(color, x,y))
            self.board = board
            return True
        return False

    def figuremanual_generator(self):

        """Ручная расстановка 6 фигур по полю"""
        format_dict = {"white" : "белого", "black":"чёрного"}
        for color in ("white", "black"):
            print("\033[93m*Выставляем шашки {} цвета*\033[0m".format(format_dict[color]))
            for i in range(5):
                
                boolean_flag = True
                while boolean_flag:
                    print(self)
                    coord_input = input("Введите координаты расположения шашки №{} -> ".format(i+1))
                    if UtilClass.checkxy_value(coord_input):
                        coord_x = int(coord_input[1])-1
                        coord_y = coord_input[0]
                        result = self.boardfigure_setter(color, coord_x, coord_y)
                        if result:
                            print("Успешная постановка шашки на координаты ")
                            boolean_flag = False
                        else:
                            print("Некорретный ввод координат!")
                    else: 
                        print("Некорретный ввод данных, пример координат: h2")


    def __str__(self):
        """Вывод игровой доски не экран"""
        board = self.board
        for i in np.arange(board.shape[0]-1,-1,-1):
            print("{}".format(i+1), end="")
            for j in np.arange(board.shape[1]):
                print('{}'.format(board[i][j]), end="")
            print("")
        print("  A B C D E F G H")
        return ""


class GameOverClass:
    """Класс определения окончания игры"""
    def __init__(self, board, user_color):
        self.result = False
        self.won_color = ""
        self.user_color = user_color
        self.board = board

        #На одной итерации может сработать только один из этих методов (не путать с логикой работы UserAnalyserClass)
        self.queen_detector()
        self.nofigures_detector()
        self.deadlock_detector()
    
    def queen_detector(self):
        """Определение прохода шашки одного из игроков в дамки"""
        board = self.board
        
        uc = self.user_color
        reverse_uc = "black" if uc == "white" else "white"

        for i in np.arange(board.shape[0]):
            if not board[0][i].isfree() and board[0][i].figure_obj.color == reverse_uc:
                self.result = True
                self.won_color = reverse_uc
                break
        
        for i in np.arange(board.shape[0]):
            if not board[7][i].isfree() and board[7][i].figure_obj.color == uc:
                self.result = True
                self.won_color = uc
                break


    def nofigures_detector(self):
        """Определение того, что у одного из игроков больше нет фигур"""
        board = self.board
        black_count, white_count = 0, 0
        for i in np.arange(8):
            for j in np.arange(8):
                if not board[i][j].isfree() and board[i][j].figure_obj.color == "black":
                    black_count += 1
                elif not board[i][j].isfree() and board[i][j].figure_obj.color == "white":
                    white_count += 1
        
        if white_count == 0:
            self.result = True
            self.won_color = "black"

        if black_count == 0:
            self.result = True
            self.won_color = "white"   

    #TODO ?????
    def deadlock_detector(self):
        """
        Определение тупиковой ситуации
        Использует логику, аналогичную рандомному ходу компьютера
        """
        pass

class MainClass:
    """Управляющий класс с логикой игры"""
    def __init__(self):
        #Создаем доску
        user_color = input("Выберите цвет шашек:\n1. Белый (по умолчанию)\n2. Черный\n-> ")
        self.user_color = "black" if user_color == "2" else "white"
        
        generator_mode = input("Введите способ генерации шашек на доске:\n1. Ручная расстановка, 6 фигур (по умолчанию)\n2. Стандартная авторасстановка, 12 фигур\n-> ")
        board_obj = BoardClass(2, self.user_color) if generator_mode == "2" else BoardClass(1, self.user_color)
        print(board_obj)

        #board_obj.board[3][3].figure_obj = FigureClass("TEST", 3, 3)

        self.board_obj = board_obj
        self.gameprocess()

    def command_parser(self, cmd):
        """
        Осуществление парсинга и фильтрации команды, которую ввел пользователь
        Если все хорошо - вызывается проверка на уровне
        """

        movement_type_dict = {":" : "war", "-" : "peace"}
        #Разделитель строки на 2 части
        spliter = ""
        detect_flag = False
        for key in movement_type_dict.keys():
            if key in cmd:
                detect_flag = True
                spliter = key
                break
        
        if not detect_flag:
            print("Не найден разделитель комманд! ':' - перемещение с боем, '-' - тихое перемещение")
            return {}

        command_dict = {"from": {}, "to": {}, "mode": movement_type_dict[spliter], "user_color" : self.user_color}
        #Разделяем введенную команду на 2 части
        part1, part2 = cmd.split(spliter)
        if UtilClass.checkxy_value(part1) and UtilClass.checkxy_value(part2):
            command_dict["from"]["x"] = int(part1[1])-1
            command_dict["from"]["y"] = part1[0]
            command_dict["to"]["x"] = int(part2[1])-1
            command_dict["to"]["y"] = part2[0]
            return command_dict

        print("Некорректный ввод данных!")
        return {}

        
    def gameprocess(self):
        """Управляющая логика работы игры"""
        
        #Номер итерации
        i = 0
        print("\033[93m*Игра началась*\033[0m")
        stopgame_flag = True
        while stopgame_flag:

            #Ходит пользователь
            if i % 2 == 0:
                print("Ход №{}. Ходит пользователь".format(i+1))
                cmd = input("Введите команду -> ")
                result_dict = self.command_parser(cmd)
                
                #Если норально прошло фильтрацию
                if result_dict != {}:
                    self.result_dict = result_dict
                    #Проверка на все критерии
                    obj = UserAnalyserClass(result_dict, self.board_obj)
                    #Если все хорошо, то осуществлем ход
                    if obj.boolean_result:
                        self.result_dict = obj.command_dict
                        #Пользователь ходит
                        self.user_mode()
                        i+=1
            
            #Компьютер ходит
            else:
                print("Ход №{}. Ходит компьютер".format(i+1))
                computergame_obj = ComputerGameClass(self.board_obj.board, self.user_color)
                #Если тупиковый ход со стороны компьютера
                if computergame_obj.result:
                    stopgame_flag = False
                i+=1

            #Проверяем на окончание игры
            obj = GameOverClass(self.board_obj.board, self.user_color)
            if obj.result:
                stopgame_flag = False
                print("Выиграл цвет: {}".format(obj.won_color))

            #Вывод доски
            print(self.board_obj)
    
    def user_mode(self):
        """
        Осуществление хода пользователем
        """
        d = self.result_dict
        board = self.board_obj.board
        
        mode = d["mode"]
        f1 = [d["from"]["x"], UtilClass.char2xint(d["from"]["y"])]
        f2 = [d["to"]["x"], UtilClass.char2xint(d["to"]["y"])]
        x1, y1 = f1
        x2, y2 = f2
        field_from = board[x1][y1]
        field_to = board[x2][y2]

        #Получаем объект фигуры с ячейки и выставлем для него обновленные координаты
        figure_obj = field_from.figure_obj
        figure_obj.coord_x, figure_obj.coord_y = f2

        #Присваиваем фигуру обновленной ячейке
        field_to.field_reserve(figure_obj)
        #Освобождаем из старой
        field_from.field_free()

        #Если мы кого-то бъём, то удаляем фигуру с той ячейки
        if mode == "war":
            attack_x, attack_y = d["enemy"]["x"], d["enemy"]["y"]
            board[attack_x][attack_y].field_free()

        self.board_obj.board = board

if __name__ == "__main__":
    MainClass()