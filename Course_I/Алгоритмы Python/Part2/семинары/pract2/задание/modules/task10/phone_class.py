from .goods_class import GoodsClass


class PhoneClass(GoodsClass):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return (
            "[Телефон]\nНазвание: " + self.name + "\nЦена: " + str(self.price) + " руб."
        )
