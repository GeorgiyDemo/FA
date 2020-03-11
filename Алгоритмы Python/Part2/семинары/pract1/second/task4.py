"""
Задача 4. Создайте класс ТРАНСПОРТ с методами, позволяющими вывести на экран информацию о 
транспортном средстве, а также определить грузоподъемность транспортного средства.

Создайте дочерние классы АВТОМОБИЛЬ (марка, номер, скорость, грузоподъемность),

МОТОЦИКЛ (марка, номер, скорость, грузоподъемность, наличие коляски,
при этом если коляска отсутствует, то грузоподъемность равна нулю),

ГРУЗОВИК (марка, номер, скорость, грузоподъемность, наличие прицепа,
при этом если есть прицеп, то грузоподъемность увеличивается в два раза)
со своими методами вывода информации на экран и определения грузоподъемности.

Создайте список из п машин, выведите полную информацию на экран, а также организуйте поиск машин, удовлетворяющих требованиям грузоподъемности.
"""

from random import randint

from random_auto import random_auto, random_number


class TransportClass:
    """
    Базовый класс транспорт
    """

    def __init__(self, model, number, speed, carrying):
        self.model = str(model)
        self.number = str(number)
        self.speed = speed
        self.carrying = carrying

    def get_info(self):
        return "[Транспорт]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying)

    def get_carrying(self):
        return self.carrying


class CarClass(TransportClass):
    """
    Дочерний класс автомобиль
    """

    def __init__(self, model, number, speed, carrying):
        super().__init__(model, number, speed, carrying)

    def get_info(self):
        return "[Автомобиль]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying)


class MotorcycleClass(TransportClass):
    """
    Дочерний класс мотоцикл
    """

    def __init__(self, model, number, speed, carrying, addition):
        super().__init__(model, number, speed, carrying)

        self.addition = addition
        # Для красивого вывода в get_info
        self.formater_dict = {
            True: "Да",
            False: "Нет",
        }
        self.carrying_calculating()

    def carrying_calculating(self):
        # Это все адекватные люди сделали бы это в конструкторе, но задание требует
        if self.addition == False:
            self.carrying = 0

    def get_info(self):
        return "[Мотоцикл]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying) + "\nНаличие коляски: " + self.formater_dict[
                   self.addition]


# Я бы занаследовался бы от мотоцикла
class TruckClass(TransportClass):
    """
    Дочерний класс грузовик
    """

    def __init__(self, model, number, speed, carrying, addition):
        super().__init__(model, number, speed, carrying)
        self.addition = addition
        self.formater_dict = {
            True: "Да",
            False: "Нет",
        }
        self.carrying_calculating()

    def carrying_calculating(self):
        if self.addition == True:
            self.carrying *= 2

    def get_info(self):
        return "[Грузовик]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying) + "\nНаличие прицепа: " + self.formater_dict[
                   self.addition]


def main():
    try:
        n = int(input("Введите количество транспорта -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: TransportClass,
        2: CarClass,
        3: MotorcycleClass,
        4: TruckClass,
    }

    transport_list = []
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {
            1: (random_auto(), random_number(), randint(60, 300), randint(500, 10000)),
            2: (random_auto(), random_number(), randint(60, 300), randint(500, 10000)),
            3: (random_auto(), random_number(), randint(60, 300), randint(500, 10000), bool(randint(0, 1))),
            4: (random_auto(), random_number(), randint(60, 300), randint(500, 10000), bool(randint(0, 1))),
        }
        transport_list.append(d[r_int](*d_args[r_int]))

    for transport in transport_list:
        print(transport.get_info() + "\n")

    # Организуйте поиск машин, удовлетворяющих требованиям грузоподъемности.
    try:
        carrying_input = float(input("Введите грузоподъёмность -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    print("\n**Транспорт, грузоподъёмность которого меньше или равна заданной**\n")
    search_flag = False
    for transport in transport_list:
        if transport.get_carrying() <= carrying_input:
            print(transport.get_info() + "\n")
            search_flag = True

    if not search_flag:
        print("**Транспорт не найден**")


if __name__ == "__main__":
    main()
