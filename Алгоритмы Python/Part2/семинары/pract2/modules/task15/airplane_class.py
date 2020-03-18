from transport_class import TransportClass
class AirplaneClass(TransportClass):
    def __init__(self, name, coords, passengers_number, max_speed, max_height):
        super().__init__(name, coords)
        self.passengers_number = passengers_number
        self.max_speed = max_speed
        self.max_height = max_height
    def info(self):
        return "[Класс самолёт]\nМодель: " + self.name + "\nКоординаты: " + self.coords_formater_str() + "\nКол-во пассажиров: " + str(
            self.passengers_number) + "\nМакс. скорость: " + str(self.max_speed) + "\nМакс. высота: " + str(
            self.max_height)