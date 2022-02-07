import time

import numpy as np
from computer_module import ComputerGameClass
from elements_module import BoardClass
from user_module import UserAnalyserClass
from util_module import UtilClass


# Белые - это синие
# Черные - это красные
class JournalWriterClass:
    """Класс для записи данных о ходах каждого участника и формирования отчетов"""

    def __init__(self, user_color="white"):
        self.journal_arr = np.array([])
        self.bufstr = ""

    def add_result(self, d):
        """Метод для добавления данных хода"""

        journal = self.journal_arr
        if self.bufstr == "" and d["user_color"] == "black":
            raise ValueError("Белые всегда начинают ходить первые")

        movementtype_dict = {"war": ":", "peace": "-"}
        locale_str = (
            d["from"]["y"].lower()
            + str(d["from"]["x"] + 1)
            + movementtype_dict[d["mode"]]
            + d["to"]["y"].lower()
            + str(d["to"]["x"] + 1)
        )
        if self.bufstr == "":
            self.bufstr = locale_str

        else:
            self.journal_arr = np.append(journal, self.bufstr + " " + locale_str)
            self.bufstr = ""

    def winlose_add(self, win_color):
        """Добавление результатов игры"""

        # Если у черных нет больше ходов и игра завершена (т.е. у кого-то больше нет вариантов, как пойти)
        journal = self.journal_arr
        if self.bufstr != "":
            self.journal_arr = np.append(journal, self.bufstr + "X")

        # Иначе работаем с последним элементом массива
        else:
            e = journal[-1]
            white, black = e.split(" ")
            if win_color == "white":
                white += "X"
            else:
                black += "X"
            self.journal_arr[-1] = white + " " + black

    def __str__(self):
        """Информация о записанном"""
        return "\033[93mЗапись ходов:\033[0m\n" + "\n".join(
            [
                str(i + 1) + ". " + self.journal_arr[i]
                for i in np.arange(self.journal_arr.shape[0])
            ]
        )


class GameOverClass:
    """Класс определения окончания игры"""

    def __init__(self, board_obj, user_color):
        self.result = False
        self.won_color = ""
        self.user_color = user_color
        self.board_obj = board_obj

        # На одной итерации может сработать только один из этих методов (не путать с логикой работы UserAnalyserClass)
        self.queen_detector()
        self.nofigures_detector()
        self.deadlock_detector()

    def queen_detector(self):
        """Определение прохода шашки одного из игроков в дамки"""
        board = self.board_obj.board

        uc = self.user_color
        reverse_uc = "black" if uc == "white" else "white"

        for i in np.arange(board.shape[1]):
            if not board[0][i].isfree() and board[0][i].figure_obj.color == reverse_uc:
                self.result = True
                self.won_color = reverse_uc
                print("\033[93m[ИНФО]\033[0m Шашка прошла в дамки")
                break

        for i in np.arange(board.shape[1]):
            if not board[7][i].isfree() and board[7][i].figure_obj.color == uc:
                self.result = True
                self.won_color = uc
                print("\033[93m[ИНФО]\033[0m Шашка прошла в дамки")
                break

    def nofigures_detector(self):
        """Определение того, что у одного из игроков больше нет фигур"""
        board = self.board_obj.board
        black_count, white_count = 0, 0
        for i in np.arange(board.shape[0]):
            for j in np.arange(board.shape[1]):
                if not board[i][j].isfree() and board[i][j].figure_obj.color == "black":
                    black_count += 1
                elif (
                    not board[i][j].isfree() and board[i][j].figure_obj.color == "white"
                ):
                    white_count += 1

        if white_count == 0:
            self.result = True
            self.won_color = "black"
            print("\033[93m[ИНФО]\033[0m Белых шашек больше нет на поле")

        if black_count == 0:
            self.result = True
            self.won_color = "white"
            print("\033[93m[ИНФО]\033[0m Черных шашек больше нет на поле")

    def deadlock_detector(self):
        """
        Определение тупиковой ситуации для пользователя
        Использует логику, аналогичную рандомному ходу компьютера
        """
        board_obj = self.board_obj
        board = board_obj.board

        uc = self.user_color
        reverse_uc = "black" if uc == "white" else "white"

        all_d = np.array([])
        myfields_arr = np.array([])
        # Ищем все фигуры пользователя
        for i in np.arange(board.shape[0]):
            for j in np.arange(board.shape[1]):
                if not board[i][j].isfree() and board[i][j].figure_obj.color == uc:
                    myfields_arr = np.append(myfields_arr, board[i][j])

        # Для каждой шашки формируем возможные новые координаты:
        for field in myfields_arr:

            x, y = field.figure_obj.coord_x, field.figure_obj.coord_y
            y_char = UtilClass.xint2char(y)

            # Возможные короткие шаги
            # [x+1,y-1]
            if board_obj.detect_element(y - 1, x + 1):
                new_y, new_x = UtilClass.xint2char(y - 1), x + 1
                all_d = np.append(
                    all_d,
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "peace",
                        "user_color": uc,
                    },
                )

            # [x+1,y+1]
            if board_obj.detect_element(y + 1, x + 1):
                new_y, new_x = UtilClass.xint2char(y + 1), x + 1
                all_d = np.append(
                    all_d,
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "peace",
                        "user_color": uc,
                    },
                )

            # Длинные шаги
            # [x+2,y+2]
            if board_obj.detect_element(y + 2, x + 2):
                new_y, new_x = UtilClass.xint2char(y + 2), x + 2
                all_d = np.append(
                    all_d,
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "war",
                        "user_color": uc,
                    },
                )

            # [x+2,y-2]
            if board_obj.detect_element(y - 2, x + 2):
                new_y, new_x = UtilClass.xint2char(y - 2), x + 2
                all_d = np.append(
                    all_d,
                    {
                        "from": {"x": x, "y": y_char},
                        "to": {"x": new_x, "y": new_y},
                        "mode": "war",
                        "user_color": uc,
                    },
                )

        # Перебираем все возможные ходы пользователя
        for d in all_d:
            obj = UserAnalyserClass(d, self.board_obj)
            if obj.boolean_result:
                break

        else:
            self.result = True
            self.won_color = reverse_uc
            print("\033[91m[ИНФО]\033[0m У пользователя тупиковая ситуация")


class MainClass:
    """Управляющий класс с логикой игры"""

    def __init__(self):
        # Создаем доску
        user_color = input(
            "Выберите цвет шашек:\n1. Белый (по умолчанию)\n2. Черный\n-> "
        )
        self.user_color = "black" if user_color == "2" else "white"

        generator_mode = input(
            "Введите способ генерации шашек на доске:\n1. Ручная расстановка, 6 фигур (по умолчанию)\n2. Стандартная авторасстановка, 12 фигур\n-> "
        )
        board_obj = (
            BoardClass(2, self.user_color)
            if generator_mode == "2"
            else BoardClass(1, self.user_color)
        )
        print(board_obj)

        # board_obj.board[3][3].figure_obj = FigureClass("TEST", 3, 3)

        self.board_obj = board_obj
        self.gameprocess()

    def command_parser(self, cmd):
        """
        Осуществление парсинга и фильтрации команды, которую ввел пользователь
        Если все хорошо - вызывается проверка на уровне
        """

        movement_type_dict = {":": "war", "-": "peace"}
        # Разделитель строки на 2 части
        spliter = ""
        detect_flag = False
        for key in movement_type_dict.keys():
            if key in cmd:
                detect_flag = True
                spliter = key
                break

        if not detect_flag:
            return {}

        command_dict = {
            "from": {},
            "to": {},
            "mode": movement_type_dict[spliter],
            "user_color": self.user_color,
        }
        # Разделяем введенную команду на 2 части
        part1, part2 = cmd.split(spliter)
        if UtilClass.checkxy_value(part1) and UtilClass.checkxy_value(part2):
            command_dict["from"]["x"] = int(part1[1]) - 1
            command_dict["from"]["y"] = part1[0]
            command_dict["to"]["x"] = int(part2[1]) - 1
            command_dict["to"]["y"] = part2[0]
            return command_dict

        return {}

    def gameprocess(self):
        """Управляющая логика работы игры"""
        userstepcolor_dict = {"black": 1, "white": 0}
        usercolor_dict = {"black": "Черный", "white": "Белый"}
        user_color = self.user_color
        userstep = userstepcolor_dict[user_color]

        # Номер итерации
        i = 0
        won_color = ""

        print("\033[93m*Игра началась*\033[0m")
        journal = JournalWriterClass()
        while True:

            # Проверяем на окончание игры
            obj = GameOverClass(self.board_obj, user_color)
            if obj.result:
                won_color = obj.won_color
                print("Выиграл цвет: {}".format(usercolor_dict[obj.won_color]))
                break

            # Ходит пользователь
            if i % 2 == userstep:
                print("Ход №{}. Ходит пользователь..".format(i + 1))
                cmd = input("Введите команду -> ")
                result_dict = self.command_parser(cmd)

                # Если нормально прошло фильтрацию
                if result_dict != {}:
                    self.result_dict = result_dict
                    # Проверка на все критерии
                    obj = UserAnalyserClass(result_dict, self.board_obj, True)
                    # Если все хорошо, то осуществлем ход
                    if obj.boolean_result:
                        self.result_dict = obj.command_dict
                        # Пользователь ходит
                        self.user_mode()
                        journal.add_result(obj.command_dict)
                        i += 1
                    else:
                        print("\033[91m[Ошибка]\033[0m Некорректный ход")
                else:
                    print(
                        "\033[91m[Ошибка]\033[0m Некорректный ввод данных. Пример: 'c3:e5' - перемещение с боем, 'c3-b4' - тихое перемещение"
                    )

            # Компьютер ходит
            else:
                print("Ход №{}. Ходит компьютер..".format(i + 1))
                time.sleep(3)
                computergame_obj = ComputerGameClass(self.board_obj, user_color)
                d = computergame_obj.result_dict
                print(
                    "{} -> {}".format(
                        UtilClass.getfail_coords(d["from"]),
                        UtilClass.getfail_coords(d["to"]),
                    )
                )
                # Если тупиковый ход со стороны компьютера
                if not computergame_obj.result:
                    won_color = user_color
                    print("\033[91m[ИНФО]\033[0m У компьютера тупиковая ситуация")
                    print("Выиграл цвет: {}".format(usercolor_dict[user_color]))
                    break

                journal.add_result(d)
                i += 1

            # Вывод доски
            print(self.board_obj)

        # Добавление окончания
        journal.winlose_add(won_color)
        print(journal)

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

        # Получаем объект фигуры с ячейки и выставлем для него обновленные координаты
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


if __name__ == "__main__":
    MainClass()
