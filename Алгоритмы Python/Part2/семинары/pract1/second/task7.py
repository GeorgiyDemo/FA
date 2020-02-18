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

class PhoneDictionaryClass:
    """
    Класс телефонный справочник
    """

    def search(self, input_name):
        if input_name in self.name:
            return True
        return False

    def out_info(self):
        pass


class PersonClass(PhoneDictionaryClass):
    """
    Класс персона
    """

    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def out_info(self):
        pass

class OrganizationClass(PhoneDictionaryClass):
    """
    Класс организация
    """

    def __init__(self, name, address, phone_number, fax, contact_person):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.fax = fax
        self.contact_person = contact_person


class FriendClass(PhoneDictionaryClass):
    """
    Класс друг
    """

    def __init__(self, name, address, phone_number, birth_date):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.birth_date = birth_date

def main():
    pass

if __name__ == "__main__":
    main()