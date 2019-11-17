"""
Модуль для работы с билетами
- Заказ, бронирование, покупка
- Отмена зказа
"""
#TODO красивые таблицы
import yaml
import time
import universal_module

class PaymentClass():

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

class AddTicketClass():
    """
    Класс для добавления билетов. Выщывается как при прямых рейсов, так и для ресов с пересадками
    #TODO В конструкторе ввести поля для автобронирования мест при использовании пункта 1
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
        #TODO
        print("Зарезервировали билет по маршруту МОСКВА - САНКТ-ПЕТЕРБУРГ ЗА 228 руб..")

    def mechanical_components_reserve(self):
        """
        Выбор вагона для брони в поезде
        #TODO Проверка, если нет таких поездов совсем + выбор поезда на пути
        """

        content = self.content

        for i in range(len(content)):
            if content[i]["from"] == self.way_from and content[i]["to"] == self.way_to:
                print("Поезд найден "+content[i]["from"]+" -> "+content[i]["to"])
                print("Всего в поезде "+str(content[i]["info"]["car_count"])+" вагонов и "+str(content[i]["info"]["places_free"])+" свободных мест")
                
                print('\nМест по вагонам:\n{0:<10} {1:>10} {2:>25}'.format("Вагон", "Мест свободно", "Диапазон цен на места"))
                buf_car_list = []

                for car in content[i]["train"]:
                    price_min, price_max = get_min_max_price_of_car(content[i]["train"][car])
                    price_range = str(price_max) + " - "+ str(price_min)+" руб."
                    print('{0:<10} {1:>10} {2:>25}'.format(car, content[i]["train"][car]["places_free"],price_range))
                    buf_car_list.append(car)
                
                selected_car = input("Выберите вагон -> ")
                if selected_car in buf_car_list:
                    self.place_searcher(i,selected_car)
                else:
                    print("Нет такого вагона, выход из подпрограммы..")
    
    def place_searcher(self, way, selected_car):
        """
        Выбор места в вагоне для брони
        """
        print('Места в вагоне:\n{0:<10} {1:>10} {2:>15} {3:>20}'.format("№", "Статус", "Цена", "Тип"))
        content = self.content
        buf_place_list = []
        for place in content[way]["train"][selected_car]["cars"]:
            buf_place_list.append(place)
            locale_place = content[way]["train"][selected_car]["cars"][place]
            
            reserved_type = "свободно"
            if locale_place["name"] != None:
                reserved_type = "забронировано"
            price = str(locale_place["price"])+" руб."

            print('{0:<10} {1:>10} {2:>15} {3:>20}'.format(place, reserved_type, price, locale_place["type"]))
        
        selected_place = input("Введите номер места для бронирования ->")
        if selected_place in buf_place_list:
            question_string = "Вы действительно хотите забронировать место №"+selected_place+"в вагоне "+selected_car+" поезда "+self.way_from+" - "+self.way_to+" на имя '"+self.name+"'? (Да/Нет)\n->"
            user_reply = input(question_string)
            if user_reply == "Да" or user_reply == "Y" or user_reply == "y":
                #Успешно меняем текущий словарь
                self.content[way]["train"][selected_car]["cars"][selected_place]["name"] = self.name
                question_input = input("Место успешно зарезервировано\nОплатить его сейчас? Да/Нет -> ")
                if question_input == "Да":
                    pay_obj = PaymentClass()
                    if pay_obj.result == True:
                        #Устанавливаем флаг того, что мы всё оплатили
                        self.content[way]["train"][selected_car]["cars"][selected_place]["payment"] = 1
                elif question_input == "Нет":
                    print("Хорошо, оплатить билет вы можете позже в пункте 2 'Управление моими билетами'")
                
                #Записываем все в файл
                writer_obj = universal_module.FileClass(self.file_name)
                writer_obj.set_file(self.content)
        else:
            print("Введенное место не найдено, выход из подпрограммы..")

class RemoveTicketClass():

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
        #делает None на место + обращается к universal_module.FileClass для записи обновлённого файла
        
        print("Отмена бронирования..")
        percent = self.refund_percent
        content = self.content
        way = self.way
        car = self.car
        place = self.place

        way_str = content[way]["from"]+" -> "+content[way]["to"]
        selected_place = content[way]["train"][car]["cars"][place]
        percent_price = (selected_place["price"]/100)*percent
        refound_price = selected_place["price"]-percent_price

        refound_str = "Вам вернется "+str(refound_price)+" руб. Сервис удержит комиссию в виде "+str(percent_price)+" руб."
        place_str = "\nВы действительно хотите отменить бронирование на "+place+" место "+car+" вагона поезда "+way_str+" ? (Да/Нет) -> "
        
        confirm_input = input(refound_str+place_str)
        if confirm_input == "Да" or confirm_input == "Y" or confirm_input == "y":

            selected_place["payment"] = 0
            selected_place["name"] = None

            #TODO Документ о возврате

            content[way]["train"][car]["cars"][place] = selected_place
            print("Запиcь изменений..")
            writer_obj = universal_module.FileClass(self.file_name)
            writer_obj.set_file(self.content)
            print("Успешно")
        
        else: 
            print("Хорошо, все оставили без изменений")