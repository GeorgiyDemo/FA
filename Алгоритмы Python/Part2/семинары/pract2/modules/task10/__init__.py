from random import randint
from faker import Faker
from .goods_class import GoodsClass
from .product_class import ProductClass
from .group_class import GroupClass
from .phone_class import PhoneClass
from .search_module import *
def main():
    try:
        n = int(input("Введите количество товаров -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {1: GoodsClass, 2: ProductClass, 3: GroupClass, 4: PhoneClass,}
    fake = Faker(['ru_RU'])
    goods_list = []
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {1: (fake.word(), randint(1, 1000000), fake.date(pattern='%d.%m.%Y'), fake.date(pattern='%d.%m.%Y')), 2: (fake.word(), randint(1, 1000000), fake.date(pattern='%d.%m.%Y'), fake.date(pattern='%d.%m.%Y')),3: (fake.word(), randint(1, 1000000), fake.date(pattern='%d.%m.%Y'), fake.date(pattern='%d.%m.%Y'),randint(1, 100000)),4: (fake.word(), randint(1, 1000000)),}
        goods_list.append(d[r_int](*d_args[r_int]))
    displaying(goods_list)
    search(goods_list)