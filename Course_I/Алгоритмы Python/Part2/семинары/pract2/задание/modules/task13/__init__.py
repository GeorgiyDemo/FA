from random import randint

from faker import Faker

from .clent_class import ClentClass
from .contributor_class import ContributorClass
from .creditor_class import CreditorClass
from .organization_class import OrganizationClass
from .search_module import search


def main():
    try:
        n = int(input("Введите количество клиентов -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {
        1: ClentClass,
        2: ContributorClass,
        3: CreditorClass,
        4: OrganizationClass,
    }
    fake = Faker(["ru_RU"])
    bankclients_list = []
    for _ in range(n):
        r_int = randint(1, 4)
        d_args = {
            1: (
                fake.name(),
                fake.date(pattern="%d.%m.%Y"),
                randint(1, 1000000),
                randint(0, 100),
            ),
            2: (
                fake.name(),
                fake.date(pattern="%d.%m.%Y"),
                randint(1, 1000000),
                randint(0, 100),
            ),
            3: (
                fake.name(),
                fake.date(pattern="%d.%m.%Y"),
                randint(1, 1000000),
                randint(0, 100),
                randint(1, 1000000),
            ),
            4: (
                fake.word(),
                fake.date(pattern="%d.%m.%Y"),
                randint(1000000, 9999999),
                randint(1, 1000000),
            ),
        }
        bankclients_list.append(d[r_int](*d_args[r_int]))
    for cli in bankclients_list:
        print(cli.get_info() + "\n")
    search(bankclients_list)
