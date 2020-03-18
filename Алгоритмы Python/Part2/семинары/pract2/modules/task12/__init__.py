from random import randint
from faker import Faker
from phonedictionary_class import PhoneDictionaryClass
from person_class import PersonClass
from organization_class import OrganizationClass
from friend_class import FriendClass
from search_module import search
def main():
    try:
        n = int(input("Введите количество записей -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return
    d = {1: PersonClass,2: OrganizationClass,3: FriendClass,}
    fake, obj_list = Faker(['ru_RU']), []
    for _ in range(n):
        r_int = randint(1, 3)
        d_args = {1: (fake.name(), fake.address(), fake.phone_number()),2: (fake.word(), fake.address(), fake.phone_number(), fake.phone_number(), fake.name()), 3: (fake.name(), fake.address(), fake.phone_number(), fake.date(pattern='%d.%m.%Y')),}
        obj_list.append(d[r_int](*d_args[r_int]))
    for obj in obj_list:
        print(obj.out_info() + "\n")
    search(obj_list)