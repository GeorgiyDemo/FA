class Task6():
    """
    Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
    Между переходами разница в 30 мин
    """

    def __init__(self):
        self.TIME_WAIT = 30
        self.all_ways_list = []
        self.d = {
            "Одинцово": [
                {"time": 30, "name": "Белорусский вокзал"},
                {"time": 3, "name": "Баковка"},
                {"time": 15, "name": "Отрадное"},
            ],

            "Баковка": [
                {"time": 3, "name": "Одинцово"},
                {"time": 10, "name": "Курский Вокзал"},
                {"time": 25, "name": "Савёловский Вокзал"},
            ],
            "Отрадное": [
                {"time": 15, "name": "Одинцово"},
                {"time": 60, "name": "Курский Вокзал"},
                {"time": 38, "name": "Савёловский вокзал"},
            ],
            "Белорусский вокзал": [
                {"time": 30, "name": "Одинцово"},
                {"time": 10, "name": "Курский Вокзал"},
                {"time": 5, "name": "Савёловский вокзал"},
            ],
            "Курский Вокзал": [
                {"time": 10, "name": "Белорусский Вокзал"},
                {"time": 10, "name": "Баковка"},
                {"time": 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал": [
                {"time": 5, "name": "Белорусский вокзал"},
                {"time": 25, "name": "Баковка"},
                {"time": 38, "name": "Отрадное"},
            ],
        }
        self.way_inputer()
        self.way_recognizer()
        if self.all_ways_list != []:
            self.time_detector()
            self.result_outputer()

    def result_outputer(self):
        self.all_ways_list.sort(key=lambda x: (x["times"]))
        for e in self.all_ways_list:
            buf_out = ""
            for way in e["points"]:
                buf_out += way + " -> "
            buf_out = buf_out[:len(buf_out) - 4]
            print("*" * 40 + "\nПуть:\n" + buf_out)
            print("Время: " + str(e["times"]) + " минут")

    def time_detector(self):

        all_ways_list = self.all_ways_list

        for i in range(len(all_ways_list)):
            total_time = 0
            if len(all_ways_list[i]["points"]) > 2:
                # Цикл по каждому времени
                for time in all_ways_list[i]["times"]:
                    total_time += time + self.TIME_WAIT
                total_time -= self.TIME_WAIT
            else:
                total_time = all_ways_list[i]["times"][0]

            all_ways_list[i]["times"] = total_time

        self.all_ways_list = all_ways_list

    def way_inputer(self):

        self.point_a = input("Введите точку А -> ")
        self.point_b = input("Введите точку В -> ")

    def way_recognizer(self):

        d = self.d
        point_a = self.point_a
        point_b = self.point_b

        all_ways_list = []

        if point_a in d:

            for first_element in d[point_a]:

                if first_element["name"] == point_b:
                    print("[Вложенность 0] " + point_a + " - > " + first_element["name"])
                    all_ways_list.append(
                        {
                            "points": [point_a, first_element["name"]],
                            "times": [first_element["time"]],
                            "detector_number": 0,
                        })

                if first_element["name"] in d:
                    for second_element in d[first_element["name"]]:
                        if second_element["name"] == point_b:
                            print("[Вложенность 1] " + point_a + " - > " + first_element["name"] + " -> " +
                                  second_element["name"])
                            all_ways_list.append(
                                {
                                    "points": [point_a, first_element["name"], second_element["name"]],
                                    "times": [first_element["time"], second_element["time"]],
                                    "detector_number": 1,
                                })

                        if second_element["name"] in d:
                            for third_element in d[second_element["name"]]:
                                if third_element["name"] == point_b:
                                    print("[Вложенность 2] " + point_a + " - > " + first_element["name"] + " -> " +
                                          second_element["name"] + " -> " + third_element["name"])
                                    all_ways_list.append(
                                        {
                                            "points": [point_a, first_element["name"], second_element["name"],
                                                       third_element["name"]],
                                            "times": [first_element["time"], second_element["time"],
                                                      third_element["time"]],
                                            "detector_number": 2,
                                        })

                                if third_element["name"] in d:
                                    for fourth_element in d[third_element["name"]]:
                                        if fourth_element["name"] == point_b:
                                            print("[Вложенность 3] " + point_a + " - > " + first_element[
                                                "name"] + " -> " + second_element["name"] + " -> " + third_element[
                                                      "name"] + " -> " + fourth_element["name"])
                                            all_ways_list.append(
                                                {
                                                    "points": [point_a, first_element["name"], second_element["name"],
                                                               third_element["name"], fourth_element["name"]],
                                                    "times": [first_element["time"], second_element["time"],
                                                              third_element["time"], fourth_element["time"]],
                                                    "detector_number": 3,
                                                })

            self.all_ways_list = all_ways_list

        else:
            print("Нет исходной точки в начале")


if __name__ == "__main__":
    Task6()
