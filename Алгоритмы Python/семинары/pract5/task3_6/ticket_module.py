"""
Модуль для работы с билетами
- Заказ, бронирование, покупка
- Отмена зказа
"""
import yaml

def check_reservers_by_name(d, name):
    """
    Метод полезен тажке для отмены бронирования
    """
    trains_with_name = []
    for way in d:
        for train in way["train"]:
            for place in way["train"][train]["cars"]:
                current_place_dict = way["train"][train]["cars"][place]
                if current_place_dict["name"] == name:
                    price_str = str(current_place_dict["price"])
                    print("["+price_str+"руб.] Поезд по пути '"+way["from"]+"' -> '"+way["to"]+"' Вагон №"+train+", место "+place)
                
                #for place in way["train"][train]["cars"][car]:

                #    locale_dict = way["train"][train]["cars"][car]
                #    print(locale_dict[place])
    return ""
    
class FileClass():

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
    def __init__(self, file_name):
        obj = FileClass(file_name,2)
        self.content = obj.get_text()
        self.file_name = file_name 
        self.add_reserve()

    def add_reserve(self):
        """
        Файл добавления данных в файл
        - Спрашивает номер вагона 
        - Спрашивает номер места
        """
        new_name = input("Введите ФИО пассажира -> ")
        check_name_tuple = check_reservers_by_name(self.content,new_name)
        if check_name_tuple != "":
            print("Ваши брони:")
            print(check_name_tuple)
        #print("Весь словарь:")
        #for k in self.content:
        #    print(k)

        #    print("-")
        #car_places_dict[str(i)] = {"name":"Кот занял место", "price":1300, "type":"reserved"}
    

class RemoveTicketClass():
    """
    Класс для отмены бронирования билетов
    """
    def __init__(self, file_name):
        self.remove_reserve()

    def remove_reserve(self):
        """
        Файл добавления данных в файл
        - Спрашивает номер вагона 
        - Спрашивает номер места
        """
        #car_places_dict[str(i)] = {"name":"Кот занял место", "price":1300, "type":"reserved"}
        pass

    def remove_reserve(self):
        pass

###Временно
if __name__ == "__main__":
    AddTicketClass("tickets.yml")