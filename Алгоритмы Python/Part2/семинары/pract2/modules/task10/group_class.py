from goods_class import GoodsClass
class GroupClass(GoodsClass):
    def __init__(self, name, price, manufacture_date, expiration_date, amount):
        super().__init__(name, price, manufacture_date, expiration_date)
        self.amount = amount
    def get_info(self):
        return "[Партия]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + " руб.\nДата производства: " + self.manufacture_date + "\nСрок годности: " + self.expiration_date + "\nКоличество штук: " + str(
            self.amount)