from toy_class import ToyClass
class CarClass(ToyClass):
    def __init__(self, color, price, name, manufacturer):
        self.color = color
        self.price = price
        self.name = name
        self.manufacturer = manufacturer
    def toy_info(self):
        return "[Машинка]\nЦвет: " + self.color + "\nЦена: " + str(self.price) + " руб.\nНазвание: " + self.name + "\nПроизводитель: " + self.manufacturer