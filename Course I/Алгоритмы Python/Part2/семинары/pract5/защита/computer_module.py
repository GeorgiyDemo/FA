import random

import numpy as np
from user_module import UserAnalyserClass
from util_module import UtilClass


class ComputerAnalyserClass(UserAnalyserClass):
    """
    Класс ограничений и выявление некорректного хода со стороны компьютера
    - figure_detector - у UserAnalyserClass
    - backstep_detector - переписываем
    - diagonal_detector - переписываем
    - war_detector - переписываем
    - fieldtype_detector - у UserAnalyserClass
    """

    def __init__(self, command_dict, board_obj, info=False):

        self.boolean_result = False
        self.results_list = []
        self.command_dict = command_dict
        self.board_obj = board_obj
        self.info = info

        self.figure_detector()
        self.backstep_detector()
        self.diagonal_detector()
        self.fieldtype_detector()
        if command_dict["mode"] == "war":
            self.war_detector()

        if all(self.results_list):
            self.boolean_result = True

    def backstep_detector(self):
        """Проверка на перемещение назад"""
        d = self.command_dict
        if d["from"]["x"] < d["to"]["x"]:
            self.results_list.append(False)
        else:
            self.results_list.append(True)

    def diagonal_detector(self):
        """Проверка на осуществление перехода по диагонали"""
        # Возможные пути, куда может пойти шашка (их всего 4)
        board_obj = self.board_obj
        d = self.command_dict
        target_x = d["from"]["x"]
        target_y = UtilClass.char2xint(d["from"]["y"])
        # Возможные клетки, куда можно пойти и которые есть на доске

        # Т.к. использование "коротких" перемещений при атаке просто невозможно
        if d["mode"] == "war":
            allowedfields_list = [
                [target_x - 2, target_y + 2],
                [target_x - 2, target_y - 2],
            ]
        # При тихом ходе возмодны только короткие перемещения
        else:
            allowedfields_list = [
                [target_x - 1, target_y + 1],
                [target_x - 1, target_y - 1],
            ]

        validated_points = [
            e for e in allowedfields_list if board_obj.detect_element(*e)
        ]

        if [d["to"]["x"], UtilClass.char2xint(d["to"]["y"])] in validated_points:
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

        # Соседние точки относительно точки назначения
        middle_points = np.array(
            [
                e
                for e in [[x_finish + 1, y_finish - 1], [x_finish + 1, y_finish + 1]]
                if board_obj.detect_element(*e)
            ]
        )

        # Возможные точки, где стоит фигура
        validated_points = np.array(
            [
                e
                for e in [[x_start - 1, y_start + 1], [x_start - 1, y_start - 1]]
                if board_obj.detect_element(*e)
            ]
        )

        attack_points = []
        for i in np.arange(middle_points.shape[0]):
            for j in np.arange(validated_points.shape[0]):
                if (
                    middle_points[i][0] == validated_points[j][0]
                    and middle_points[i][1] == validated_points[j][1]
                ):
                    attack_points = middle_points[i]
                    break

        # Если нет точек пересечения
        if len(attack_points) == 0:
            self.results_list.append(False)
            return

        self.command_dict["enemy"] = {}
        self.command_dict["enemy"]["x"], self.command_dict["enemy"]["y"] = attack_points
        attack_x, attack_y = attack_points

        # Выбрали точку, где располагается предполагаемый враг
        attack_field = board_obj.board[attack_x][attack_y]
        # Если есть чужая фигура на этой точке
        if (
            not attack_field.isfree()
            and attack_field.figure_obj.color != d["user_color"]
        ):
            self.results_list.append(True)
        else:
            self.results_list.append(False)


class ComputerGameClass:
    """
    Класс с основной логикой автоматического хода компьютера
    - Суть заключается просто в рандомном генерировани словаря dict относительно своих фигур по типу
      {'from': {'x': 2, 'y': 'c'}, 'to': {'x': 3, 'y': 'b'}, 'mode': 'peace', 'user_color': 'black'}
    """

    def __init__(self, board_obj, user_color):
        # Используется для контроля тупикового хода со стороны компьютера
        self.result = True
        # Статистика шагов
        self.result_dict = {}

        self.board_obj = board_obj
        self.user_color = user_color
        self.processing()

    def processing(self):
        uc = self.user_color
        # Цвет, за который ходит компьютер
        reverse_uc = "black" if uc == "white" else "white"
        myfields_arr = np.array([])
        all_d = []
        board = self.board_obj.board

        for i in np.arange(board.shape[0]):
            for j in np.arange(board.shape[1]):
                if (
                    not board[i][j].isfree()
                    and board[i][j].figure_obj.color == reverse_uc
                ):
                    myfields_arr = np.append(myfields_arr, board[i][j])

        # Для каждой шашки формируем возможные новые координаты, перемешиваем это и закидываем в ComputerAnalyserClass
        for field in myfields_arr:

            x, y = field.figure_obj.coord_x, field.figure_obj.coord_y
            y_char = UtilClass.xint2char(y)

            # Возможные короткие шаги
            # [x-1,y-1]
            if self.board_obj.detect_element(y - 1, x - 1):
                new_y, new_x = UtilClass.xint2char(y - 1), x - 1
                all_d.append(
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "peace",
                        "user_color": reverse_uc,
                    }
                )

            # [x-1,y+1]
            if self.board_obj.detect_element(y + 1, x - 1):
                new_y, new_x = UtilClass.xint2char(y + 1), x - 1
                all_d.append(
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "peace",
                        "user_color": reverse_uc,
                    }
                )

            # Длинные шаги
            # [x-2,y+2]
            if self.board_obj.detect_element(y + 2, x - 2):
                new_y, new_x = UtilClass.xint2char(y + 2), x - 2
                all_d.append(
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "war",
                        "user_color": reverse_uc,
                    }
                )

            # [x-2,y-2]
            if self.board_obj.detect_element(y - 2, x - 2):
                new_y, new_x = UtilClass.xint2char(y - 2), x - 2
                all_d.append(
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "war",
                        "user_color": reverse_uc,
                    }
                )

        random.shuffle(all_d)
        all_d.sort(key=lambda x: x["mode"], reverse=True)

        for d in all_d:
            obj = ComputerAnalyserClass(d, self.board_obj)
            if obj.boolean_result:
                self.result_dict = obj.command_dict
                self.computer_mode()
                break
        else:
            self.result = False

    def computer_mode(self):
        """
        Осуществление хода компьютера
        - Выбираются координаты ячейки из сформированного словаря
        - Берется объект фигуры, меняются координаты фигуры на обновлённые
        - Осуществляется привязка к новой ячейке фигуры
        - Из старой ячейки освобождается объект фигуры

        - Если осуществилась атака, то удаляем фигуру врага из ячейки enemy
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

        figure_obj = field_from.figure_obj
        figure_obj.coord_x, figure_obj.coord_y = f2

        # Присваиваем фигуру обновленной ячейке
        field_to.field_reserve(figure_obj)
        # Освобождаем из старой
        field_from.field_free()

        # Если мы кого-то бъём, то удаляем фигуру с той ячейки
        if mode == "war":
            attack_x, attack_y = d["enemy"]["x"], d["enemy"]["y"]
            board[attack_x][attack_y].field_free()

        self.board_obj.board = board
