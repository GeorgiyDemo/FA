from random import randint
from faker import Faker
from .goods_class import GoodsClass
from .toy_class import ToyClass
from .book_class import BookClass
from .sportgoods_class import SportGoodsClass
from .search_module import search 
def main():
    try:
        n = int(input("Введите количество товаров -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {1: GoodsClass, 2: ToyClass, 3: BookClass, 4: SportGoodsClass,}
    fake = Faker(['ru_RU'])
    goods_list = []
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {1: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18)),2: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18), "пластик"),3: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18), fake.name()),4: (fake.word(), randint(1, 1000000), fake.word(), randint(1, 18)),}
        goods_list.append(d[r_int](*d_args[r_int]))
    for goods in goods_list:
        print(goods.get_info() + "\n")
    search(goods_list)