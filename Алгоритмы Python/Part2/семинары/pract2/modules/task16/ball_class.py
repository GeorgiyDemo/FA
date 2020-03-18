from .toy_class import ToyClass
class BallClass(ToyClass):
    def __init__(self, color, price, material, size):
        super().__init__(color, price, material, size)
    def toy_info(self):
        return "[Мяч]\nЦвет: " + self.color + "\nЦена: " + str(self.price) + " руб.\nМатериал: " + self.material + "\nДиаметр: " + str(self.size) + " см."
