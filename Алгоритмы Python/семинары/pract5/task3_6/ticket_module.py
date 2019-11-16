"""
Модуль для работы с билетами
- Заказ, бронирование, покупка
- Отмена зказа
"""
import yaml

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

def check_reservers_by_name(d, name):
    """
    Метод находит по ФИО брони все билеты в коллекции
    Также полезен для отмены бронирования #TODO
    """
    trains_str = []
    trains = []
    for i in range(len(d)):
        for car in d[i]["train"]:
            for place in d[i]["train"][car]["cars"]:
                current_place_dict = d[i]["train"][car]["cars"][place]
                if current_place_dict["name"] == name:
                    price_str = str(current_place_dict["price"])
                    trains_str.append("["+price_str+" руб.] Поезд по пути '"+d[i]["from"]+"' -> '"+d[i]["to"]+"' Вагон №"+car+", место "+place)
                    trains.append([i,car,place])
                
    return (trains_str, trains)
    
class FileClass():
    """
    Класс для работы с файлом file_name, который передаётся в конструктр из main
    - Записывает данные в файл
    - Читает данные из файла 
    """

    def __init__(self, file_name, method):
        self.file_name = file_name
        _select_d = {
            1 : self.set_file,
            2 : self.read_file,
        }
        if method in _select_d:
            _select_d[method]()
        else:
            raise ValueError("Значения нет в словаре","method принял значение "+str(method))

    def set_file(self,content):
        with open(self.file_name, 'w') as outfile:
            yaml.safe_dump(content, outfile, allow_unicode=True)
    
    def read_file(self):
        with open(self.file_name, 'r') as outfile:
            self.content = yaml.safe_load(outfile)

    def get_text(self):
        return self.content


class AddTicketClass():
    """
    Класс для добавления билетов. Выщывается как при прямых рейсов, так и для ресов с пересадками
    #TODO В конструкторе ввести поля для автобронирования мест при использовании пункта 1
    """
    def __init__(self, file_name, way_from=None, way_to=None):
        
        self.file_name = file_name 
        self.way_from = way_from
        self.way_to = way_to

        print("Загрузка..")
        obj = FileClass(file_name,2)
        self.content = obj.get_text()
        
        self.add_reserve()

        
    def add_reserve(self):
        """
        Файл добавления данных в файл
        - Спрашивает номер вагона 
        - Спрашивает номер места
        """
        new_name = input("Введите ФИО пассажира -> ")
        check_name_tuple = check_reservers_by_name(self.content,new_name)
        if check_name_tuple[0] != []:
            print("Ваши брони:")
            print('\n'.join(check_name_tuple[0]))
        else:
            print("Броней, связанных с введенными ФИО не найдено")
        
        if self.way_from == None and self.way_to == None:
            self.way_from = input("Введите странцию отправления -> ")
            self.way_to = input("Введите станцию прибытия -> ")

        self.car_searcher()

    def car_searcher(self):
        """
        Выбор вагона для брони в поезде
        #TODO Проверка, если нет таких поездов совсем + выбор поезда на пути
        
        #Номер Статус  Цена Тип
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
        for place in content[way]["train"][selected_car]["cars"]:
            
            locale_place = content[way]["train"][selected_car]["cars"][place]
            
            reserved_type = "свободно"
            if locale_place["name"] != None:
                reserved_type = "забронировано"
            price = str(locale_place["price"])+" руб."

            print('{0:<10} {1:>10} {2:>15} {3:>20}'.format(place, reserved_type, price, locale_place["type"]))
        
        #print(selected_car)
        #for place in 

    #Введите место 
    #Вы действительно хотите забронировать место N в вагоне M поезда Москва - Екатеринбург на имя ФИО???
    #Номер Статус  Цена Тип



        pass

class RemoveTicketClass():
    """
    Класс для отмены бронирования билетов
    """
    def __init__(self, file_name):
        self.remove_reserve()

    def ticket_remover(self):
        #делает None на место + обращается к FileClass для записи обновлённого файла
        pass

    def remove_reserve(self):
        """
        Файл добавления данных в файл
        - Спрашивает номер вагона 
        - Спрашивает номер места
        """
        new_name = input("Введите ФИО пассажира -> ")
        check_name_tuple = check_reservers_by_name(self.content,new_name)
        if check_name_tuple[0] != []:
            print("Ваши брони:")
            print('\n'.join(check_name_tuple[0]))
            remove_ticket = input("Какую бронь хотите отменить?\n-> ")

        else:
            print("Броней, связанных с введенными ФИО не найдено")
        #car_places_dict[str(i)] = {"name":"Кот занял место", "price":1300, "type":"reserved"}
        pass


###Временно
if __name__ == "__main__":
    AddTicketClass("tickets.yml")