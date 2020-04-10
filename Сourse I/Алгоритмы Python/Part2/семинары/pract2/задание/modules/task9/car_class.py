from .transport_class import TransportClass


class CarClass(TransportClass):
    def __init__(self, model, number, speed, carrying):
        super().__init__(model, number, speed, carrying)

    def get_info(self):
        return "[Автомобиль]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying)
