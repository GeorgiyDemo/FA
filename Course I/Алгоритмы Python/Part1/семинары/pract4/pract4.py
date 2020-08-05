import random
import string

UNIC_NAMES_LIST = [
    "Комова Елизавета Олеговна",
    "Репенков Сергей Алексеевич",
    "Анисимов Ефим Сергеевич",
    "Борисов Никита Алексеевич",
    "Исмоилова Милена Витальевна",
    "Рогов Владимир Алексеевич",
    "Савочкин Артём Дмитриевич",
    "Кривошеина Елена Олеговна",
    "Пономарев Михаил Александрович",
    "Абдулмеджидов Мирза Мурадович",
    "Егшатян Артем Кирович",
    "Гарайшин Тамерлан Тагирович",
    "Брусова Полина Игоревна",
    "Крылова Елизавета Алексеевна",
    "Гераськина Надежда Станиславовна",
    "Гиниятуллина Эвита Маратовна",
    "Малахов Иван Петрович",
    "Жилина Алена Алексеевна",
    "Королев Илья Алексеевич",
    "Пойкалайнен Александра Максимовна",
    "Щербак Станислав Валентинович",
    "Буркина Елизавета Сергеевна",
    "Мосолова Ксения Дмитриевна",
    "Кротов Олег Валерьевич",
    "Шаповалов Сергей Александрович",
    "Прищепа Екатерина Михайловна",
    "Артемьева Дарья Сергеевна",
    "Попова Софья Александровна",
    "Башмакова Анастасия Алексеевна",
    "Корнева Татьяна Андреевна",
    "Олзошкина Янжина Владленовна",
    "Касьянов Максим Евгеньевич",
    "Олейник Анастасия Александровна",
    "Сивухов Артём Олегович",
    "Груздев Всеволод Алексеевич",
    "Буковец Данила Андреевич",
    "Зелянина Алёна Геннадьевна",
    "Мерзляков Данила Артемович",
    "Карасёв Артём Владимирович",
    "Пономаренко Александр Павлович",
    "Курносиков Кирилл Андреевич",
    "Гуриков Дмитрий Олегович",
    "Котова Екатерина Дмитриевна",
    "Лихачев Марк Игоревич",
    "Волкова Татьяна Алексеевна",
    "Марунько Анна Сергеевна",
    "Пашкевич Денис Вячеславович",
    "Маркова Ольга Алексеевна",
    "Термышева Полина Евгеньевна",
    "Василевская Лидия Игоревна",
]


class Task1:
    """
    Создать словарь адресной книги, содержащий ФИО и адрес. Заполнить его 50 элементами, реализовать поиск по адресу
    """

    def __init__(self):
        self.dict_generator()
        self.search()

    def dict_generator(self):
        n = UNIC_NAMES_LIST
        self.d = {}
        for i in range(0, len(n), 2):
            self.d["адрес №" + str(i)] = [n[i], n[i + 1]]

    def search(self):
        s = input("Введите адрес для поиска ->")
        if s in self.d:
            print("Адрес найден!\nПроживающие по адресу:")
            [print(x) for x in self.d[s]]
        else:
            for k, v in self.d.items():
                for p in v:
                    if s in p:
                        print("Возможно вы имели ввиду '" + p + "' по '" + k + "'")


class Task2:
    """
    Cоздать словарь телефонного справочника. Заполнить его 50 элементами. Реализовать поиск по телефону
    """

    def __init__(self):
        self.dict_generator()
        self.search()

    def locale_random(self, n):
        return str(random.randint(10 ** (n - 1), (10 ** n) - 1))

    def dict_generator(self):
        self.d = {}
        for e in UNIC_NAMES_LIST:
            key = "+7" + self.locale_random(10)
            self.d[key] = e
            print("Сгенерировали ключ " + key)

    def search(self):
        input_key = input("Введите номер телефона для поиска ->")
        if input_key in self.d:
            print("Значение для телефона " + input_key + " -> " + self.d[input_key])
        else:
            print("Введённого номера телефона нет в базе")


class Task3(object):
    """
    реализовать проверку на существующие записи в предыдущих заданиях с возможностью дополнения
    """

    def __init__(self):
        d = {
            "1": Task1Plus,
            "2": Task2Plus,
        }
        e = input("Какой номер вы хотите дополнить ?")
        if e in d:
            d[e]()
        else:
            print("Такого номера не существует!")


class Task1Plus(Task1):
    """
    Класс для дополнения задания №1
    """

    def __init__(self):
        self.dict_generator()
        self.search()

    def search(self):
        s = input("Введите адрес для поиска ->")
        if s in self.d:
            print("Адрес найден!\nПроживающие по адресу:")
            [print(x) for x in self.d[s]]
        else:
            print("Адрес не найден, но мы его добавим в систему")
            names = input(
                "Введите ФИО людей, проживающих по этому адресу через заптую -> "
            )
            self.d[s] = names.split(",")
            print("Обновлённый словарь:")
            for k, v in self.d.items():
                print(k, v)


class Task2Plus(Task2):
    """
    Класс для дополнения задания №2
    """

    def __init__(self):
        self.dict_generator()
        self.search()

    def search(self):
        s = input("Введите телефон для поиска ->")
        if s in self.d:
            print("Телефон найден!\nАбонент " + self.d[s])
        else:
            print("Абонент не найден, но мы его добавим в систему")
            name = input("Введите ФИО абонента -> ")
            self.d[s] = name

            print("Обновлённый словарь:")
            for k, v in self.d.items():
                print(k, v)


class Task4(object):
    """
    создать словарь на свободную тему, включающий в себя кортеж в качестве ключа, реализовать поиск
    """

    def __init__(self):
        self.d = {}
        self.max_values = 100
        self.hashtable_generator()
        self.results_searcher()

    def all_counter(self, *t):
        res = 0
        for i in t:
            res += i
        return res

    def all_multipy(self, *t):
        res = 1
        for i in t:
            res *= i
        return res

    def hashtable_generator(self):
        for i in range(self.max_values):
            for j in range(self.max_values):
                for k in range(self.max_values):
                    self.d[(i, j, k)] = [
                        {
                            "multiplication": self.all_multipy(i, j, k),
                            "sum": self.all_counter(i, j, k),
                        }
                    ]

    def check_digit(self, e):
        try:
            return int(e)
        except:
            return e

    def results_searcher(self):
        out_str = "Введите 3 числа через пробел от 0 до 100 для быстрого подсчёта их суммы и произведения -> "
        r = self.d[tuple([self.check_digit(x) for x in input(out_str).split(" ")])][0]
        print("Произведение: " + str(r["multiplication"]) + "\nСумма: " + str(r["sum"]))


class Task5(object):
    """
    создать словарь авиарейсов, в возможностью поиска маршрута из точки А в точку В с учётом 1 пересадки
    """

    def __init__(self):
        self.d = {
            "Москва": ["Лондон", "Владивосток", "Санкт-Петербург"],
            "Лондон": ["Москва", "Сингапур"],
            "Сингапур": ["Лондон"],
            "Калининград": ["Санкт-Петербург"],
            "Санкт-Петербург": ["Калининград", "Москва"],
            "Владивосток": ["Москва", "Норильск"],
            "Норильск": ["Владивосток"],
        }
        self.flight_generator()
        self.search()

    def get_random_flight(self):

        letters = string.ascii_uppercase
        chars = "".join(random.choice(letters) for i in range(3))
        numbers = str(random.randint(1000, 9999))
        return chars + "-" + numbers

    def flight_generator(self):
        self.flight_d = {}
        for e in self.d:
            for city in self.d[e]:
                self.flight_d[self.get_random_flight()] = {"from": e, "to": city}

    def search(self):

        search_flag = False
        point_a = input("Введите точку А -> ")
        point_b = input("Введите точку В -> ")

        # Проверка на то, если ли изначальная точка в словаре
        begining_flag = False
        for flight, value in self.flight_d.items():
            if value["from"] == point_a:
                begining_flag = True

        if begining_flag == False:
            print("Нет указанной точки вылета в словаре!")
            return

        # Проверяем на перелёт без вложенности
        for flight, value in self.flight_d.items():
            if value["from"] == point_a and value["to"] == point_b:
                search_flag = True
                print(
                    "План перелёта\nСуществует прямой рейс №"
                    + flight
                    + "\n"
                    + point_a
                    + " -> "
                    + point_b
                )

        if search_flag == False:
            buf_list = []
            for flight, value in self.flight_d.items():
                if value["from"] == point_a:
                    buf_list.append((flight, value["from"], value["to"]))

            for element in buf_list:
                for flight, value in self.flight_d.items():
                    if element[2] == value["from"] and point_b == value["to"]:
                        search_flag = True
                        print(
                            "План перелёта:\nНа рейсе №"
                            + element[0]
                            + " "
                            + element[1]
                            + " -> "
                            + element[2]
                        )
                        print(
                            "На рейсе №"
                            + flight
                            + " "
                            + value["from"]
                            + " -> "
                            + value["to"]
                        )

            if search_flag == False:
                print("По вашему запросу ничего не найдено")


if __name__ == "__main__":
    d = {"1": Task1, "2": Task2, "3": Task3, "4": Task4, "5": Task5}
    s = input("Введите номер задания -> ")
    if s in d:
        d[s]()
    else:
        print("Такого задания нет!")
