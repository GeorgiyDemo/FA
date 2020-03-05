# TODO Изначальный банк
# TODO Коэффициенты на тараканов
# TODO Несколько забегов, проигрывает тот, у кого 0 руб остается, выигрывает - у кого больше всего денег
#TODO Возможность ввода только положительных значений > 0

from random import randint
from faker import Faker
from time import sleep
import texttable


class CockroachClass():
    """
    Класс таракан
    """

    def __init__(self, name):
        self.__name = name
        self.__current_location = 0
        self.__speed_generator()

    def movement_changer(self):
        self.movement = bool(randint(0, 1))
        # Если было перемещение
        if self.movement:
            self.__current_location += self.__speed

    def __speed_generator(self):
        # Генерация скорости
        self.__speed = randint(1, 10)

    @property
    def name(self):
        return self.__name

    @property
    def current_location(self):
        return self.__current_location

    @property
    def speed(self):
        return self.__speed


class GamerClass():
    """
    Класс геймер, что у него есть:
    - Таракан ( может ващ объект передавать?)
    - Деньги

    Один игрок = один таракан
    """

    def __init__(self, name, begin_money=1500):
        self.__name = name
        self.__cockroach_obj = None
        self.__all_money = begin_money
        self.__locale_money = None

    @property
    def cockroach_obj(self):
        return self.__cockroach_obj

    @cockroach_obj.setter
    def cockroach_obj(self, obj):
        assert isinstance(obj, CockroachClass), "Некорректное значение"
        self.__cockroach_obj = obj

    @property
    def name(self):
        return self.__name

    #А нужен ли сеттер
    @property
    def all_money(self):
        return self.__all_money

    @all_money.setter
    def all_money(self, val):
        """
        Осуществление set'а ставки
        """
        assert type(val) == float, "Некорректное значение"
        self.__all_money = val

    @property
    def locale_money(self):
        return self.__locale_money

    @locale_money.setter
    def locale_money(self, new_money):
        assert type(new_money) == float, "Некорректное значение"
        self.__all_money -= new_money 
        self.__locale_money = new_money

    def opportunity_checker(self, money):
        """
        Метод для проверки на возможность сделать ставку
        """
        if self.__all_money - money < 0:
            return False
        return True


class RaceClass():
    """
    Класс текущей гонки
    """
    
    def __init__(self, user_list):
        
        self.user_list = user_list
        self.COCKROACH_COUNT = len(user_list)*2
        self.COCKROACH_ICON = "🦗"
        self.GRASS_ICON = "_"
        self.ITERATIONS_COUNT = 50

        fake = Faker(['ru_RU'])

        # Хранит объекты тараканов
        self.cockroach_list = []

        # Начальная матрица
        self.start_matrix_generator()

        # Генерируем тараканов
        for i in range(self.COCKROACH_COUNT):
            cockroach_obj = CockroachClass(fake.word())
            self.cockroach_list.append(cockroach_obj)

        # Выбор ассоциации пользователь -> таракан
        self.user_chooser()

        # Основная логика
        for current_iteration in range(self.ITERATIONS_COUNT):

            print("Итерация №{}".format(current_iteration))
            # Отображение рейтинга тараканов
            self.rating_drawer()
            self.game_field_drawer()
            input()

            try:
                self.cockroach_changer()
            # Если допрыгались до IndexError
            except IndexError:
                self.winner_detector()
                break

    def getusers_cockroachobj(self, obj):
        """
        Получение имен пользователей по объекту таракана
        """
        out_names = []
        for e in self.user_list:
            if e.cockroach_obj == obj:
                out_names.append(e.name)

        return ", ".join(out_names)

    def user_chooser(self):
        """
        Выбор ассоциации пользователь -> таракан
        """

        for user in self.user_list:

            allowed_cockroach_list = []

            table = texttable.Texttable()
            table_list = [["№", "Кличка", "Скорость"], ]

            for i in range(len(self.cockroach_list)):

                e = self.cockroach_list[i]
                allowed_cockroach_list.append(i+1)
                table_list.append([str(i+1), e.name, str(e.speed)])

            table.add_rows(table_list)
            print(table.draw() + "\n")

            processing_flag = True
            while processing_flag:
                try:
                    print("Выберите № таракана для игрока '{}':".format(user.name))

                    # Выбираем таракана
                    selected_cockroach = int(input("\n-> "))
                    if selected_cockroach not in allowed_cockroach_list:
                        raise ValueError("Некорректный ввод номера таракана")

                    obj = self.cockroach_list[selected_cockroach-1]

                    # Делаем ставку
                    money = float(input("Введите вашу ставку на выигрыш '{}', ваш текущий баланс: {} руб.\n-> ".format(obj.name, user.all_money)))
                    
                    #Проверяем на то, чтоб у пользователя были деньги
                    if user.opportunity_checker(money):
                        # Вводим ассоциацию
                        obj.selected = True
                        user.cockroach_obj = obj
                        user.locale_money = money
                        processing_flag = False
                    
                    else:
                        print("У Вас недостаточно денег для ставки на {} в размере {} руб.".format(obj.name, money))

                except ValueError as e:
                    print(e)
                    continue

    def rating_drawer(self):
        """
        Рисовальщик рейтинга тараканов
        """
        cockroach_list = self.cockroach_list.copy()
        cockroach_list.sort(key=lambda e: e.current_location, reverse=True)
        table = texttable.Texttable()

        table_list = [
            ["Место", "Кличка", "Точка", "Пользователи"],
        ]

        for i in range(len(cockroach_list)):
            e = cockroach_list[i]
            table_list.append(
                [str(i+1), e.name, str(e.current_location), self.getusers_cockroachobj(e)])

        table.add_rows(table_list)
        print(table.draw() + "\n")

    def winner_detector(self):
        # TODO
        """
        Метод, определяющий то, какой таракан выиграл
        """
        winner = sorted(self.cockroach_list,
                        key=lambda e: e.current_location, reverse=True)[0]
        print("Победитель: {}".format(winner.name))
        self.rating_drawer()

        old_money = 0
        win_obj_users_list = []

        # Ищем игроков-победителей
        for u in self.user_list:
            if u.cockroach_obj == winner:
                win_obj_users_list.append(u)

            else:
                old_money += u.money
                u.money = 0.0

        # Распределение на каждого человека
        if len(win_obj_users_list) != 0:
            koff = old_money/len(win_obj_users_list)
            for obj in win_obj_users_list:
                obj.money += koff
                print("{} получает сумму {} руб, общее кол-во денег: {}".format(obj.name, koff, obj.money))
        
        else:
            for u in self.user_list:
                print(u.money)

    def start_matrix_generator(self):
        """
        Метод генерации начальной матрицы
        """
        # Начальная матрица
        self.matrix = [[self.GRASS_ICON for c in range(
            self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]
        for i in range(len(self.matrix)):
            self.matrix[i][0] = self.COCKROACH_ICON

    def cockroach_changer(self):
        """
        Осуществление перемещения таракана
        """
        self.matrix = [[self.GRASS_ICON for c in range(
            self.ITERATIONS_COUNT)] for r in range(self.COCKROACH_COUNT)]

        for i in range(len(self.cockroach_list)):

            e = self.cockroach_list[i]
            e.movement_changer()
            self.matrix[i][e.current_location] = self.COCKROACH_ICON

    def game_field_drawer(self):
        """
        Отображение на экране
        """

        for i in range(len(self.matrix)):
            print(i+1, end=" ")
            for j in range(len(self.matrix[i])):
                print('{}'.format(self.matrix[i][j]), end=" ")
            print("|   Таракан '{}'".format(self.cockroach_list[i].name))

        print("\n")

class MainClass():

    def __init__(self):

        # Храние объектов игроков
        self.user_list = []

        # Генерация пользователей и их начальных данных
        self.user_input_generator()

        #Пока у одного из пользователей не 0 руб, то вызываем гонку
        while self.gameover_detector:
            
            input("Вы готовы к гонке?")
            #TODO Синхронизация user_list т.к. там вроде как уже дроугие объкты, это же ссылка? (я не помню)
            RaceClass(self.user_list)
    
    def gameover_detector(self):
        """
        Метод, проверяющий окончание игры
        (пока у одного пользователя не закончились деньги)
        """
        for u in self.user_list:
            if u.all_money <= 0:
                return False
        return True
                            
    def user_input_generator(self):
        """
        Ввод количества пользователей для ставок
        """
        input_flag = True
        while input_flag:
            try:
                users_count = int(input("Введите количество игроков -> "))
                input_flag = False
            except ValueError:
                continue

        # Генерируем пользователей
        for i in range(users_count):
            curent_user_name = input(
                "Введите ФИО пользователя №{} -> ".format(i+1))
            user_obj = GamerClass(curent_user_name)
            self.user_list.append(user_obj)

if __name__ == "__main__":
    obj = MainClass()
