# TODO Рандомная генерация файла заполнения мест
# TODO Можно обратиться к полю self.content при покупке билетов. Это избавит от повторного чтения файла
"""
Для задания  6 из предыдущей практики реализовать:
[OK]    3.1 применение функций (не менее 5 штук)
    3.2 расписание полетов или поездов задается файлом, свободные места в вашон
       е или салоне указываются в файле (при продаже билета изменяете файл)
    
    3.3 реализовать заполнение шаблонов билетов (шаблон билетов разрабатывается
       самостоятельно) данными о рейсе, ФИО пассажира, вагоне, месте, времени и дат
       е отправления на весь путь(с учетом пересадок)

+ Редактирование и сдачу билетов. Но они есть, не забывайте что в файлах храним информацию 
о пассажирах и при этих операциях требуется изменять данные в соответствующих файлах.
Меню в консоли на выбор действия. При сдаче указаваем процент, который удерживается с пассажира 
(делаем вывод, что стоимость билета нам тоже желательно хранить)

Создать словарь железнодорожных сообщений с учетом более одной но менее 4 пересадок, с рекомендацией оптимального маршрута по времени
Между переходами разница в 30 мин
"""

import datetime
import random
from os import path

import file_writer_module
import texttable
import ticket_module
import universal_module
import waysearcher_module
import yaml


    """
    Проверяет reg_flag, если требуется регенерация с новой датой (т.е. reg_flag == True)
    В условии перегенерирует d с текущей датой и пишет его в файл
    """

    # Формирование нового с новой датой
    if reg_flag == True:
        print("Регенерируем файл с расписанием поездов..")

        date = datetime.datetime.now().date().strftime("%d.%m.%Y ")

        d = {
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
        tt_obj = universal_module.FileClass(file_name)
        tt_obj.set_file(d)

        return d

    return d


class GetAllInfoClass():
    """
    Класс для отдачи всей информации, связанной с именем
    - Время отправления и прибытия поездов
    - Индексы поездов в общем словаре для последующего обращения
    - Информация о билетах: вагон, место, стоимость, тип, оплата
    """

    def __init__(self, d, name):

        # Поля для обращения к ним
        self.ways_index = []
        self.tickets = []

        self.d = d
        self.name = name

        self.d_payment_formater = {
            0: "Ожидает оплаты",
            1: "Оплачено",
        }
        self.check_reservers_by_name()

    def check_reservers_by_name(self):
        """
        Метод находит по ФИО брони все билеты в коллекции
        - Возвращает время отправления и прибытия этих поездов
        - Возвращает индексы
        """

        d = self.d
        ways_index = []
        tickets = []

        for i in range(len(d)):
            train_begin_time = d[i]["time_begin"]
            train_time_finish = d[i]["time_finish"]
            for car in d[i]["train"]:
                for place in d[i]["train"][car]["cars"]:
                    current_place_dict = d[i]["train"][car]["cars"][place]
                    if current_place_dict["name"] == self.name:
                        price_str = str(current_place_dict["price"])

                        ways_index.append(i)
                        tickets.append([
                            d[i]["from"] + " -> " + d[i]["to"],
                            car,
                            place,
                            price_str + " руб.",
                            current_place_dict["type"],
                            self.d_payment_formater[current_place_dict["payment"]],
                            train_begin_time,
                            train_time_finish,
                        ])

        self.ways_index = ways_index
        self.tickets = tickets


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


class MainClass():

    def __init__(self):
        """
        Конструктор класса
        Формирует словарь железнодорожных сообщений + вызов всех методов
        """
        self.file_name = "./yaml/tickets.yml"
        self.tt_file_name = "./yaml/tt.yml"
        # Чтение из YAML
        tt_obj = universal_module.FileClass(self.tt_file_name, 2)
        self.d = tt_obj.get_text()

        tt_gereneration_flag = False
        # Проверка на текущую дату
        for first in self.d:
            for second in self.d[first]:
                buf_date = datetime.datetime.strptime(second["begin_time"], "%d.%m.%Y %H:%M").strftime("%d.%m.%Y")
                date_now = datetime.datetime.now().strftime("%d.%m.%Y")
                if buf_date != date_now:
                    tt_gereneration_flag = True

        self.d = tt_regenerator(self.tt_file_name, self.d, tt_gereneration_flag)

        fileflag = path.exists(self.file_name)
        if fileflag == False:
            FileGeneratorClass(self.d, self.file_name)
        else:
            reg_str = input("Хотите обнулить все забронированные места и перегенерировать исходный файл? (Да/Нет)\n-> ")
            if reg_str == "Y" or reg_str == "y" or reg_str == "Да":
                FileGeneratorClass(self.d, self.file_name)

        self.mainmenu_show()

    def buying_ticket_processing(self):
        """
        Управляющая логика для покупки билетов
        """

        user_input = input("\nХотите купить билет сейчас? (Да/Нет) -> ")
        if user_input == "Да":

            all_ways = self.all_ways
            way_number_input = input("Выберите номер маршрута для покупки -> ")
            if way_number_input in all_ways:

                self.new_name = input("Введите ФИО пассажира -> ")
                print("Загрузка..")
                obj = universal_module.FileClass(self.file_name, 2)
                self.content = obj.get_text()
                processing_ways_list = all_ways[way_number_input]
                auto_selecter_input = input(
                    "Выбор режима покупки\nХотите, чтоб система оформила наиболее дешевые билеты автоматически для каждого отдельного пути?\nЕсли нет, то вам придётся вручную делать оформление каждого отдельного билета (Да/Нет) -> ")

                if auto_selecter_input == "Да":
                    automate_flag = True
                elif auto_selecter_input == "Нет":
                    automate_flag = False
                else:
                    print("Некорректный ввод данных..")
                    return

                for way in processing_ways_list:
                    ticket_module.AddTicketClass(self.content, self.file_name, self.new_name, way[0], way[1],
                                                 automate_flag)

                # print("Хотите купить билет(ы) на весь указанный путь? (Да/Нет)
                # if "Да":
                #   print("Выбор режима покупки\nХотите, чтоб система оформила наиболее дешевые билеты автоматически для каждого отдельного пути? Если нет, то вам придётся вручную делать оформление каждого отдельного билета (Да/Нет) ->")
                #    if "Да":
                #        Автоматически поиск самых дешевых
                #    if "Нет"
                #        Пусть вбивает всё сам

                # ticket_module.AddTicketClass(self.file_name)

            else:
                print("Введенный маршрут не найден")
        else:
            print("Хорошо, вы можете сделать это позже в пункте 'Покупка билетов'")

    def mainmenu_show(self):
        """
        Метод для вывода меню действий, связанных с 3 заданием 5 практики
        """

        input_value = ""
        while input_value != "0":
            menu_str = "\nВыберите действие:\n1. Покупка билетов\n2. Управление моими билетами\n0. Выход из программы\n-> "
            input_value = input(menu_str)

            if input_value == "1":
                obj = waysearcher_module.SearcherClass(self.d)
                all_ways = obj.ways
                if all_ways != {}:
                    # Вынесли логику в отдельный метод
                    self.all_ways = all_ways
                    self.buying_ticket_processing()
                else:
                    print("Маршруты не найдены")

            elif input_value == "2":
                print("Загрузка..")
                obj = universal_module.FileClass(self.file_name, 2)
                self.content = obj.get_text()
                self.new_name = input("Введите ФИО пассажира -> ")

                exit_flag = False
                while exit_flag == False:
                    obj_info = GetAllInfoClass(self.content, self.new_name)
                    ways_indexes = obj_info.ways_index
                    check_name_tuple = obj_info.tickets

                    ticket_list = []
                    if check_name_tuple != []:

                        table = texttable.Texttable(180)
                        table_list = [
                            ["№", "Поезд", "№ вагона", "№ места", "Цена", "Тип места", "Статус", "Время отправления",
                             "Время прибытия"], ]
                        for i in range(len(check_name_tuple)):
                            ticket_list.append(str(i + 1))
                            buf_list = [i + 1] + check_name_tuple[i]
                            table_list.append(buf_list)

                        table.add_rows(table_list)
                        print(table.draw() + "\n")

                        reserve_input = input(
                            "Введите номер бронирования для управления им или 0 для выхода из подменю -> ")
                        if reserve_input == "0":
                            exit_flag = True

                        elif reserve_input in ticket_list:
                            current_reserve = check_name_tuple[int(reserve_input) - 1]
                            # Флаг для проверки на ввод 2 пункта
                            payment_show = False
                            if current_reserve[5] == "Ожидает оплаты":

                                payment_show = True
                                print(
                                    "Бронирование №" + reserve_input + "\nДоступные действия:\n1. Отмена бронирования\n2. Формирование электронного билета\n3. Оплата билета")

                            else:
                                print(
                                    "Бронирование №" + reserve_input + "\nДоступные действия:\n1. Отмена бронирования\n2. Формирование электронного билета")

                            input_command = input("Введите номер действия -> ")

                            way_index = ways_indexes[int(reserve_input) - 1]
                            if input_command == "1":
                                ticket_obj = ticket_module.RemoveTicketClass(self.file_name, self.content,
                                                                             self.new_name, way_index,
                                                                             current_reserve[1], current_reserve[2])
                                self.content = ticket_obj.content

                            elif input_command == "2":

                                # Формируем электронный билет об оплате
                                date_now = datetime.datetime.now().strftime("%H.%M.%S %d:%m:%Y")
                                report_filename = "Электронный билет " + self.new_name + " от " + date_now + ".pdf"
                                header_str = "Электронный билет"
                                main_text_str_name = "ФИО клиента: " + self.new_name + "\nДата и время формирования: " + date_now

                                current_ticket = table_list[int(reserve_input)]

                                main_text_str_ticket = "\nБилет\nСтанция и время отправления: " + \
                                                       self.content[way_index]["from"] + " " + self.content[way_index][
                                                           "time_begin"] + "\n" + "Место и время прибытия: " + \
                                                       self.content[way_index]["to"] + " " + self.content[way_index][
                                                           "time_finish"] + "\nМесто: №" + current_ticket[
                                                           3] + " вагон " + current_ticket[2] + " [" + current_ticket[
                                                           5] + "]"

                                main_text_str_payment = "\nОплата\nСтоимость билета: " + str(
                                    current_ticket[4]) + "\n" + "Статус оплаты: " + current_ticket[6]
                                main_text_str = main_text_str_name + "\n" + main_text_str_ticket + "\n" + main_text_str_payment
                                qr_text = main_text_str
                                PDF_obj = file_writer_module.PDFWriter(header_str, main_text_str, qr_text,
                                                                       report_filename)
                                if PDF_obj.processed_flag == True:
                                    print("Электронный билет сформирован")


                            elif input_command == "3" and payment_show == True:
                                payment_obj = ticket_module.PaymentClass()

                                if payment_obj.result == True:

                                    self.content[way_index]["train"][current_reserve[1]]["cars"][current_reserve[2]][
                                        "payment"] = 1

                                    # Формируем квитанцию об оплате
                                    date_now = datetime.datetime.now().strftime("%H.%M.%S %d:%m:%Y")
                                    report_filename = "Квитанция об оплате " + self.new_name + " от " + date_now + ".pdf"
                                    header_str = "Квитанция об оплате заказа от\n" + date_now
                                    main_text_str_name = "ФИО клиента: " + self.new_name

                                    current_ticket = table_list[int(reserve_input)]
                                    main_text_str_ticket = "\nБилет\nСтанция и время отправления: " + \
                                                           self.content[way_index]["from"] + " " + \
                                                           self.content[way_index][
                                                               "time_begin"] + "\n" + "Место и время прибытия: " + \
                                                           self.content[way_index]["to"] + " " + \
                                                           self.content[way_index]["time_finish"] + "\nМесто: №" + \
                                                           current_ticket[3] + " вагон " + current_ticket[2] + " [" + \
                                                           current_ticket[5] + "]"
                                    main_text_str_payment = "\nОплата\nСтоимость билета: " + str(
                                        current_ticket[4]) + "\n" + "Статус оплаты: ОПЛАЧЕНО"
                                    main_text_str = main_text_str_name + "\n" + main_text_str_ticket + "\n" + main_text_str_payment
                                    qr_text = main_text_str
                                    PDF_obj = file_writer_module.PDFWriter(header_str, main_text_str, qr_text,
                                                                           report_filename)
                                    if PDF_obj.processed_flag == True:
                                        print("Квитанция об оплате успешно сформирована")

                                    # Записываем все в файл
                                    print("Записываем изменения..")
                                    writer_obj = universal_module.FileClass(self.file_name)
                                    writer_obj.set_file(self.content)
                                else:
                                    print("Оплата не прошла..")

                            elif input_command != "0":
                                print("Нет такого пункта в меню")

                        else:
                            print("Введенного номера бронирования не существует")
                        # Проверка на то, что можно выводить в управлении

                    else:
                        print("Броней, связанных с введенными ФИО не найдено")
                        exit_flag = True

            elif input_value != "0":
                print("Такого пункта нет в меню")


if __name__ == "__main__":
    MainClass()
