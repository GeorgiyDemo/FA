import numpy as np
import time
from util_module import UtilClass
from user_module import UserAnalyserClass 
from computer_module import ComputerGameClass
from elements_module import FieldClass, FigureClass, BoardClass

#TODO При ручной настройке заносить инфо о фигуре
#Белые - это синие
#Черные - это красные

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

        for i in np.arange(board.shape[1]):
            if not board[0][i].isfree() and board[0][i].figure_obj.color == reverse_uc:
                self.result = True
                self.won_color = reverse_uc
                break
        
        for i in np.arange(board.shape[1]):
            if not board[7][i].isfree() and board[7][i].figure_obj.color == uc:
                self.result = True
                self.won_color = uc
                break


    def nofigures_detector(self):
        """Определение того, что у одного из игроков больше нет фигур"""
        board = self.board
        black_count, white_count = 0, 0
        for i in np.arange(board.shape[0]):
            for j in np.arange(board.shape[1]):
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
            if i % 2 == 1:
                print("Ход №{}. Ходит пользователь".format(i+1))
                cmd = input("Введите команду -> ")
                result_dict = self.command_parser(cmd)
                
                #Если норально прошло фильтрацию
                if result_dict != {}:
                    self.result_dict = result_dict
                    #Проверка на все критерии
                    print(result_dict)
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
                computergame_obj = ComputerGameClass(self.board_obj, self.user_color)
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