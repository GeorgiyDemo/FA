from .clent_class import ClentClass


class CreditorClass(ClentClass):
    def __init__(self, name, open_date, money_count, percent, balance_owed):
        super().__init__(name, open_date, money_count, percent)
        self.balance_owed = balance_owed

    def get_info(self):
        return "[Информация о кредиторе]\nФИО: " + self.name + "\nДата выдачи кредита: " + self.open_date + "\nРазмер кредита: " + str(
            self.money_count) + " руб.\nПроцент по кредиту: " + str(self.percent) + "%\nОстаток долга: " + str(
            self.balance_owed) + " руб."
