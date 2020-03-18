from random import randint
from .random_auto import random_auto, random_number
from .transport_class import TransportClass
from .car_class import CarClass
from .motorcycle_class import MotorcycleClass
from .truck_class import TruckClass
def main():
    n = int(input("Введите количество транспорта -> "))
    d = {1: TransportClass, 2: CarClass, 3: MotorcycleClass, 4: TruckClass,}
    transport_list, search_flag = [], False
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {1: (random_auto(), random_number(), randint(60, 300), randint(500, 10000)), 2: (random_auto(), random_number(), randint(60, 300), randint(500, 10000)), 3: (random_auto(), random_number(), randint(60, 300), randint(500, 10000), bool(randint(0, 1))), 4: (random_auto(), random_number(), randint(60, 300), randint(500, 10000), bool(randint(0, 1))),}
        transport_list.append(d[r_int](*d_args[r_int]))
    for transport in transport_list: print(transport.get_info() + "\n")
    carrying_input = float(input("Введите грузоподъёмность -> "))
    print("\n**Транспорт, грузоподъёмность которого меньше или равна заданной**\n")
    for transport in transport_list:
        if transport.get_carrying() <= carrying_input:
            print(transport.get_info() + "\n")
            search_flag = True
    if not search_flag: print("**Транспорт не найден**")