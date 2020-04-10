from airclass_module import HelicopterClass, AircraftClass


class PVOClass:
    """
    Класс средств ПВО
    Поля: название, высота поражения, количество людей в расчете, количество ракет в установке/количество снарядов (это же одно и то же, да?)
    """

    def __init__(self, name, murder_height, people_count, projectiles_count):
        self.name = name
        self.murder_height = murder_height
        self.people_count = people_count
        # Оу, новое слово на английском
        self.projectiles_count = projectiles_count

    def info(self):
        """Метод с информацией об объекте"""
        d_formater = {}
        d_formater["Название"] = self.name
        d_formater["Высота поражения"] = self.murder_height
        d_formater["Количество людей в расчете"] = self.people_count
        d_formater["Количество ракет в установке"] = self.projectiles_count
        out_str = "*Общая информация об объекте класса ПВО*\n"
        out_str += "\n".join(list([str(k) + ": " + str(v) for k, v in d_formater.items()]))
        print(out_str)


class MissileClass(PVOClass):
    """
    Ракетные ПВО
    Общие поля с PVOClass:
    Название, высота поражения, количество людей в расчете,  количество ракет в установке
    Различные поля:
    Дальность, скорость ракет, стационарное или перемещаемое, скорость перемещения
    """

    def __init__(self, name, murder_height, people_count, projectiles_count, shot_range, speed, dislocation_type,
                 movement_speed):

        # Список для фильтрации
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

        # Если это вертолет, то его скорость объективно меньше самолета -> 100 процентов попадет
        # Но на самом деле по-хорошему у HelicopterClass должно быть поле speed, аналогичное PlaneClass
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
