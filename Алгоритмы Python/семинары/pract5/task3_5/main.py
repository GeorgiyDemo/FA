import random
import string
 
class Task5MainClass(object):
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
        chars = ''.join(random.choice(letters) for i in range(3))
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
                print("План перелёта\nСуществует прямой рейс №" + flight + "\n" + point_a + " -> " + point_b)

        if search_flag == False:
            buf_list = []
            for flight, value in self.flight_d.items():
                if value["from"] == point_a:
                    buf_list.append((flight, value["from"], value["to"]))

            for element in buf_list:
                for flight, value in self.flight_d.items():
                    if element[2] == value["from"] and point_b == value["to"]:
                        search_flag = True
                        print("План перелёта:\nНа рейсе №" + element[0] + " " + element[1] + " -> " + element[2])
                        print("На рейсе №" + flight + " " + value["from"] + " -> " + value["to"])

            if search_flag == False:
                print("По вашему запросу ничего не найдено")

if __name__ == "__main__":
    Task5MainClass()