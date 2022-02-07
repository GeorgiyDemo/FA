"""
Задача 5. Создайте класс ТОВАР с методами, позволяющими вывести на экран информацию о товаре,
а также определить, может ли приобрести товар покупатель, имеющий заданную сумму денег.

Создайте дочерние классы
ПРОДУКТ (название, цена, дата производства, срок годности),
ПАРТИЯ (название, цена, дата производства, срок годности, количество штук),
ТЕЛЕФОН (название, цена) со своими методами вывода информации на экран и определения соответствия заданной цене.

Создайте список из п товаров, выведите полную информацию из базы на экран,
а также организуйте поиск товара, который может приобрести покупатель, имеющий заданную сумму денег.
"""

from random import randint

from faker import Faker


class GoodsClass:
    """
    Родительский класс товар
    """

    def __init__(self, name, price, manufacture_date, expiration_date):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date

    def get_info(self):
        return (
            "[Товар]\nНазвание: "
            + self.name
            + "\nЦена: "
            + str(self.price)
            + " руб.\nДата производства: "
            + self.manufacture_date
            + "\nСрок годности: "
            + self.expiration_date
        )

    def opportunity_detector(self, user_price):
        if user_price >= self.price:
            return True
        return False


class ProductClass(GoodsClass):
    """
    Дочерний класс продукт
    """

    def __init__(self, name, price, manufacture_date, expiration_date):
        super().__init__(name, price, manufacture_date, expiration_date)

    def get_info(self):
        return (
            "[Продукт]\nНазвание: "
            + self.name
            + "\nЦена: "
            + str(self.price)
            + " руб.\nДата производства: "
            + self.manufacture_date
            + "\nСрок годности: "
            + self.expiration_date
        )


class GroupClass(GoodsClass):
    """
    Дочерний класс партия
    """

    def __init__(self, name, price, manufacture_date, expiration_date, amount):
        super().__init__(name, price, manufacture_date, expiration_date)
        self.amount = amount

    def get_info(self):
        return (
            "[Партия]\nНазвание: "
            + self.name
            + "\nЦена: "
            + str(self.price)
            + " руб.\nДата производства: "
            + self.manufacture_date
            + "\nСрок годности: "
            + self.expiration_date
            + "\nКоличество штук: "
            + str(self.amount)
        )


class PhoneClass(GoodsClass):
    # Не обращаемся через super().__init__ т.к. нет некоторых полей
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return (
            "[Телефон]\nНазвание: " + self.name + "\nЦена: " + str(self.price) + " руб."
        )


def main():
    try:
        n = int(input("Введите количество товаров -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: GoodsClass,
        2: ProductClass,
        3: GroupClass,
        4: PhoneClass,
    }

    fake = Faker(["ru_RU"])
    goods_list = []
    for _ in range(n):
        r_int = randint(1, 4)

        d_args = {
            1: (
                fake.word(),
                randint(1, 1000000),
                fake.date(pattern="%d.%m.%Y"),
                fake.date(pattern="%d.%m.%Y"),
            ),
            2: (
                fake.word(),
                randint(1, 1000000),
                fake.date(pattern="%d.%m.%Y"),
                fake.date(pattern="%d.%m.%Y"),
            ),
            3: (
                fake.word(),
                randint(1, 1000000),
                fake.date(pattern="%d.%m.%Y"),
                fake.date(pattern="%d.%m.%Y"),
                randint(1, 100000),
            ),
            4: (fake.word(), randint(1, 1000000)),
        }

        goods_list.append(d[r_int](*d_args[r_int]))

    for goods in goods_list:
        print(goods.get_info() + "\n")

    # Организуйте поиск товара, который может приобрести покупатель, имеющий заданную сумму денег.
    try:
        price_input = float(input("Введите цену -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    search_flag = False
    print("Товары, которые вы можете себе позволить:")
    for goods in goods_list:
        if goods.opportunity_detector(price_input) == True:
            print(goods.get_info() + "\n")
            search_flag = True

    if not search_flag:
        print("Товары не найдены")


if __name__ == "__main__":
    main()
