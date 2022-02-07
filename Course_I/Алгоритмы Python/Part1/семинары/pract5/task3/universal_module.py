import datetime

import yaml


class FileClass:
    """
    Класс для работы с файлом file_name, который передаётся в конструктр из main
    - Записывает данные в файл
    - Читает данные из файла
    """

    def __init__(self, file_name, method=1):
        self.file_name = file_name

        if method == 2:
            self.read_file()

    def set_file(self, content):
        with open(self.file_name, "w") as outfile:
            yaml.safe_dump(content, outfile, allow_unicode=True)

    def read_file(self):
        with open(self.file_name, "r") as outfile:
            self.content = yaml.safe_load(outfile)

    def get_text(self):
        return self.content


class UniversalClass:
    @staticmethod
    def get_train_time(*time_ranges):
        """
        Метод для вычисления времени прибытия поезда
        Необходим для проверки на то, успевает ли человек на свой поезд
        """
        out_list = []
        for time_range in time_ranges:
            time = time_range[0]
            begin_time = time_range[1]

            train_begin_time = datetime.datetime.strptime(begin_time, "%d.%m.%Y %H:%M")
            train_arrive_time = train_begin_time + datetime.timedelta(minutes=time)

            out_list.append((train_begin_time, train_arrive_time))
        return out_list

    @staticmethod
    def detect_station_waiting_time(station_name, all_wait_list):
        """
        Определяем, есть ли станция в словаре ожидания
        - Если есть такая станция, то отдаём True и время ожидания
        - Если нет, то False и None
        """
        for way in all_wait_list["ways"]:
            if station_name == way["point"]:
                return True, way["time"]
        return False, None

    @staticmethod
    def get_ways_string(ways_list):
        """
        Отдаёт единую строку путей для красивого вывода в result_outputer
        """
        buf_list = []
        for e in ways_list:
            buf_list.extend([e["way_from"], e["way_to"]])
        results = []
        for item in buf_list:
            if results and item == results[-1]:
                results.pop()
            results.append(item)
        return " -> ".join(results)
