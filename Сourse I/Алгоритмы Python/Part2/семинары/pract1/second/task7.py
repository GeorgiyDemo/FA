"""
Задача 7. Создайте класс ТЕЛЕФОННЫЙ СПРАВОЧНИК с методами,
позволяющими вывести на экран информацию о записях в телефонном справочнике,
а также определить соответствие записи критерию поиска.

Создайте дочерние классы ПЕРСОНА (фамилия, адрес, номер телефона),
ОРГАНИЗАЦИЯ (название, адрес, телефон, факс, контактное лицо),
ДРУГ (фамилия, адрес, номер телефона, дата рождения)

со своими методами вывода информации на экран и определения соответствия заданной фамилии.

Создайте список из п записей, выведите полную информацию из базы на экран,
 а также организуйте поиск в базе по фамилии.
"""

from random import randint

from faker import Faker


class PhoneDictionaryClass:
    """
    Класс телефонный справочник
    """

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def search(self, input_name):
        if input_name in self.name:
            return True
        return False

    def out_info(self):
        ...


class PersonClass(PhoneDictionaryClass):
    """
    Класс персона
    """

    def __init__(self, name, address, phone_number):
        super().__init__(name, address, phone_number)

    def out_info(self):
        return "[Класс персона]\nФИО: " + self.name + "\nAдрес: " + self.address + "\nНомер телефона: " + self.phone_number


class OrganizationClass(PhoneDictionaryClass):
    """
    Класс организация
    """

    def __init__(self, name, address, phone_number, fax, contact_person):
        super().__init__(name, address, phone_number)
        self.fax = fax
        self.contact_person = contact_person

    def out_info(self):
        return "[Класс организация]\nНазвание: " + self.name + "\nAдрес: " + self.address + "\nНомер телефона: " + self.phone_number + "\nФакс: " + self.fax + "\nКонтактое лицо: " + self.contact_person

    def search(self, input_name):
        if input_name in self.contact_person:
            return True
        return False


class FriendClass(PhoneDictionaryClass):
    """
    Класс друг
    """

    def __init__(self, name, address, phone_number, birth_date):
        super().__init__(name, address, phone_number)
        self.birth_date = birth_date

    def out_info(self):
        return "[Класс друг]\nФИО: " + self.name + "\nAдрес: " + self.address + "\nНомер телефона: " + self.phone_number + "\nДата рождения: " + self.birth_date


def main():
    """
    Создайте список из п записей, выведите полную информацию из базы на экран,
    а также организуйте поиск в базе по фамилии.
    """

    try:
        n = int(input("Введите количество записей -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1: PersonClass,
        2: OrganizationClass,
        3: FriendClass,
    }

    fake = Faker(['ru_RU'])
    obj_list = []

    for _ in range(n):
        r_int = randint(1, 3)

        d_args = {

            1: (fake.name(), fake.address(), fake.phone_number()),
            2: (fake.word(), fake.address(), fake.phone_number(), fake.phone_number(), fake.name()),
            3: (fake.name(), fake.address(), fake.phone_number(), fake.date(pattern='%d.%m.%Y')),
        }

        obj_list.append(d[r_int](*d_args[r_int]))

    for obj in obj_list:
        print(obj.out_info() + "\n")

    try:
        input_name = input("Введите фамилию для поиска -> ")
    except ValueError:
        print("Некорректный ввод данных")
        return

    print("\n*Абоненты системы с фамилией \"" + input_name + "\"*")

    search_flag = False
    for obj in obj_list:
        if obj.search(input_name):
            search_flag = True
            print(obj.out_info() + "\n")

    if not search_flag:
        print("Абоненты не найдены")


if __name__ == "__main__":
    main()
