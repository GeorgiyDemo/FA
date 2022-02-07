"""
Модуль для работы с билетами
- Заказ, бронирование, покупка
- Отмена зказа
"""

import datetime
import time

import file_writer_module
import texttable
import universal_module


class PaymentClass:
    def __init__(self):
        self.payment_processing()
        self.result = True

    def payment_processing(self):
        print("Оплата..\n")
        for i in range(3):
            time.sleep(1)
            print(".")
        print("Оплата прошла успешно!")


def get_min_max_price_of_car(car):
    max_price = car["cars"]["1"]["price"]
    min_price = max_price

    for place in car["cars"]:
        locale_price = car["cars"][place]["price"]
        if locale_price > max_price:
            max_price = locale_price
        if locale_price < min_price:
            min_price = locale_price

    return max_price, min_price


class AddTicketClass:
    """
    Класс для добавления билетов. Выщывается как при прямых рейсов, так и для ресов с пересадками
    """

    def __init__(self, content, file_name, name, way_from, way_to, automate_flag=False):

        self.file_name = file_name
        self.way_from = way_from
        self.way_to = way_to
        self.name = name

        self.content = content

        if automate_flag == True:
            self.auto_components_reserve()
        else:
            self.mechanical_components_reserve()

    def auto_components_reserve(self):
        way_index = 0
        price_dict = {}
        content = self.content
        for i in range(len(content)):
            if content[i]["from"] == self.way_from and content[i]["to"] == self.way_to:
                way_index = i
                for car in content[i]["train"]:
                    for place in content[i]["train"][car]["cars"]:
                        if content[i]["train"][car]["cars"][place]["name"] == None:
                            locale_price = content[i]["train"][car]["cars"][place][
                                "price"
                            ]
                            price_dict[(car, place)] = locale_price

        min_price = price_dict[("1", "1")]
        min_key = ("1", "1")
        for k, v in price_dict.items():
            if v < min_price:
                min_price = v
                min_key = k

        way_index
        price = min_price
        car, place = min_key

        selected_train = content[way_index]
        train_places_free = selected_train["info"]["places_free"] - 1
        car_places_free = selected_train["train"][car]["places_free"] - 1
        print(
            "Зарезервировали "
            + place
            + " место в вагоне "
            + car
            + " по маршруту "
            + selected_train["from"]
            + " -> "
            + selected_train["to"]
            + " за "
            + str(price)
            + " руб"
        )
        print(
            "Отправление в "
            + selected_train["time_begin"]
            + ", прибытие - "
            + selected_train["time_finish"]
        )

        content[way_index]["info"]["places_free"] = train_places_free
        content[way_index]["train"][car]["places_free"] = car_places_free
        content[way_index]["train"][car]["cars"][place]["name"] = self.name
        # Записываем все в файл
        writer_obj = universal_module.FileClass(self.file_name)
        writer_obj.set_file(content)
        self.content = content

    def mechanical_components_reserve(self):
        """
        Выбор вагона для брони в поезде
        """
        exit_flag = False
        while exit_flag == False:
            content = self.content

            for i in range(len(content)):
                if (
                    content[i]["from"] == self.way_from
                    and content[i]["to"] == self.way_to
                ):
                    print(
                        "Поезд найден " + content[i]["from"] + " -> " + content[i]["to"]
                    )
                    print(
                        "Всего в поезде "
                        + str(content[i]["info"]["car_count"])
                        + " вагонов и "
                        + str(content[i]["info"]["places_free"])
                        + " свободных мест\nМест по вагонам:"
                    )
                    table = texttable.Texttable(180)
                    table_list = [
                        ["Вагон", "Мест свободно", "Диапазон цен на места"],
                    ]

                    buf_car_list = []

                    for car in content[i]["train"]:
                        price_min, price_max = get_min_max_price_of_car(
                            content[i]["train"][car]
                        )
                        price_range = str(price_max) + " - " + str(price_min) + " руб."
                        table_list.append(
                            [car, content[i]["train"][car]["places_free"], price_range]
                        )
                        buf_car_list.append(car)

                    # Вывод
                    table.add_rows(table_list)
                    print(table.draw() + "\n")

                    selected_car = input("Выберите вагон (0 для выхода из подменю) -> ")
                    if selected_car == "0":
                        exit_flag = True
                    elif selected_car in buf_car_list:
                        self.place_searcher(i, selected_car)
                    else:
                        print("Нет такого вагона, выход из подпрограммы..")
                        exit_flag = True
            self.content = content

    def place_searcher(self, way, selected_car):
        """
        Выбор места в вагоне для брони
        """
        exit_flag = False

        while exit_flag == False:
            content = self.content
            table = texttable.Texttable(180)
            print("Места в вагоне:")
            table_list = [
                ["№", "Статус", "Цена", "Тип"],
            ]
            buf_place_list = []
            for place in content[way]["train"][selected_car]["cars"]:
                buf_place_list.append(place)
                locale_place = content[way]["train"][selected_car]["cars"][place]

                reserved_type = "свободно"
                if locale_place["name"] != None:
                    reserved_type = "забронировано"
                price = str(locale_place["price"]) + " руб."
                table_list.append([place, reserved_type, price, locale_place["type"]])

            table.add_rows(table_list)
            print(table.draw() + "\n")

            selected_place = input(
                "Введите номер места для бронирования (0 для выхода из подменю) -> "
            )
            if selected_place == "0":
                exit_flag = True
            elif selected_place in buf_place_list:
                if (
                    content[way]["train"][selected_car]["cars"][selected_place]["name"]
                    == None
                ):
                    question_string = (
                        "Вы действительно хотите забронировать место №"
                        + selected_place
                        + " в вагоне "
                        + selected_car
                        + " поезда "
                        + self.way_from
                        + " - "
                        + self.way_to
                        + " на имя '"
                        + self.name
                        + "'? (Да/Нет) -> "
                    )
                    user_reply = input(question_string)
                    if user_reply == "Да" or user_reply == "Y" or user_reply == "y":

                        # Успешно меняем текущий словарь
                        content[way]["train"][selected_car]["cars"][selected_place][
                            "name"
                        ] = self.name
                        question_input = input(
                            "Место успешно зарезервировано\nОплатить его сейчас? Да/Нет -> "
                        )
                        if question_input == "Да":
                            pay_obj = PaymentClass()
                            if pay_obj.result == True:
                                # Устанавливаем флаг того, что мы всё оплатили
                                content[way]["train"][selected_car]["cars"][
                                    selected_place
                                ]["payment"] = 1

                                # Формируем квитанцию об оплате
                                date_now = datetime.datetime.now().strftime(
                                    "%H.%M.%S %d:%m:%Y"
                                )
                                report_filename = (
                                    "Квитанция об оплате "
                                    + self.name
                                    + " от "
                                    + date_now
                                    + ".pdf"
                                )
                                header_str = (
                                    "Квитанция об оплате заказа от\n" + date_now
                                )
                                main_text_str_name = "ФИО клиента: " + self.name

                                buf_place = content[way]["train"][selected_car]["cars"][
                                    selected_place
                                ]

                                main_text_str_ticket = (
                                    "\nБилет\nСтанция и время отправления: "
                                    + content[way]["from"]
                                    + " "
                                    + content[way]["time_begin"]
                                    + "\n"
                                    + "Место и время прибытия: "
                                    + content[way]["to"]
                                    + " "
                                    + content[way]["time_finish"]
                                    + "\nМесто: №"
                                    + selected_place
                                    + " вагон "
                                    + selected_car
                                    + " ["
                                    + buf_place["type"]
                                    + "]"
                                )
                                main_text_str_payment = (
                                    "\nОплата\nСтоимость билета: "
                                    + str(buf_place["price"])
                                    + " руб. \n"
                                    + "Статус оплаты: ОПЛАЧЕНО"
                                )
                                main_text_str = (
                                    main_text_str_name
                                    + "\n"
                                    + main_text_str_ticket
                                    + "\n"
                                    + main_text_str_payment
                                )
                                qr_text = main_text_str
                                PDF_obj = file_writer_module.PDFWriter(
                                    header_str, main_text_str, qr_text, report_filename
                                )
                                if PDF_obj.processed_flag == True:
                                    print("Квитанция об оплате успешно сформирована")

                        elif question_input == "Нет":
                            print(
                                "Хорошо, оплатить билет вы можете позже в пункте 'Управление моими билетами'"
                            )

                        # Обновляем количество мест
                        train_places_free = content[way]["info"]["places_free"] - 1
                        car_places_free = (
                            content[way]["train"][selected_car]["places_free"] - 1
                        )

                        content[way]["info"]["places_free"] = train_places_free
                        content[way]["train"][selected_car][
                            "places_free"
                        ] = car_places_free

                        # Записываем все в файл
                        writer_obj = universal_module.FileClass(self.file_name)
                        writer_obj.set_file(content)

                else:
                    print("Введенное место уже забронировано")
            else:
                print("Введенное место не найдено, выход из подпрограммы..")
                exit_flag = True
            self.content = content


class RemoveTicketClass:
    """
    Класс для отмены бронирования билетов
    """

    def __init__(self, file_name, content, name, way, car, place):
        self.file_name = file_name
        self.content = content
        self.name = name
        self.way = way
        self.car = car
        self.place = place
        self.refund_percent = 5

        self.ticket_remover()

    def ticket_remover(self):

        print("Отмена бронирования..")
        percent = self.refund_percent
        content = self.content
        way = self.way
        car = self.car
        place = self.place

        way_str = content[way]["from"] + " -> " + content[way]["to"]
        selected_place = content[way]["train"][car]["cars"][place]
        percent_price = (selected_place["price"] / 100) * percent
        refound_price = selected_place["price"] - percent_price

        refound_str = (
            "Вам вернется "
            + str(refound_price)
            + " руб. Сервис удержит комиссию в виде "
            + str(percent_price)
            + " руб."
        )
        place_str = (
            "\nВы действительно хотите отменить бронирование на "
            + place
            + " место "
            + car
            + " вагона поезда "
            + way_str
            + " ? (Да/Нет) -> "
        )

        confirm_input = input(refound_str + place_str)
        if confirm_input == "Да" or confirm_input == "Y" or confirm_input == "y":

            selected_place["payment"] = 0
            selected_place["name"] = None

            # Обновляем количество мест
            train_places_free = content[way]["info"]["places_free"] + 1
            car_places_free = content[way]["train"][car]["places_free"] + 1

            content[way]["info"]["places_free"] = train_places_free
            content[way]["train"][car]["places_free"] = car_places_free

            date_now = datetime.datetime.now().strftime("%H.%M.%S %d:%m:%Y")
            report_filename = "Возврат " + self.name + " от " + date_now + ".pdf"
            header_str = "Документ об оформлении возврата срeдств от\n" + date_now

            main_text_str_name = "ФИО клиента: " + self.name
            main_text_str_ticket = (
                "\nБилет\nСтанция и время отправления: "
                + content[way]["from"]
                + " "
                + content[way]["time_begin"]
                + "\n"
                + "Место и время прибытия: "
                + content[way]["to"]
                + " "
                + content[way]["time_finish"]
                + "\nМесто: №"
                + place
                + " вагон "
                + car
                + " ["
                + selected_place["type"]
                + "]"
            )
            main_text_str_payment = (
                "\nВозврат средств\nСтоимость билета: "
                + str(selected_place["price"])
                + " руб. \n"
                + "Стоимость комиссии: "
                + str(percent_price)
                + " руб. \nВозвращённая сумма: "
                + str(refound_price)
                + " руб."
            )
            main_text_str = (
                main_text_str_name
                + "\n"
                + main_text_str_ticket
                + "\n"
                + main_text_str_payment
            )
            qr_text = main_text_str

            PDF_obj = file_writer_module.PDFWriter(
                header_str, main_text_str, qr_text, report_filename
            )
            if PDF_obj.processed_flag == True:
                print("Документ о возврате успешно сформирован")

            content[way]["train"][car]["cars"][place] = selected_place
            print("Запиcь изменений..")
            writer_obj = universal_module.FileClass(self.file_name)
            writer_obj.set_file(content)
            self.content = content
            print("Успешно")

        else:
            print("Хорошо, все оставили без изменений")
