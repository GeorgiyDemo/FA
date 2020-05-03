import numpy as np
import random
#Белые - это синие
#Черные - это красные

#Война - это мир
#Свобода - это рабство
#Незнание - это сила

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
        d = {"A" : 0, "B" : 1, "C" : 2, "D": 3, "E":4, "F":5, "G":6 , "H":7,
            "a": 0, "b" : 1, "c" :2, "d" : 3, "e" : 4, "f" : 5, "g" : 6, "h" : 7
        }
        if char in d:
            return d[char]
        else:
            raise ValueError("Нет ключа для полученного char {}".format(char))
    
    @staticmethod
    def checkxy_value(part):
        """Проверка на корректные на координаты xy"""
        if type(part) != str or len(part) != 2:
            return False

        l1 = ["A", "B", "C", "D", "E", "F", "G", "H", "a","b", "c", "d", "e", "f", "g", "h"]
        l2 = list(map(str, range(1,9)))
        if part[0] in l1 and part[1] in l2:
            return True
        return False

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

class AnalyserClass:
    """Класс ограничений и выявление некорректного хода"""
    def __init__(self, command_dict, board_obj):
        
        self.boolean_result = False
        self.results_list = []
        self.command_dict = command_dict
        self.board_obj = board_obj

        self.fugure_detector()
        self.backstep_detector()
        self.diagonal_detector()
        self.fieldtype_detector()
        if command_dict["mode"] == "war":
            self.war_detector()
        
        print(self.results_list)

        if all(self.results_list):
            self.boolean_result = True

    def fugure_detector(self):
        """Определение, стоит ли на исходной клетке фигура и если стоит, то своя ли"""
        
        board_obj = self.board_obj
        d = self.command_dict

        #Проверка на то, существует ли ячейка, с которой мы хотим переставить фигуру
        target_x = d["from"]["x"]
        target_y = UtilClass.char2xint(d["from"]["y"])
        if not board_obj.detect_element(target_x, target_y):
            self.results_list.append(False)
            return
        
        #Если есть фигура и ее цвет тот, за который мы играем
        selected_field = board_obj.board[target_x][target_y]
        if not selected_field.isfree() and selected_field.figure_obj.color == d["user_color"]:
            self.results_list.append(True)
        else:
            self.results_list.append(False)

    def backstep_detector(self):
        """Проверка на перемещение вперед"""
        d = self.command_dict
        if d["from"]["x"] > d["to"]["x"]:
            self.results_list.append(False)
        else:
            self.results_list.append(True)

    def diagonal_detector(self):
        """Проверка на осуществление перехода по диагонали"""
        #Возможные пути, куда может пойти шашка (их всего 4)
        board_obj = self.board_obj
        d = self.command_dict
        target_x = d["from"]["x"]
        target_y = UtilClass.char2xint(d["from"]["y"])
        #Возможные клетки, куда можно пойти и которые есть на доске

        #Т.к. использование "коротких" перемещений при атаке просто невозможно
        if d["mode"] == "war":
            allowedfields_list = [[target_x+2,target_y+2], [target_x+2,target_y-2]]
        #При тихом ходе возмодны только короткие перемещения
        else:
            allowedfields_list = [[target_x+1,target_y+1], [target_x+1,target_y-1]]
        
        validated_points = [e for e in allowedfields_list if board_obj.detect_element(*e)]

        if [d["to"]["x"], UtilClass.char2xint(d["to"]["y"])] in validated_points:
            self.results_list.append(True)
        else:
            self.results_list.append(False)    
        
        #self.board_obj.board[x][y].figure_obj = FigureClass("TEST", x, y)

    def fieldtype_detector(self):
        """
        Проверка на все, что связано с ячейкой.
        - Проверка на существование ячейки
        - Занятость ячейки
        - Цвет ячейки
        """

        #Понятное дело, что мы ячейку на существование проверили на предыдущем шаге в diagonal_detector, но МАЛО ЛИ
        d = self.command_dict
        board_obj = self.board_obj
        x = d["to"]["x"]
        y = UtilClass.char2xint(d["to"]["y"])
        if not board_obj.detect_element(x,y):
            self.results_list.append(False)
            return

        selected_field = board_obj.board[x][y]
        if selected_field.color == "black" and selected_field.isfree():
            self.results_list.append(True)
        else:
            self.results_list.append(False)

    def war_detector(self):
        """
        Проверка на осуществление перехода с боем
        - Проверка на то, чтоб была фигура, которую мы атакуем
        - Поиск и установление координат фигуры, выставление в self.command_dict
        - Проверка на то, чтоб цвет фигуры был не наш
        """
        d = self.command_dict
        board_obj = self.board_obj

        x_start = d["from"]["x"]
        y_start = UtilClass.char2xint(d["from"]["y"])

        x_finish = d["to"]["x"]
        y_finish = UtilClass.char2xint(d["to"]["y"])
        
        #Соседние точки относительно точки назначения
        middle_points = np.array([e for e in [[x_finish-1,y_finish-1], [x_finish-1,y_finish+1]] if board_obj.detect_element(*e)])


        #Возможные точки, где стоит фигура
        validated_points = np.array([e for e in [[x_start+1,y_start+1], [x_start+1,y_start-1]] if board_obj.detect_element(*e)])

        attack_points = []
        for i in np.arange(middle_points.shape[0]):
            for j in np.arange(validated_points.shape[0]):
                if middle_points[i][0] == validated_points[j][0] and middle_points[i][1] == validated_points[j][1]:
                    attack_points = middle_points[i]
                    break

        #Если нет точек пересечения
        if len(attack_points) == 0:
            self.results_list.append(False)
            return

        self.command_dict["enemy"] = {}
        self.command_dict["enemy"]["x"], self.command_dict["enemy"]["y"] = attack_points
        attack_x, attack_y = attack_points

        #Выбрали точку, где располагается предполагаемый враг
        attack_field = board_obj.board[attack_x][attack_y]
        #Если есть чужая фигура на этой точке
        if not attack_field.isfree() and attack_field.figure_obj.color != d["user_color"]:
            self.results_list.append(True)
        else:
            self.results_list.append(False)

#TODO
class GameOverClass:
    """Класс определения окончания игры"""
    def __init__(self, board):
        self.result = False
        self.board = board

        self.queen_detector()
        self.nofigures_detector()
        self.deadlock_detector()
    
    def queen_detector(self):
        """Определение прохода шашки одного из игроков в дамки"""
        pass

    def nofigures_detector(self):
        """Определение того, что у одного из игроков больше нет фигур"""
        pass

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
        usercolor = input("Выберите цвет шашек:\n1. Белый (по умолчанию)\n2. Черный\n-> ")
        self.usercolor = "black" if usercolor == "2" else "white"
        
        generator_mode = input("Введите способ генерации шашек на доске:\n1. Ручная расстановка, 6 фигур (по умолчанию)\n2. Стандартная авторасстановка, 12 фигур\n-> ")
        board_obj = BoardClass(2, self.usercolor) if generator_mode == "2" else BoardClass(1, self.usercolor)
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

        command_dict = {"from": {}, "to": {}, "mode": movement_type_dict[spliter], "user_color" : self.usercolor}
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
        print("\033[93m*Игра началась*\033[0m")
        stopgame_flag = True
        while stopgame_flag:
            
            cmd = input("Введите команду -> ")
            result_dict = self.command_parser(cmd)
            
            #Если норально прошло фильтрацию
            if result_dict != {}:
                self.result_dict = result_dict
                #Проверка на все критерии
                obj = AnalyserClass(result_dict, self.board_obj)
                #Если все хорошо, то осуществлем ход
                if obj.boolean_result:
                    self.result_dict = obj.command_dict
                    #Пользователь ходит
                    self.user_mode()
                    #Компьютер ходит
                    self.computer_mode()

            #Проверяем на окончание игры
            obj = GameOverClass(self.board_obj.board)
            if obj.result:
                stopgame_flag = False

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
    
    #TODO
    def computer_mode(self):
        """Осуществление хода компьютером"""
        pass

if __name__ == "__main__":
    MainClass()