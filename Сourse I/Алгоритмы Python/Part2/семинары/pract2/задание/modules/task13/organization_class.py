from .clent_class import ClentClass


class OrganizationClass(ClentClass):
    def __init__(self, name, open_date, account_number, balance):
        self.name = name
        self.open_date = open_date
        self.account_number = account_number
        self.balance = balance

    def get_info(self):
        return "[Информация об организации]\nНазвание: " + self.name + "\nДата открытия счёта: " + self.open_date + "\nНомер счёта: " + str(
            self.account_number) + "\nСумма на счету: " + str(self.balance) + " руб."
