#Чекнуть парочку TODO ниже

"""1.	Создайте класс Летательный аппарат с методом, позволяющими вывести на экран информацию об объекте. 

Создайте дочерние классы для летательных аппаратов:

Самолеты (название, цена, скорость, тип самолета (истребитель, штурмовик, бомбардировщик,гражданский (может быть транспортный, может быть пассажирский)), 
тип вооружения, максимальная высота полета, высота полета, запас топлива в баке, максимальный запас топлива, расход топлива, страна производитель, страна владелец).
Методы:
расчет времени полета на имеющемся запасе топлива;
расчет возможности полета на введенное расстояние;
расчет возможности поражения цели (если самолет военный: для бомбардировщика наземные, истребитель любые летательные объекты, штурмовик наземные и летательные объекты);
расчет возможности полета на заданное расстояние без дозаправки.

Вертолеты (название, цена, количество членов экипажа, грузоподъемность, тип объекта (военный, медицинский, транспортный), высота полета, место расположение объекта, страна производитель, страна владелец).

В качестве методов в дочернем классе Вертолетов должны быть реализованы:
расчет количества вертолетов для перевозки груза за заданное количество полетов
(Пример: если требуется перевезти 40 т. программа должна использовать только вертолеты транспортные, при заданном количестве полетов 2 возможно использование одного вертолета с грузоподъемностью более 20 т, но менее 40. Если количество полётов равно 1, то возможно использование вертолетов с грузоподъемностью более или равной 40 т., если такого вертолета нет в созданном списке объектов, то требуется уведомить о невозможности совершения грузоперевозки). 


Создайте класс для Средств ПВО с методом вывода информации об объекте.


Подклассы:

Ракетные (название, дальность, высота поражения, скорость ракет, количество ракет в установке, стационарное или перемещаемое, скорость перемещения, количество людей в расчете).

Метод: расчет возможности поражения летательного объекта (скорость ракеты должна быть больше скорости летательного аппарата).

Зенитные (название, высота поражения, количество снарядов, калибр, количество стволов, количество людей в расчете) Метод: расчет возможности поражения объекта по высоте (высота поражения должна быть больше высоты полета летательного объекта).

Класс Объекты поражения (название, тип).
Метод: вывод информации об объекте.


Программа должна: 
1.	предоставлять пользователю возможность создания списка летательных объектов, средств ПВО и Объектов поражения;
2.	предоставлять возможность вывода информации о летательном объекте, средстве ПВО и Объекте поражения;
3.	выполнить расчет времени полета на имеющемся запасе топлива; (для самолетов)
4.	выполнить расчет возможности полета на введенное расстояние без дозаправки; (для самолетов)
5.	для выбранного летательного объектов выполнять расчет возможности поражения заданного объекта (объект может быть летательным или наземным); (для самолетов)
6.	предоставлять расчет количества вертолетов для перевозки груза за заданное количество полетов; (для вертолетов)
7.	предоставлять расчета возможности поражения летательного объекта с учетом его скорости и высоты полета.
В программе должно использоваться минимально 2 рекурсии на усмотрение учащегося. Допускается обоснованное изменение структуры классов при программной реализации. Итоговое задание требуется разбить на модули.
PS. Да, я знаю, что самолеты входят в средства ПВО.
"""

class AircraftClass:
    """Класс летательный аппарат"""
    def __init__(self, name, price, object_type, flight_altitude, producing_country, owner_country):
        """
        Общие поля: название, цена, тип объекта, высота полета, страна производитель, страна владелец
        """
        self.name = name
        self.price = price
        self.object_type = object_type
        self.flight_altitude = flight_altitude
        self.producing_country = producing_country
        self.owner_country = owner_country


    def info(self):
        """Метод для вывода информации об объекте"""
        d_formater = {}
        d_formater["Имя"] = self.name
        d_formater["Цена"] = self.price
        d_formater["Тип объекта"] = self.object_type
        d_formater["Высота полета"] = self.flight_altitude
        d_formater["Страна-производитель"] = self.producing_country
        d_formater["Страна-владелец"] = self.owner_country

        out_str = "*Общая информация о летательном аппарате*\n"
        out_str+="\n".join(list([str(k)+": "+str(v) for k, v in d_formater.items()]))
        print(out_str)

class PlaneClass(AircraftClass):
    """Дочерний класс самолет"""
    def __init__(self, name, price, object_type, flight_altitude, producing_country, owner_country, speed, weapon_type, altitude_max, fuel, fuel_max, fuel_consumption):
        """
        Общие поля с Aircraft:
        Название, цена, тип объекта, высота полета, страна производитель, страна владелец
        Различные поля с Aicraft:
        Скорость,тип вооружения, максимальная высота полета, запас топлива в баке, максимальный запас топлива, расход топлива
        """
        #Список для фильтрации типа самолетов
        type_detector_list = ["истребитель", "штурмовик", "бомбардировщик", "гражданский транспортный", "гражданский пассажирский"]
        if object_type not in type_detector_list:
            raise ValueError("Мне передали некорректный тип самолета, что дальше?")
        
        #Если текущие показания больше максиальных, то выставляем максимальные для текущих
        if flight_altitude > altitude_max:
            flight_altitude = altitude_max
        if fuel > fuel_max:
            fuel = fuel_max

        super().__init__(name, price, object_type, flight_altitude, producing_country, owner_country)
        self.speed = speed
        self.weapon_type = weapon_type
        self.altitude_max = altitude_max
        self.fuel = fuel
        self.fuel_max = fuel_max
        #Это расход топлива, учим английский
        self.fuel_consumption = fuel_consumption

    
    def fuel_calculation(self):
        """Расчет времени полета на имеющемся запасе топлива"""
        #Текущий запас топлива
        fuel = self.fuel 
        #Расход топлива в час времени
        fuel_consumption = self.fuel_consumption

        #Целое кол-во часов + дробное кол-во минут
        result = round(fuel/fuel_consumption,2)

        return result

    def flight_opportunity_max(self, distance_input):
        """"
        Расчет возможности полета на введенное расстояние с дозаправкой (т.е. с использованием полного бака)
        - Возвращает True или False
        """
        #макс топливо/расход = часы
        max_hours = self.fuel_max/self.fuel_consumption
        #часы* скорость = макс расстояние
        max_distance = max_hours * self.speed
        if max_distance < distance_input:
            return False
        return True

    def murder_opportunity(self, purpose_obj):
        """
        Расчет возможности поражения цели если самолет военный
        - Для бомбардировщика наземные,
        - Истребитель - любые летательные объекты
        - штурмовик - наземные и летательные объекты
        """
        if not isinstance(purpose_obj, ObjectKilledClass):
            raise ValueError("Неободим объект класса ObjectKilledClass")
        
        #Если не гражданский
        if "гражданский" not in self.object_type:
            
            if self.object_type == "штурмовик":
                return True
            
            if self.object_type == "истребитель" and purpose_obj.type == "летательный":
                return True

            if self.object_type == "бомбардировщик" and purpose_obj.type == "наземный":
                return True
        
        return False

    def flight_opportunity_current(self, distance_input):
        """
        Расчет возможности полета на заданное расстояние без дозаправки (т.е. с использованием текущего бака)
        - Возвращает True или False
        """
        #макс топливо/расход = часы
        hours = self.fuel_calculation()
        #часы* скорость = макс расстояние
        distance = hours * self.speed
        if distance < distance_input:
            return False
        return True

class HelicopterClass(AircraftClass):
    """Дочерний класс вертолет"""
    #Поле со всеми объектами вертолетов
    obj_list = []

    def __init__(self, name, price, object_type, flight_altitude, producing_country, owner_country, people_count, carrying, current_location):
        """
        Общие поля с Aircraft:
        Название, цена, тип объекта, высота полета, страна производитель, страна владелец
        Различные поля с Aicraft:
        Количество членов экипажа, грузоподъемность, место расположение объекта
        """
        #Список для фильтрации типа вертолетов
        type_detector_list = ["военный", "медицинский", "транспортный"]
        if object_type not in type_detector_list:
            raise ValueError("Мне передали некорректный тип вертолета, что дальше?")

        
        super().__init__(name, price, object_type, flight_altitude, producing_country, owner_country)
        self.people_count = people_count
        self.carrying = carrying
        self.current_location = current_location

        HelicopterClass.obj_list.append(self)
    
    #TODO
    def transportation_calculation(self, weight=40, flights_number = 10):
        """
        Расчет количества вертолетов для перевозки груза за заданное количество полетов
        (Пример: если требуется перевезти 40 т. программа должна использовать только вертолеты транспортные, (??????)
        при заданном количестве полетов 2 возможно использование одного вертолета с грузоподъемностью более 20 т, но менее 40.
        
        
        """
        #Список задействованных вертолетов
        stakhanovsk_h_list = []
        
        #Если надо перевезти все за 1 раз, то ищем вертолеты больше или равной грузоподьемности
        if flights_number == 1:
            for h_obj in HelicopterClass.obj_list:
                if h_obj.carrying >= weight:
                    print("Осуществили перевозку {} т. груза на объекте самолета {}".format(weight, h_obj))
                    stakhanovsk_h_list.append(h_obj)
                    break
        
        #Значит больше 1 раза надо полетать
        else:
            #Вводим переменную доставленного груза
            dislocated_weight = weight

            for h_obj in HelicopterClass.obj_list:
                print("Вес, который осталось перевезти:",dislocated_weight)
                
                if dislocated_weight == 0:
                    print("Все перевезли!")
                    return

                #Нормальная ситуация, когда грузоподъемность меньше груза
                if h_obj.carrying <= weight:
                    #Если меньше грузоподъёмности надо загрузить
                    if dislocated_weight < h_obj.carrying:
                        print("Осуществили перевозку {} т. груза на объекте самолета {}".format(dislocated_weight, h_obj))
                        dislocated_weight = 0
                    else:
                        dislocated_weight -= h_obj.carrying
                        print("Осуществили перевозку {} т. груза на объекте самолета {}".format(h_obj.carrying, h_obj))
                    stakhanovsk_h_list.append(h_obj)
                
                #Ненормальная ситуация, когда грузоподъёмность больше груза
                if h_obj.carrying > weight:
                    dislocated_weight = 0
                    print("Осуществили перевозку ВСЕГО груза в кол-ве {} т. груза на объекте самолета {}".format(weight, h_obj))
                    stakhanovsk_h_list.append(h_obj)

        if len(stakhanovsk_h_list) == 0:
            print("Невозможно осуществить грузоперевозку!")

class PVOClass:
    """
    Класс средств ПВО
    Поля: название, высота поражения, количество людей в расчете, количество ракет в установке/количество снарядов (это же одно и то же, да?)
    """
    def __init__(self, name, murder_height, people_count, projectiles_count):
        self.name = name
        self.murder_height = murder_height
        self.people_count = people_count
        #Оу, новое слово на английском
        self.projectiles_count = projectiles_count
    
    def info(self):
        """Метод с информацией об объекте"""
        d_formater = {}
        d_formater["Название"] = self.name
        d_formater["Высота поражения"] = self.murder_height
        d_formater["Количество людей в расчете"] = self.people_count
        d_formater["Количество ракет в установке"] = self.projectiles_count
        out_str = "*Общая информация об объекте класса ПВО*\n"
        out_str+="\n".join(list([str(k)+": "+str(v) for k, v in d_formater.items()]))
        print(out_str)

class MissileClass(PVOClass):
    """
    Ракетные ПВО
    Общие поля с PVOClass:
    Название, высота поражения, количество людей в расчете,  количество ракет в установке
    Различные поля:
    Дальность, скорость ракет, стационарное или перемещаемое, скорость перемещения
    """
    def __init__(self, name, murder_height, people_count, projectiles_count, shot_range, speed, dislocation_type, movement_speed):
        
        #Список для фильтрации
        dislocation_type_list = ["стационарное", "перемещаемое"]
        if dislocation_type not in dislocation_type_list:
            raise ValueError("Мне передали некорректный тип дислокации ракетного ПВО, что я должен с этим делать?")

        super().__init__(name, murder_height, people_count, projectiles_count)
        self.shot_range = shot_range
        self.speed = speed
        self.dislocation_type = dislocation_type
        self.movement_speed = movement_speed


    def murder_opportunity(self, aircraft_obj):
        """"
        Метод для расчета возможности поражения летательного объекта (скорость ракеты должна быть больше скорости летательного аппарата)
        """
        if not isinstance(aircraft_obj, AircraftClass):
            raise ValueError("Необходим объект класса AircraftClass!")
        
        #Если это вертолет, то его скорость объективно меньше самолета -> 100 процентов попадет
        #Но на самом деле по-хорошему у HelicopterClass должно быть поле speed, аналогичное PlaneClass
        if isinstance(aircraft_obj, HelicopterClass):
            return True
        
        if self.speed > aircraft_obj.speed:
            return True
        return False

class AntiAircraft(PVOClass):
    """
    Зенитные ПВО
    Общие поля с PVOClass:
    Название, высота поражения, количество людей в расчете,  количество ракет в установке
    Различные поля:
    Калибр, количество стволов
    """
    def __init__(self, name, murder_height, people_count, projectiles_count, caliber, barrels_number):
        super().__init__(name, murder_height, people_count, projectiles_count)
        self.caliber = caliber
        self.barrels_number = barrels_number
    
    def murder_opportunity(self, aircraft_obj):
        """
        Расчет возможности поражения объекта по высоте (высота поражения должна быть больше высоты полета летательного объекта).
        """
        if not isinstance(aircraft_obj, AircraftClass):
            raise ValueError("Необходим объект класса AircraftClass!")

        if self.murder_height > aircraft_obj.flight_altitude:
            return True
        
        return False

class ObjectKilledClass:
    """
    Класс Объекты поражения (название, тип)
    Как я понял, используются в PlaneClass.murder_opportunity
    Тип: наземный, летательный
    """
    def __init__(self, name, type_):
        self.name = name
        self.type = type_
    
    def info(self):
        """Вывод информации об объекте."""

        d_formater = {}
        d_formater["Имя"] = self.name
        d_formater["Тип"] = self.type

        out_str = "*Общая информация об объекте поражения*\n"
        out_str+="\n".join(list([str(k)+": "+str(v) for k, v in d_formater.items()]))
        print(out_str)


if __name__ == "__main__":

    for i in range(7):
        h = HelicopterClass("КОТ", 2445, "военный",435345, "Россия", "Китай",5,40,"Дубаи",)
    h.transportation_calculation(110,10)