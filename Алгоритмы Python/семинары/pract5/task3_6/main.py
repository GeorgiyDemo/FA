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
import waysearcher_module

from os import path

def check_reservers_by_name(d, name):
    """
    Метод находит по ФИО брони все билеты в коллекции
    Также полезен для отмены бронирования #TODO
    """
    d_payment_formater = {
        0 : "Ожидает оплаты",
        1 : "Оплачено",
    }
    ways_index = []
    tickets = []
    for i in range(len(d)):
        for car in d[i]["train"]:
            for place in d[i]["train"][car]["cars"]:
                current_place_dict = d[i]["train"][car]["cars"][place]
                if current_place_dict["name"] == name:
                    price_str = str(current_place_dict["price"])
                    ways_index.append(i)
                    tickets.append([
                        d[i]["from"]+" -> "+d[i]["to"],
                        car,
                        place,
                        price_str+" руб.",
                        current_place_dict["type"],
                        d_payment_formater[current_place_dict["payment"]],
                    ])
    return ways_index, tickets   

class FileGeneratorClass():

   """
   Класс-генератор свободных мест на рейсы и запись в файл
   """
   #TODO Сделать рандомное заполнение мест в словаре, не всегда же поезда пустыи катаются??

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

class MainClass():

    def __init__(self):
        """
        Конструктор класса
        Формирует словарь железнодорожных сообщений + вызов всех методов
        """
        self.file_name = "tickets.yml"
        
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
            menu_str = "\nВыберите действие:\n1. Покупка билетов\n2. Управление моими билетами\n0. Выход из программы\n-> "
            input_value = input(menu_str)
            
            if input_value == "1":
                obj = waysearcher_module.SearcherClass(self.d)
                
                #print("Хотите купить билет(ы) на весь указанный путь? (Да/Нет)
                #if "Да":
                #   print("Выбор режима покупки\nХотите, чтоб система оформила наиболее дешевые билеты автоматически для каждого отдельного пути? Если нет, то вам придётся вручную делать оформление каждого отдельного билета (Да/Нет) ->")
                #    if "Да":
                #        Автоматически поиск самых дешевых
                #    if "Нет"
                #        Пусть вбивает всё сам

                #ticket_module.AddTicketClass(self.file_name)
                #
            elif input_value == "2":
                print("Загрузка..")
                obj = universal_module.FileClass(self.file_name,2)
                self.content = obj.get_text()


                self.new_name = input("Введите ФИО пассажира -> ")
                ways_indexes, check_name_tuple = check_reservers_by_name(self.content,self.new_name)
                
                #TODO Оформить в виде таблицы
                #Поезд #№Вагона #№Места #Цена #Тип #Статус (Оплачено/Ожидет оплаты)
                ticket_list = []
                if check_name_tuple != []:
                    print('Ваши билеты:\n{0:<10} {1:>17} {2:>19} {3:>21} {4:>23} {5:>25} {6:>27}'.format("№","Поезд", "№ вагона", "№ места", "Цена","Тип места","Статус"))
                    for i in range(len(check_name_tuple)):
                        ticket_list.append(str(i+1))
                        #Вывод
                        
                        print('{0:<10} {1:>17} {2:>19} {3:>21} {4:>23} {5:>25} {6:>27}'.format(i+1,*check_name_tuple[i]))
                    reserve_input = input("Введите номер бронирования для управления им -> ")
                    if reserve_input in ticket_list:
                        current_reserve = check_name_tuple[int(reserve_input)-i]
                        #Флаг для проверки на ввод 2 пункта
                        payment_show = False
                        if current_reserve[5] == "Ожидает оплаты":
                        #TODO Печать билета?
                        #TODO Выход на меню назад, к выбору всех билетов?
                            payment_show = True
                            print("Бронирование №"+reserve_input+"\nДоступные действия:\n1. Отмена бронирования\n2. Оплата билета")
                        else:
                            print("Бронирование №"+reserve_input+"\nДоступные действия:\n1. Отмена бронирования")
                        input_command = input("Введите номер действия -> ")
                        
                        if input_command == "1":
                            #TODO Номер бронирования, вагон и т д 
                            ticket_module.RemoveTicketClass(self.file_name)
                            print("Отмена бронирования..")
                        
                        elif input_command == "2" and payment_show == True:
                            payment_obj = ticket_module.PaymentClass()
                            
                            if payment_obj.result == True:
                                way_index = ways_indexes[int(reserve_input)-i]

                                self.content[way_index]["train"][current_reserve[1]]["cars"][current_reserve[2]]["payment"] = 1

                                #Записываем все в файл
                                print("Записываем изменения..")
                                writer_obj = universal_module.FileClass(self.file_name)
                                writer_obj.set_file(self.content)
                            else:
                                print("Оплата не прошла..")

                        
                        else:
                            print("Нет такого пункта в меню")
                        
                        print("Доступные действия со списком:\n")


                        print("Работаем..")
                    else:
                        print("Введенного номера бронирования не существует")
                    #Проверка на то, что можно выводить в управлении
                    

                
                else:
                    print("Броней, связанных с введенными ФИО не найдено")
        



               
                #Вводим фио
                #Ищем билеты по мним
                #Выберите билет (выбираем билет)
                #Доступные действия
                #1. Отмена бронирования
                #2. Оплата билета (появляется если только мы его не оплатили)
                #3. Распечатать билет (????? ПОКА #TODO)
                #ticket_module.AddTicketClass(self.file_name)
                #ticket_module.RemoveTicketClass(self.file_name)

            elif input_value != "0":
                print("Такого пункта нет в меню")




if __name__ == "__main__":
    MainClass()