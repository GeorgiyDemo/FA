class TransportClass:
    def __init__(self, model, number, speed, carrying):
        self.model = str(model)
        self.number = str(number)
        self.speed = speed
        self.carrying = carrying

    def get_info(self):
        return "[Транспорт]\nМарка: " + self.model + "\nНомер: " + self.number + "\nСкорость: " + str(
            self.speed) + "\nГрузоподъёмность: " + str(self.carrying)

    def get_carrying(self):
        return self.carrying
