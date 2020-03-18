from .toy_class import ToyClass
class CubeClass(ToyClass):
    def __init__(self, color, price, material, size):
        super().__init__(color, price, material, size)
    def toy_info(self):
        return "[Кубик]\nЦвет: " + self.color + "\nЦена: " + str(self.price) + " руб.\nМатериал: " + self.material + "\nРазмер ребра: " + str(self.size) + " см."
