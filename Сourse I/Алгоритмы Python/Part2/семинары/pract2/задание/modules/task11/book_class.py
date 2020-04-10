from .goods_class import GoodsClass


class BookClass(GoodsClass):
    def __init__(self, name, price, manufacturer, age, author):
        super().__init__(name, price, manufacturer, age)
        self.author = author

    def get_info(self):
        return "[Информация о книге]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nИздательство: " + self.manufacturer + "\nВозраст, на который рассчитана: " + str(
            self.age) + "\nАвтор: " + self.author
