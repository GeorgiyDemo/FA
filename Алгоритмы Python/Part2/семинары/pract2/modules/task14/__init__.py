import datetime
from random import randint
from faker import Faker
from software_class import SoftwareClass
from freeware_class import FreewareClass
from trial_class import TrialClass
from commercial_class import CommercialClass
from util_module import search, display
def main():
    try:
        n = int(input("Введите количество ПО -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {1: FreewareClass,2: TrialClass,3: CommercialClass,}
    fake = Faker(['ru_RU'])
    software_list = []
    for _ in range(n):
        r_int = randint(1, 3)
        d_args = {1: (fake.word(), fake.word() + " " + fake.word()),2: (fake.word(), fake.word() + " " + fake.word(), fake.date(pattern='%d.%m.%Y'), randint(0, 1800)),3: (fake.word(), fake.word() + " " + fake.word(), fake.date(pattern='%d.%m.%Y'), randint(0, 1800)),}
        software_list.append(d[r_int](*d_args[r_int]))
    display(software_list)
    search(software_list)