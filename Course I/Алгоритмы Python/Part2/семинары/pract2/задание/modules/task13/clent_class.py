class ClentClass:
    def __init__(self, name, open_date, money_count, percent):
        self.name = name
        self.open_date = open_date
        self.money_count = money_count
        self.percent = percent

    def get_info(self):
        return "[Информация о клиенте]\nФИО: " + self.name + "\nДата оформления операции: " + self.open_date + "\nРазмер денежных единиц в операции: " + str(
            self.money_count) + " руб.\nПроцент: " + str(self.percent) + "%"

    def date_calculation(self, input_date):
        if input_date == self.open_date:
            return True
        return False
