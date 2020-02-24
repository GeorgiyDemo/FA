"""
Задача 8. Создайте класс КЛИЕНТ с методами,
позволяющими вывести на экран информацию о клиентах банка,
а также определить соответствие клиента критерию поиска.

Создайте дочерние классы ВКЛАДЧИК (фамилия, дата открытия вклада, размер вклада, процент по вкладу),
КРЕДИТОР (фамилия, дата выдачи кредита, размер кредита, процент по кредиту, остаток долга),
ОРГАНИЗАЦИЯ (название, дата открытия счета, номер счета, сумма на счету)

со своими методами вывода информации на экран и определения соответствия дате 
(открытия вклада, выдаче кредита, открытия счета).

Создайте список из п клиентов, выведите полную информацию из базы на экран,
а также организуйте поиск клиентов, начавших сотрудничать с банком в заданную дату.
"""

from faker import Faker
from random import randint

class ClentClass:
    """
    Класс клиент
    """
    def __init__(self, name, open_date, money_count, percent):
        self.name = name
        self.open_date = open_date
        self.money_count = money_count
        self.percent = percent
    
    def get_info(self):
        return "[Информация о клиенте]\nФИО: "+self.name+"\nДата оформления операции: "+self.open_date+"\nРазмер денежных единиц в операции: "+str(self.money_count)+" руб.\nПроцент: "+str(self.percent)+"%"

    def date_calculation(self, input_date):
        if input_date == self.open_date:
            return True
        return False

class ContributorClass(ClentClass):
    """
    Класс вкладчик
    """
    def __init__(self, name, open_date, money_count, percent):
        super().__init__(name, open_date, money_count, percent)

    def get_info(self):
        return "[Информация о вкладчике]\nФИО: "+self.name+"\nДата открытия вклада: "+self.open_date+"\nРазмер вклада: "+str(self.money_count)+" руб.\nПроцент по вкладу: "+str(self.percent)+"%"

class CreditorClass(ClentClass):
    """
    Класс кредитор
    """
    def __init__(self, name, open_date, money_count, percent, balance_owed):
        super().__init__( name, open_date, money_count, percent)
        self.balance_owed = balance_owed
    
    def get_info(self):
        return "[Информация о кредиторе]\nФИО: "+self.name+"\nДата выдачи кредита: "+self.open_date+"\nРазмер кредита: "+str(self.money_count)+" руб.\nПроцент по кредиту: "+str(self.percent)+"%\nОстаток долга: "+str(self.balance_owed)+" руб."

class OrganizationClass(ClentClass):
    """
    Класс организация
    """
    def __init__(self, name, open_date, account_number, balance):
        self.name = name
        self.open_date = open_date
        self.account_number = account_number
        self.balance = balance

    def get_info(self):
        return "[Информация об организации]\nНазвание: "+self.name+"\nДата открытия счёта: "+self.open_date+"\nНомер счёта: "+str(self.account_number)+"\nСумма на счету: "+str(self.balance)+" руб."


def main():
    """
    Создайте список из п клиентов, выведите полную информацию из базы на экран,
    а также организуйте поиск клиентов, начавших сотрудничать с банком в заданную дату.
    """
    try:
        n = int(input("Введите количество клиентов -> "))
    except ValueError:
        print("Некорректный ввод данных")
        return

    d = {
        1 : ClentClass,
        2 : ContributorClass,
        3 : CreditorClass,
        4 : OrganizationClass,
    }

    fake = Faker(['ru_RU'])
    bankclients_list = []
    for _ in range(n):

        r_int = randint(1,4)

        d_args = {
            1 : (fake.name(),fake.date(pattern='%d.%m.%Y'),randint(1,1000000),randint(0,100)),
            2 : (fake.name(),fake.date(pattern='%d.%m.%Y'),randint(1,1000000),randint(0,100)),
            3 : (fake.name(),fake.date(pattern='%d.%m.%Y'),randint(1,1000000),randint(0,100),randint(1,1000000)),
            4 : (fake.word(),fake.date(pattern='%d.%m.%Y'),randint(1000000,9999999),randint(1,1000000)),
        }
        
        bankclients_list.append(d[r_int](*d_args[r_int]))


    for cli in bankclients_list:
        print(cli.get_info()+"\n")

    #Поиск клиентов, начавших сотрудничать с банком в заданную дату.
    try:
        input_date = input("Введите дату для поиска клиентов в формате 01.01.2020 -> ")
        _, _, _ = input_date.split(".")
    
    except ValueError:
        print("Некорректный ввод данных")
        return

    search_flag = False
    print("Найденные клиенты:")
    for cli in bankclients_list:
        if cli.date_calculation(input_date) == True:
            print(cli.get_info()+"\n")
            search_flag = True

    if not search_flag:
        print("Клиенты не найдены")


if __name__ == "__main__":
    main()