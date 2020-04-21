from .transport_class import TransportClass


class TruckClass(TransportClass):
    def __init__(self, model, number, speed, carrying, addition):
        super().__init__(model, number, speed, carrying)
        self.addition = addition
        self.formater_dict = {True: "Да", False: "Нет", }
        self.carrying_calculating()

    def carrying_calculating(self):
        if self.addition == True: self.carrying *= 2

    def get_info(self):
        return "[Грузовик]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying) + "\nНаличие прицепа: " + self.formater_dict[
                   self.addition]
