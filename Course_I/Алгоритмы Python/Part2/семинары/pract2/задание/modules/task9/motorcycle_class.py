from .transport_class import TransportClass


class MotorcycleClass(TransportClass):
    def __init__(self, model, number, speed, carrying, addition):
        super().__init__(model, number, speed, carrying)
        self.addition = addition
        self.formater_dict = {
            True: "Да",
            False: "Нет",
        }
        self.carrying_calculating()

    def carrying_calculating(self):
        if self.addition == False:
            self.carrying = 0

    def get_info(self):
        return (
            "[Мотоцикл]\nМарка: "
            + self.model
            + "\nНомер: "
            + self.number
            + "\nСкорость: "
            + str(self.speed)
            + "\nГрузоподъёмность: "
            + str(self.carrying)
            + "\nНаличие коляски: "
            + self.formater_dict[self.addition]
        )
