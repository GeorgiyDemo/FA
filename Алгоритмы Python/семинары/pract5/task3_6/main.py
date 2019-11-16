#TODO Рандомная генерация файла + сохранение расписания в файл
#+ смотри еще один TODO в коде 
"""
Для задания 5 или 6 из предыдущей практики реализовать:
[OK]    3.1 применение функций (не менее 5 штук)
    3.2 расписание полетов или поездов задается файлом, свободные места в вашон
       е или салоне указываются в файле (при продаже билета изменяете файл)
    
    3.3 реализовать заполнение шаблонов билетов (шаблон билетов разрабатывается
       самостоятельно) данными о рейсе, ФИО пассажира, вагоне, месте, времени и дат
       е отправления на весь путь(с учетом пересадок)

+ Редактирование и сдачу билетов. Но они есть, не забывайте что в файлах храним информацию 
о пассажирах и при этих операциях требуется изменять данные в соответствующих файлах.
Меню в консоли на выбор действия. 
При сдаче указаваем процент, который удерживается с пассажира 
(делаем вывод, что стоимость билета нам тоже желательно хранить)




Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
Между переходами разница в 30 мин
"""

import yaml
import random
import datetime
import universal_module
import ticket_module
from os import path

# Время для пересадки между поездами
TIME_WAIT = 30

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
   
   def processing(self):
      
      print("Перегенерация исходного файла..")
      #Каждый путь с каждым поездом и каждым вагоном и каждым местом
      sum_train_list = []
      #Все пути от self.d
      all_train_dict = self.all_train_dict
      
      for first_point in all_train_dict:
         for second_point in all_train_dict[first_point]:
            total_free_places = (self.places_count-1)*(self.car_count-1)
            sum_train_list.append(
                {"from" : first_point, "to" : second_point["name"],"train" : {},"info":{
                    "places_free": total_free_places ,"places_count" : self.places_count-1, "car_count" : self.car_count-1}
                }
            )

      for i in range(len(sum_train_list)):
         
         #Список поезда
         train_dict = {}
         for j in range(self.car_count):

            #Словарь вагонов
            car_places_dict = {"cars" : {}, "places_free" :self.places_count-1}
            place_type_dict = {
                0 : "нижнее (боковое)",
                1 : "верхнее (боковое)",
                2 : "верхнее",
                3 : "нижнее",
                4 : "верхнее",
                5 : "нижнее",
            }
            place_type_counter = 0
            for k in range(self.places_count):
               price = random.randint(999,3300)
               place_type = place_type_dict[place_type_counter]
               car_places_dict["cars"][str(k+1)] = {"name": None, "price":price, "type":place_type, "payment":0}
               place_type_counter +=1
               if place_type_counter == 6:
                   place_type_counter = 0

            train_dict[str(j+1)] = car_places_dict

         sum_train_list[i]["train"] = train_dict
      
      self.result = sum_train_list

   def file_writer(self):
      with open(self.file_name, 'w') as outfile:
         yaml.safe_dump(self.result, outfile, allow_unicode=True)
      print("Перегенерация завершена")

class Task6MainClass():

    def __init__(self):
        """
        Конструктор класса
        Формирует словарь железнодорожных сообщений + вызов всех методов
        """
        self.file_name = "tickets.yml"
        self.all_ways_list = []
        date = datetime.datetime.now().date().strftime("%d.%m.%Y ")
        #TODO Чтение из YAML, если date != текущей date, то регенерейт.
        #Если файла нет, то тоже его заного создаём
        self.d = {
            "Одинцово": [
                {"begin_time": date + "21:30", "time_range": 30, "name": "Белорусский Вокзал"},
                {"begin_time": date + "14:40", "time_range": 3, "name": "Баковка"},
                {"begin_time": date + "10:30", "time_range": 15, "name": "Отрадное"},
            ],

            "Баковка": [
                {"begin_time": date + "07:45", "time_range": 3, "name": "Одинцово"},
                {"begin_time": date + "14:20", "time_range": 10, "name": "Курский Вокзал"},
                {"begin_time": date + "08:10", "time_range": 25, "name": "Савёловский Вокзал"},
            ],
            "Отрадное": [
                {"begin_time": date + "08:10", "time_range": 15, "name": "Одинцово"},
                {"begin_time": date + "09:40", "time_range": 60, "name": "Курский Вокзал"},
                {"begin_time": date + "18:21", "time_range": 38, "name": "Савёловский Вокзал"},
            ],
            "Белорусский Вокзал": [
                {"begin_time": date + "11:15", "time_range": 30, "name": "Одинцово"},
                {"begin_time": date + "13:50", "time_range": 10, "name": "Курский Вокзал"},
                {"begin_time": date + "20:52", "time_range": 5, "name": "Савёловский Вокзал"},
            ],
            "Курский Вокзал": [
                {"begin_time": date + "17:02", "time_range": 10, "name": "Белорусский Вокзал"},
                {"begin_time": date + "17:10", "time_range": 10, "name": "Баковка"},
                {"begin_time": date + "15:58", "time_range": 60, "name": "Отрадное"},
            ],
            "Савёловский Вокзал": [
                {"begin_time": date + "11:18", "time_range": 5, "name": "Белорусский Вокзал"},
                {"begin_time": date + "15:26", "time_range": 25, "name": "Баковка"},
                {"begin_time": date + "19:10", "time_range": 38, "name": "Отрадное"},
            ],
        }

        fileflag = path.exists(self.file_name)
        if fileflag == False:
            FileGeneratorClass(self.d, self.file_name)
        else:
            reg_str = input("Хотите обнулить все забронированные места и перегенерировать исходный файл? (Да/Нет)\n-> ")
            if reg_str == "Y" or reg_str == "y" or reg_str == "Да":
                FileGeneratorClass(self.d, self.file_name)

        self.mainmenu_show()
    
    def mainmenu_show(self):
        """
        Метод для вывода меню действий, связанных с 3 заданием 5 практики
        """
        
        input_value = ""
        while input_value != "0":
            menu_str = "Выберите действие:\n1. Покупка билетов\n2. Управление моими билетами\n0. Выход из программы\n-> "
            input_value = input(menu_str)
            
            if input_value == "1":
                self.way_inputer()
                self.way_recognizer()
                if self.all_ways_list:
                    self.waiting_time_detector()
                    self.main_time_detector()
                    self.result_outputer()
                    #print("Хоите купить билет на путь? (Да/Нет)
                    #if "Да":
                    #   print("Выбор режима покупки\nХотите, чтоб система оформила наиболее дешевые билеты автоматически? Если нет, то вам придётся вручную делать оформление каждого отдельного билета (Да/Нет) ->")
                    #    if "Да":
                    #        Автоматически поиск самых дешевых
                    #    if "Нет"
                    #        Пусть вбивает всё сам

                    #ticket_module.AddTicketClass(self.file_name)
                #
            elif input_value == "2":
                #Вводим фио
                #Ищем билеты по мним
                #Выберите билет (выбираем билет)
                #Доступные действия
                #1. Отмена бронирования
                #2. Оплата билета (появляется если только мы его не оплатили)
                #3. Распечатать билет (????? ПОКА #TODO)
                ticket_module.AddTicketClass(self.file_name)
                ticket_module.RemoveTicketClass(self.file_name)

            elif input_value != "0":
                print("Такого пункта нет в меню")

    def result_outputer(self):
        """
        Вывод всего этого веселья на экран
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
                    if pairs_time[i][0] + datetime.timedelta(minutes=TIME_WAIT) > pairs_time[i][1]:
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


if __name__ == "__main__":
    Task6MainClass()