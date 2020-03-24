class GoodsClass:
    def __init__(self, name, price, manufacturer, age):
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
        self.age = age
    def get_info(self):
        return "[Информация о товаре]\nНазвание: " + self.name + "\nЦена: " + str(
            self.price) + "\nПроизводитель: " + self.manufacturer + "\nВозраст, на который рассчитан: " + str(self.age)
    def age_calculation(self, age_input):
        if age_input >= self.age:
            return True
        return False