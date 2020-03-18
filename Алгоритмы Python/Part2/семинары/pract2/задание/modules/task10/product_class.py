from .goods_class import GoodsClass
class ProductClass(GoodsClass):
    def __init__(self, name, price, manufacture_date, expiration_date):
        super().__init__(name, price, manufacture_date, expiration_date)
    def get_info(self):
        return "[Продукт]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + " руб.\nДата производства: " + self.manufacture_date + "\nСрок годности: " + self.expiration_date