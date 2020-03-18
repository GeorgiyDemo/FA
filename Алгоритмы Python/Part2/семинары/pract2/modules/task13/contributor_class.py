from .clent_class import ClentClass
class ContributorClass(ClentClass):
    def __init__(self, name, open_date, money_count, percent):
        super().__init__(name, open_date, money_count, percent)
    def get_info(self):
        return "[Информация о вкладчике]\nФИО: " + self.name + "\nДата открытия вклада: " + self.open_date + "\nРазмер вклада: " + str(
            self.money_count) + " руб.\nПроцент по вкладу: " + str(self.percent) + "%"