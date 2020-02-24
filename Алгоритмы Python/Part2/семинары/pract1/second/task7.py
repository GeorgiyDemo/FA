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

from faker import Faker
from random import randint

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

class PersonClass(PhoneDictionaryClass):
    """
    Класс персона
    """

    def __init__(self, name, address, phone_number):
        super().__init__(name, address, phone_number)

    def out_info(self):
        return "[Класс персона]\nФамилия"+self.name+"\nAдрес"+self.address+"\nНомер телефона:"+self.phone_number

class OrganizationClass(PhoneDictionaryClass):
    """
    Класс организация
    """

    def __init__(self, name, address, phone_number, fax, contact_person):
        super().__init__(name, address, phone_number)
        self.fax = fax
        self.contact_person = contact_person

    def out_info(self):
        return "[Класс организация]\nНазвание"+self.name+"\nAдрес"+self.address+"\nНомер телефона:"+self.phone_number+"\nФакс: "+self.fax+"\nКонтактое лицо:"+self.contact_person


class FriendClass(PhoneDictionaryClass):
    """
    Класс друг
    """

    def __init__(self, name, address, phone_number, birth_date):
        super().__init__(name, address, phone_number)
        self.birth_date = birth_date
    
    def out_info(self):
        return "[Класс друг]\nИмя"+self.name+"\nAдрес"+self.address+"\nНомер телефона:"+self.phone_number+"\nДата рождения: "+self.birth_date

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
        1 : PersonClass,
        2 : OrganizationClass,
        3 : FriendClass,
    }

    fake = Faker(['ru_RU'])
    base_list = []

    #################
    for _ in range(n):

        r_int = randint(1,3)

        d_args = {
            
            1 : (fake.word(),randint(1,1000000),fake.word(),randint(1,18)),
            2 : (fake.word(),randint(1,1000000),fake.word(),randint(1,18),"пластик"),
            3 : (fake.word(),randint(1,1000000),fake.word(),randint(1,18),fake.name()),
        }
        
        goods_list.append(d[r_int](*d_args[r_int]))


    for goods in goods_list:
        print(goods.get_info()+"\n")
if __name__ == "__main__":
    main()