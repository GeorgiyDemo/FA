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
                {"begin_time": "21:30", "time_range": 30, "name": "Белорусский вокзал"},
                {"begin_time": "14:40", "time_range": 3, "name": "Баковка"},
                {"begin_time": "10:30", "time_range": 15, "name": "Отрадное"},
            ],

            "Баковка": [
                {"begin_time": "7:45", "time_range": 3, "name": "Одинцово"},
                {"begin_time": "14:20", "time_range": 10, "name": "Курский Вокзал"},
                {"begin_time": "8:10", "time_range": 25, "name": "Савёловский Вокзал"},
            ],
            "Отрадное": [
                {"begin_time": "8:10", "time_range": 15, "name": "Одинцово"},
                {"begin_time": "9:40", "time_range": 60, "name": "Курский Вокзал"},
                {"begin_time": "18:21", "time_range": 38, "name": "Савёловский вокзал"},
            ],
            "Белорусский вокзал": [
                {"begin_time": "11:15", "time_range": 30, "name": "Одинцово"},
                {"begin_time": "13:50", "time_range": 10, "name": "Курский Вокзал"},
                {"begin_time": "20:52", "time_range": 5, "name": "Савёловский вокзал"},
            ],
            "Курский Вокзал": [
                {"begin_time": "17:02", "begin_time": "15:21", "time_range": 10, "name": "Белорусский Вокзал"},
                {"begin_time": "17:10", "time_range": 10, "name": "Баковка"},
                {"begin_time": "15:58", "time_range": 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал": [
                {"begin_time": "11:18", "time_range": 5, "name": "Белорусский вокзал"},
                {"begin_time": "15:26", "time_range": 25, "name": "Баковка"},
                {"begin_time": "19:10", "time_range": 38, "name": "Отрадное"},
            ],
        }
        self.way_inputer()
        self.way_recognizer()
        if self.all_ways_list != []:
            self.time_detector()
            # self.result_outputer()

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
            print(all_ways_list[i])
            # total_time = 0
            # if len(all_ways_list[i]["points"]) > 2:
            #    # Цикл по каждому времени
            #    for time in all_ways_list[i]["times"]:
            #        total_time += time + self.TIME_WAIT
            #    total_time -= self.TIME_WAIT
            # else:
            #    total_time = all_ways_list[i]["times"][0]
            #
            # all_ways_list[i]["times"] = total_time

        # self.all_ways_list = all_ways_list

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
                            "times": [(first_element["time_range"], first_element["begin_time"])],
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
                                    "times": [
                                        (first_element["time_range"], first_element["begin_time"]),
                                        (second_element["time_range"], second_element["begin_time"])
                                    ],
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
                                            "times": [
                                                (first_element["time_range"], first_element["begin_time"]),
                                                (second_element["time_range"], second_element["begin_time"]),
                                                (third_element["time_range"], third_element["begin_time"]),
                                            ],
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
                                                    "times": [
                                                        (first_element["time_range"], first_element["begin_time"]),
                                                        (second_element["time_range"], second_element["begin_time"]),
                                                        (third_element["time_range"], third_element["begin_time"]),
                                                        (fourth_element["time_range"], fourth_element["begin_time"]),
                                                    ],
                                                    "detector_number": 3,
                                                })

            self.all_ways_list = all_ways_list

        else:
            print("Нет исходной точки в начале")


if __name__ == "__main__":
    Task6()
