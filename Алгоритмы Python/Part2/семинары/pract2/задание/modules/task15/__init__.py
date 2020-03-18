from random import randint
from faker import Faker
from .ship_class import ShipClass
from .car_class import CarClass
from .airplane_class import AirplaneClass
from .transport_class import TransportClass
from .util_module import display, search
def main():
    try:
        n = int(input("Введите кол-во транспортных средств -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {1: TransportClass,2: AirplaneClass,3: CarClass,4: ShipClass,}
    fake = Faker(['ru_RU'])
    transport_list = []
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {1: (fake.word(), [randint(1, 100), randint(1, 100)]),2: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), randint(1000, 6000)),3: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(1960, 2020)),4: (fake.word(), [randint(1, 100), randint(1, 100)], randint(1, 1000), randint(50, 300), fake.word()),}
        transport_list.append(d[r_int](*d_args[r_int]))
    display(transport_list)
    search(transport_list)