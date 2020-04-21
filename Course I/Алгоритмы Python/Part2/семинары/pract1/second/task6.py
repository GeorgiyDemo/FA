"""
Задача  6. Создайте класс ТОВАР с методами, позволяющими вывести на экран
информацию о товаре, а также определить, предназначен ли он для заданного возраста потребителя.

Создайте дочерние классы ИГРУШКА (название, цена, производитель, возраст, на который рассчитана, материал),
КНИГА (название, цена, издательство, возраст, на который рассчитана, автор),
СПОРТИНВЕНТАРЬ (название, цена, производитель, возраст, на который рассчитан)
со своими методами вывода информации на экран и определения соответствия возрасту потребителя.

Создайте список из п товаров, выведите полную информацию из базы на экран,
а также организуйте поиск товаров для потребителя в заданном возрастном диапазоне.
"""

from random import randint

from faker import Faker


class GoodsClass:
    """
    Класс товар
    """

    def __init__(self, name, price, manufacturer, age):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.age = age

    def get_info(self):
        return "[Информация о товаре]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nПроизводитель: " + self.manufacturer + "\nВозраст, на который рассчитан: " + str(self.age)

    def age_calculation(self, age_input):
        if age_input >= self.age:
            return True
        return False


class ToyClass(GoodsClass):
    """
    Класс игрушка
    """

    def __init__(self, name, price, manufacturer, age, material):
        super().__init__(name, price, manufacturer, age)
        self.material = material

    def get_info(self):
        return "[Информация об игрушке]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nПроизводитель: " + self.manufacturer + "\nВозраст, на который рассчитана: " + str(
            self.age) + "\nМатериал: " + self.material


class BookClass(GoodsClass):
    """
    Класс книга
    """

    def __init__(self, name, price, manufacturer, age, author):
        super().__init__(name, price, manufacturer, age)
        self.author = author

    def get_info(self):
        return "[Информация о книге]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nИздательство: " + self.manufacturer + "\nВозраст, на который рассчитана: " + str(
            self.age) + "\nАвтор: " + self.author


class SportGoodsClass(GoodsClass):
    """
    Класс спортинвентарь
    """

    def __init__(self, name, price, manufacturer, age):
        super().__init__(name, price, manufacturer, age)

    def get_info(self):
        return "[Информация о спортинвентаре]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nПроизводитель: " + self.manufacturer + "\nВозраст, на который рассчитан: " + str(self.age)


def main():
    """
    Создайте список из п товаров, выведите полную информацию из базы на экран,
    а также организуйте поиск товаров для потребителя в заданном возрастном диапазоне.
    """

    try:
        n = int(input("Введите количество товаров -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: GoodsClass,
        2: ToyClass,
        3: BookClass,
        4: SportGoodsClass,
    }

    fake = Faker(['ru_RU'])
    goods_list = []
    for _ in range(n):
        r_int = randint(1, 4)

        d_args = {

            1: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18)),
            2: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18), "пластик"),
            3: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18), fake.name()),
            4: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18)),
        }

        goods_list.append(d[r_int](*d_args[r_int]))

    for goods in goods_list:
        print(goods.get_info() + "\n")

    # Организуйте поиск товара, который может приобрести покупатель, имеющий заданную сумму денег.
    try:
        age_input = int(input("Введите возраст для фильтрации -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    search_flag = False
    print("Товары c фильтрацией по возрасту")
    for goods in goods_list:
        if goods.age_calculation(age_input) == True:
            print(goods.get_info() + "\n")
            search_flag = True

    if not search_flag:
        print("Товары не найдены")


if __name__ == "__main__":
    main()
