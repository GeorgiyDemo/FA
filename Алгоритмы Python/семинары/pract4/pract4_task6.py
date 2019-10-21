#TODO Сделать 4 уровень + учёт времени 

class Task6():
    TIME_WAIT = 30
    """
    Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
    Между переходами разница в 30 мин
    """
    def __init__(self):
        self.way_list = {}
        self.d = {
            "Одинцово":[
                {"time" : 30, "name": "Белорусский вокзал"},
                {"time" : 3, "name": "Баковка"},
                {"time" : 15, "name": "Отрадное"},
            ],

            "Баковка":[
                {"time" : 3, "name": "Одинцово"},
                {"time" : 10, "name": "Курский Вокзал"},
                {"time" : 25, "name": "Савёловский Вокзал"},
            ],
            "Отрадное":[
                {"time" : 15, "name": "Одинцово"},
                {"time" : 60, "name": "Курский Вокзал"},
                {"time" : 38, "name": "Савёловский вокзал"},
            ],
            "Белорусский вокзал":[
                {"time" : 30, "name": "Одинцово"},
                {"time" : 10, "name" : "Курский Вокзал"},
                {"time" : 5,"name" : "Савёловский вокзал"},
            ],
            "Курский Вокзал":[
                {"time" : 10, "name" : "Белорусский Вокзал"},
                {"time" : 10, "name": "Баковка"},
                {"time" : 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал":[
                {"time" : 5,"name" : "Белорусский вокзал"},
                {"time" : 25, "name": "Баковка"},
                {"time" : 38, "name": "Отрадное"},
            ],
        }
        self.time_recognizer()

    def time_recognizer(self):
        d = self.d
        point_a = input("Введите точку А -> ")
        point_b = input("Введите точку В -> ")

        all_ways_list = []

        if point_a in d:

            for first_element in d[point_a]:

                if first_element["name"] == point_b:

                    print(point_a+" - > "+first_element["name"])
                    all_ways_list.append([point_a,first_element["name"]])
                    print("ПРИЕХАЛИ 0 ")

                if first_element["name"] in d:
                    for second_element in d[first_element["name"]]:
                        if second_element["name"] == point_b:
                            print(point_a+" - > "+first_element["name"]+" -> "+second_element["name"])
                            all_ways_list.append([point_a,first_element["name"],second_element["name"]])
                            print("ПРИЕХАЛИ 1")
                        
                        if second_element["name"] in d:
                            for third_element in d[second_element["name"]]:
                                if third_element["name"] == point_b:
                                    print(point_a+" - > "+first_element["name"]+" -> "+second_element["name"]+" -> "+third_element["name"])
                                    all_ways_list.append([point_a,first_element["name"],second_element["name"],third_element["name"]])
                                    print("ПРИЕХАЛИ 2") 

        else:
            print("Нет исходной точки в начале")
        
        print(all_ways_list)

if __name__ == "__main__":
    Task6()