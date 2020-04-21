import datetime
import random

import yaml


class FileGeneratorClass():
    """
    Класс-генератор свободных мест на рейсы и запись в файл
    """

    def __init__(self, all_train_dict, file_name, places_count=55, car_count=16):

        self.file_name = file_name
        self.all_train_dict = all_train_dict
        self.places_count = places_count
        self.car_count = car_count
        self.processing()
        self.file_writer()

    def get_time_ranges(self, train):
        """
        Возврат диапазонов времени отправлений поезда
        - Принимает словарь поезда
        - Отдаёт временные промежутки отправления и прибытия поезда
        """
        train_begin_time = datetime.datetime.strptime(train["begin_time"], "%d.%m.%Y %H:%M")
        train_begin_time_str = train_begin_time.strftime("%H:%M:%S %d/%m/%Y")
        train_finish_time = train_begin_time + datetime.timedelta(minutes=train["time_range"])
        train_finish_time_str = train_finish_time.strftime("%H:%M:%S %d/%m/%Y")
        return train_begin_time_str, train_finish_time_str

    def processing(self):

        print("Перегенерация исходного файла..")
        # Каждый путь с каждым поездом и каждым вагоном и каждым местом
        sum_train_list = []
        # Все пути от self.d
        all_train_dict = self.all_train_dict

        for first_point in all_train_dict:
            for second_point in all_train_dict[first_point]:
                time_begin, time_finish = self.get_time_ranges(second_point)
                total_free_places = (self.places_count - 1) * (self.car_count - 1)
                sum_train_list.append(
                    {
                        "from": first_point,
                        "to": second_point["name"],
                        "time_begin": time_begin,
                        "time_finish": time_finish,
                        "train": {},
                        "info":
                            {
                                "places_free": total_free_places,
                                "places_count": self.places_count - 1,
                                "car_count": self.car_count - 1,
                            }
                    }
                )

        for i in range(len(sum_train_list)):

            # Список поезда
            train_dict = {}
            for j in range(self.car_count):

                # Словарь вагонов
                car_places_dict = {"cars": {}, "places_free": self.places_count - 1}
                place_type_dict = {
                    0: "нижнее (боковое)",
                    1: "верхнее (боковое)",
                    2: "верхнее",
                    3: "нижнее",
                    4: "верхнее",
                    5: "нижнее",
                }
                place_type_counter = 0
                for k in range(self.places_count):
                    price = random.randint(999, 3300)
                    place_type = place_type_dict[place_type_counter]
                    car_places_dict["cars"][str(k + 1)] = {"name": None, "price": price, "type": place_type,
                                                           "payment": 0}
                    place_type_counter += 1
                    if place_type_counter == 6:
                        place_type_counter = 0

                train_dict[str(j + 1)] = car_places_dict

            sum_train_list[i]["train"] = train_dict

        self.result = sum_train_list

    def file_writer(self):
        with open(self.file_name, 'w') as outfile:
            yaml.safe_dump(self.result, outfile, allow_unicode=True)
        print("Перегенерация завершена")
