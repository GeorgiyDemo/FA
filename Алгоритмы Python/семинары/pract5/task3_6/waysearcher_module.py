"""
Модуль для поиска наиболее рациональных путей по веремени.
Неокогда основной процессинг 4 практики 6 задания
"""
import datetime
import universal_module
class SearcherClass():
    def __init__(self, d):
        self.d = d
        self.TIME_WAIT = 30
        self.all_ways_list = []
        self.way_inputer()
        self.way_recognizer()

        #Поля для последующего обращения с main
        self.ways = {}

        if self.all_ways_list:
            self.waiting_time_detector()
            self.main_time_detector()
            self.result_outputer()
            self.ways_outer()

    def ways_outer(self):
        """
        Метод необходим для формирования словаря self.ways со всеми путями
        """
        locale_ways = {}
        r = self.final_out_list
        for i in range(len(r)):
            buf_list = []
            for e in r[i]["ways"]:
                buf_list.append([e["way_from"], e["way_to"]])
            
            locale_ways[str(i + 1)] = buf_list
        self.ways = locale_ways


    def waiting_time_detector(self):
        """
        Метод для определения времени ожидания след поезда между станциями + TIME_WAIT мин на пересадку
        """

        all_ways_list = self.all_ways_list
        all_wait_list = []

        for way in all_ways_list:
            # Словарь для хранения маршрутов и времени для дальнейшего вывода
            wait_dict = {"ways": []}
            # Список с парами прибытия предыдущего и отправления следующего поезда
            pairs_time = []
            # Т.к. есть прямой маршрут, то время одно от точки 0 до 1
            # Индивидуальный подход кароч, если маршрут прямой
            if len(way["times"]) == 1:
                pairs_time.append([way["times"][0][0], way["times"][0][1]])

                if pairs_time[0][0] > pairs_time[0][1]:
                    pairs_time[0][1] = pairs_time[0][1] + datetime.timedelta(days=1)
                    total_time = pairs_time[0][1] - pairs_time[0][0]
                else:
                    total_time = pairs_time[0][1] - pairs_time[0][0]
                wait_dict["ways"].append({"point": way["points"], "time": total_time})
            else:
                for i in range(1, len(way["times"])):
                    pairs_time.append([way["times"][i - 1][1], way["times"][i][0]])

                for i in range(len(pairs_time)):

                    # Если не успевает на след поезд от премени предыдущего поезда + 30 мин, то + 24 часа
                    if pairs_time[i][0] + datetime.timedelta(minutes=self.TIME_WAIT) > pairs_time[i][1]:
                        pairs_time[i][1] = pairs_time[i][1] + datetime.timedelta(days=1)
                        diff_time = pairs_time[i][1] - pairs_time[i][0]

                    else:
                        diff_time = pairs_time[i][1] - pairs_time[i][0]

                    wait_dict["ways"].append({"point": way["points"][i + 1], "time": diff_time})

            all_wait_list.append(wait_dict)
        self.all_wait_list = all_wait_list

    def way_inputer(self):
        """
        Ввод данных
        """

        self.point_a = input("Введите точку А -> ")
        self.point_b = input("Введите точку В -> ")

    def way_recognizer(self):
        """
        Метод для поиска маршрутов по словарю d
        Заносит результаты вычислений в all_ways_list
        """

        d = self.d
        point_a = self.point_a
        point_b = self.point_b

        all_ways_list = []

        if point_a in d:

            for first_element in d[point_a]:

                if first_element["name"] == point_b:
                    print("[Вложенность 0] " + point_a + " - > " + first_element["name"])

                    all_ways_list.append(
                        dict(points=[point_a, first_element["name"]], times=universal_module.UniversalClass.get_train_time(
                            (first_element["time_range"], first_element["begin_time"])), detector_number=0))

                if first_element["name"] in d:
                    for second_element in d[first_element["name"]]:
                        if second_element["name"] == point_b:
                            print("[Вложенность 1] " + point_a + " - > " + first_element["name"] + " -> " +
                                  second_element["name"])

                            all_ways_list.append(
                                dict(points=[point_a, first_element["name"], second_element["name"]],
                                     times=universal_module.UniversalClass.get_train_time(
                                         (first_element["time_range"], first_element["begin_time"]),
                                         (second_element["time_range"], second_element["begin_time"])
                                     ), detector_number=1))

                        if second_element["name"] in d:
                            for third_element in d[second_element["name"]]:
                                if third_element["name"] == point_b:
                                    print("[Вложенность 2] " + point_a + " - > " + first_element["name"] + " -> " +
                                          second_element["name"] + " -> " + third_element["name"])
                                    all_ways_list.append(
                                        {
                                            "points": [point_a, first_element["name"], second_element["name"],
                                                       third_element["name"]],
                                            "times": universal_module.UniversalClass.get_train_time(
                                                (first_element["time_range"], first_element["begin_time"]),
                                                (second_element["time_range"], second_element["begin_time"]),
                                                (third_element["time_range"], third_element["begin_time"]),
                                            ),
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
                                                    "times": universal_module.UniversalClass.get_train_time(
                                                        (first_element["time_range"], first_element["begin_time"]),
                                                        (second_element["time_range"], second_element["begin_time"]),
                                                        (third_element["time_range"], third_element["begin_time"]),
                                                        (fourth_element["time_range"], fourth_element["begin_time"]),
                                                    ),
                                                    "detector_number": 3,
                                                })

            self.all_ways_list = all_ways_list

        else:
            print("Нет исходной точки в начале")

    def result_outputer(self):
        """
        Вывод всех результатов на экран + отдача значений в self.ways
        """
        r = self.final_out_list
        for i in range(len(r)):
            print("\n" + "*" * 10 + "Маршрут №" + str(i + 1) + "*" * 10)
            print(universal_module.UniversalClass.get_ways_string(r[i]["ways"]))
            print("Общее время: "+str(r[i]["total_time"]))
            for way in r[i]["ways"]:
                print(way["way_from"]+" -> "+way["way_to"]+", время: "+str(way["train_time"]))
                if way["waiting_time"] is not None:
                    print("Ожидание: "+str(way["waiting_time"]))

    def main_time_detector(self):

        """
        Метод вычисляет общее время, которое включает в себя:
         - Время поездки на поезда
         - Время ожидания между поездами
        Формуирет форматированный список рейсов, отсортированных по убыванию
        """

        all_ways_list = self.all_ways_list
        all_wait_list = self.all_wait_list

        out_list = []

        for i in range(len(all_ways_list)):

            final_way = {"total_time": None, "ways": []}

            points = all_ways_list[i]["points"]
            times = all_ways_list[i]["times"]
            total_time = None
            little_way_dict = []
            for j in range(len(times)):
                train_time = times[j][1] - times[j][0]
                checked_value = universal_module.UniversalClass.detect_station_waiting_time(points[j + 1], all_wait_list[i])

                if checked_value[0]:
                    little_way_dict.append({"way_from": points[j], "way_to": points[j + 1], "train_time": train_time,
                                            "waiting_time": checked_value[1]})
                    train_time += checked_value[1]
                else:
                    little_way_dict.append({"way_from": points[j], "way_to": points[j + 1], "train_time": train_time,
                                            "waiting_time": None})

                if total_time is None:
                    total_time = train_time
                else:
                    total_time += train_time

            final_way["total_time"] = total_time
            final_way["ways"] = little_way_dict
            out_list.append(final_way)
            out_list.sort(key=lambda x: (x["total_time"]))

        self.final_out_list = out_list