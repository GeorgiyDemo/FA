from random import randint

from faker import Faker

from .ball_class import BallClass
from .car_class import CarClass
from .cube_class import CubeClass
from .random_color import random_color
from .toy_class import ToyClass
from .util_module import search, display


def main():
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
    fake = Faker(["ru_RU"])
    toy_list = []
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {
            1: (random_color(), randint(1, 1000), "пластик", randint(1, 20)),
            2: (random_color(), randint(1, 1000), "пластик", randint(1, 20)),
            3: (random_color(), randint(1, 1000), "пластик", randint(1, 20)),
            4: (
                random_color(),
                randint(1, 1000),
                fake.word(),
                fake.word() + " " + fake.word(),
            ),
        }
        toy_list.append(d[r_int](*d_args[r_int]))
    display(toy_list)
    search(toy_list)
