class Task6():
    TIME_WAIT = 30
    """
    Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
    Между переходами разница в 30 мин
    """
    def __init__(self):

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
                {"time" : 30, "name": "Савёловский вокзал"},
                {"time" : 10, "name": "Баковка"},
                {"time" : 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал":[
                {"time" : 30, "name": "Курский вокзал"},
                {"time" : 5,"name" : "Белорусский вокзал"},
                {"time" : 25, "name": "Баковка"},
                {"time" : 38, "name": "Отрадное"},
            ],
        }
        self.time_recognizer()


#TODO Рекурсивный поиск элементов
    def checker(self, elements, b):
        detect_flag = False
        for item in elements:
            if item["name"] == b:
                print(item["name"])
                detect_flag = True
            
        if detect_flag == False:
            self.checker(self.d[item["name"]], b)
        else:
            return

    def time_recognizer(self):
        d = self.d
        point_a = input("Введите точку А -> ")
        point_b = input("Введите точку В -> ")

        if point_a in d:
            self.checker(d[point_a], point_b)
        else:
            print("Нет исходной точки в начале")

if __name__ == "__main__":
    Task6()