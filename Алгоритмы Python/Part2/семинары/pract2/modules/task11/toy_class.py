from .goods_class import GoodsClass
class ToyClass(GoodsClass):
    def __init__(self, name, price, manufacturer, age, material):
        super().__init__(name, price, manufacturer, age)
        self.material = material
    def get_info(self):
        return "[Информация об игрушке]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nПроизводитель: " + self.manufacturer + "\nВозраст, на который рассчитана: " + str(
            self.age) + "\nМатериал: " + self.material