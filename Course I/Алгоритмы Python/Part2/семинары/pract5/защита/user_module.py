from util_module import UtilClass
import numpy as np

class UserAnalyserClass:
    """Класс ограничений и выявление некорректного хода"""
    def __init__(self, command_dict, board_obj):
        
        self.boolean_result = False
        self.results_list = []
        self.command_dict = command_dict
        self.board_obj = board_obj

        self.figure_detector()
        self.backstep_detector()
        self.diagonal_detector()
        self.fieldtype_detector()
        if command_dict["mode"] == "war":
            self.war_detector()
        
        print(self.results_list)

        if all(self.results_list):
            self.boolean_result = True

    def figure_detector(self):
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
        #При тихом ходе возможны только короткие перемещения
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