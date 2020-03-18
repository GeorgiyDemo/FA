from .transport_class import TransportClass
class ShipClass(TransportClass):
    def __init__(self, name, coords, passengers_number, max_speed, destination_name):
        super().__init__(name, coords)
        self.passengers_number = passengers_number
        self.max_speed = max_speed
        self.destination_name = destination_name
    def info(self):
        return "[Класс корабль]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str() + "\nКол-во пассажиров: " + str(
            self.passengers_number) + "\nМакс. скорость: " + str(
            self.max_speed) + "\nПорт приписки: " + self.destination_name