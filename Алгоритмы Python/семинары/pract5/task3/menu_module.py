import waysearcher_module
import file_writer_module
import universal_module
import texttable
import ticket_module
import datetime

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

class MenuShower():
    def __init__(self, d, file_name):
        self.d = d
        self.file_name = file_name
        self.mainmenu_show()

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

                

            else:
                print("Введенный маршрут не найден")
        else:
            print("Хорошо, вы можете сделать это позже в пункте 'Покупка билетов'")
