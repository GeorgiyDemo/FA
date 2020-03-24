"""
Задача  11. Создайте класс ИГРУШКА с методами, позволяющими вывести на экран информацию о товаре,
а также определить соответствие игрушки критерию поиска.

Создайте дочерние классы КУБИК (цвет, цена, материал, размер ребра),
МЯЧ (цвет, цена, материал, диаметр),
МАШИНКА (цвет, цена, название, производитель) со своими методами вывода информации на экран и 
определения соответствия заданному цвету.

Создайте список из п игрушек, выведите полную информацию из базы на экран,
а также организуйте поиск игрушек заданного цвета.
"""

from random import randint

from faker import Faker
from random_color import random_color

class ToyClass:
    """
    Класс игрушка
    """

    def __init__(self, color, price, material, size):
        self.color = color
        self.price = price
        self.material = material
        self.size = size

    def toy_info(self):
        return "[Базовый класс игрушка]\nЦвет: " + self.color + "\nЦена: " + str(
            self.price) + " руб.\nМатериал: " + self.material + "\nРазмер: " + str(self.size) + " см."

    def color_detector(self, color_input):
        if color_input == self.color:
            return True
        return False


class CubeClass(ToyClass):
    """
    Класс Куб
    """

    def __init__(self, color, price, material, size):
        super().__init__(color, price, material, size)

    def toy_info(self):
        return "[Кубик]\nЦвет: " + self.color + "\nЦена: " + str(
            self.price) + " руб.\nМатериал: " + self.material + "\nРазмер ребра: " + str(self.size) + " см."


class BallClass(ToyClass):
    """
    Класс мяч
    """

    def __init__(self, color, price, material, size):
        super().__init__(color, price, material, size)

    def toy_info(self):
        return "[Мяч]\nЦвет: " + self.color + "\nЦена: " + str(
            self.price) + " руб.\nМатериал: " + self.material + "\nДиаметр: " + str(self.size) + " см."


class CarClass(ToyClass):
    """
    Класс машинка
    """

    def __init__(self, color, price, name, manufacturer):
        self.color = color
        self.price = price
        self.name = name
        self.manufacturer = manufacturer

    def toy_info(self):
        return "[Машинка]\nЦвет: " + self.color + "\nЦена: " + str(
            self.price) + " руб.\nНазвание: " + self.name + "\nПроизводитель: " + self.manufacturer


def main():
    """
    Создайте список из п игрушек, выведите полную информацию из базы на экран,
    а также организуйте поиск игрушек заданного цвета.
    """

    try:
        n = int(input("Введите количество игрушек -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: ToyClass,
        2: CubeClass,
        3: BallClass,
        4: CarClass,
    }

    fake = Faker(['ru_RU'])
    toy_list = []
    for _ in range(n):
        r_int = randint(1, 4)

        d_args = {
            1: (random_color(), randint(1, 1000), "пластик", randint(1, 20)),
            2: (random_color(), randint(1, 1000), "пластик", randint(1, 20)),
            3: (random_color(), randint(1, 1000), "пластик", randint(1, 20)),
            4: (random_color(), randint(1, 1000), fake.word(), fake.word() + " " + fake.word()),
        }

        toy_list.append(d[r_int](*d_args[r_int]))

    for toy in toy_list:
        print(toy.toy_info() + "\n")

    # организуйте поиск игрушек заданного цвета.
    try:
        color_input = input("Введите цвет для поиска игрушек -> ")
    except ValueError:
        print("Некорректный ввод данных")
        return

    search_flag = False
    print("Игрушки c фильтрацией по цвету")
    for toy in toy_list:
        if toy.color_detector(color_input):
            print(toy.toy_info() + "\n")
            search_flag = True

    if not search_flag:
        print("Игрушки не найдены")


if __name__ == "__main__":
    main()
