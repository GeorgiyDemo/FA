from .goods_class import GoodsClass


class SportGoodsClass(GoodsClass):
    def __init__(self, name, price, manufacturer, age):
        super().__init__(name, price, manufacturer, age)

    def get_info(self):
        return "[Информация о спортинвентаре]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nПроизводитель: " + self.manufacturer + "\nВозраст, на который рассчитан: " + str(self.age)
