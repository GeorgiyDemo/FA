class GoodsClass:
    def __init__(self, name, price, manufacture_date, expiration_date):
        self.name = name
        self.price = price
        self.manufacture_date = manufacture_date
        self.expiration_date = expiration_date

    def get_info(self):
        return (
            "[Товар]\nНазвание: "
            + self.name
            + "\nЦена: "
            + str(self.price)
            + " руб.\nДата производства: "
            + self.manufacture_date
            + "\nСрок годности: "
            + self.expiration_date
        )

    def opportunity_detector(self, user_price):
        if user_price >= self.price:
            return True
        return False
