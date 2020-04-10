class ToyClass:
    def __init__(self, color, price, material, size):
        self.color = color
        self.price = price
        self.material = material
        self.size = size

    def toy_info(self):
        return "[Базовый класс игрушка]\nЦвет: " + self.color + "\nЦена: " + str(
            self.price) + " руб.\nМатериал: " + self.material + "\nРазмер: " + str(self.size) + " см."

    def color_detector(self, color_input):
        if color_input == self.color:
            return True
        return False
