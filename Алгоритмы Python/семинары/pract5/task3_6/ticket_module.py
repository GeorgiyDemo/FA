"""
Модуль для работы с билетами
- Заказ, бронирование, покупка
- Отмена зказа
"""
import yaml

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
        
        self.selected_car = None
        self.file_name = file_name 
        self.way_from = way_from
        self.way_to = way_to

        print("Загрузка..")
        obj = FileClass(file_name,2)
        self.content = obj.get_text()
        
        self.add_reserve()
        self.car_searcher()
        if self.selected_car != None:
            self.place_searcher()
        
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
    
    def car_searcher(self):
        """
        Выбор вагона для брони в поезде
        #TODO Проверка, если нет таких поездов совсем + выбор поезда на пути
        #TODO Также можно добавить диапазон цен на места
        """
        content = self.content
        for train in content:
            if train["from"] == self.way_from and train["to"] == self.way_to:
                print("Поезд найден "+train["from"]+" -> "+train["to"])
                print("Всего в поезде "+str(train["info"]["car_count"])+" вагонов и "+str(train["info"]["places_free"])+" свободных мест")
                print('\nМест по вагонам:\n{0:10}  {1}'.format("Вагон", "Мест свободно"))
                buf_car_list = []

                for car in train["train"]:
                    print('{0:10}  {1}'.format(car, train["train"][car]["places_free"]))
                    buf_car_list.append(car)
                
                selected_car = input("Выберите вагон -> ")
                if selected_car in buf_car_list:
                    self.selected_car = selected_car
                else:
                    print("Нет такого вагона, выход из подпрограммы..")
    
    def place_searcher(self):
        """
        Выбор места в вагоне для брони
        """
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