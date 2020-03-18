from phonedictionary_class import PhoneDictionaryClass
class FriendClass(PhoneDictionaryClass):
    def __init__(self, name, address, phone_number, birth_date):
        super().__init__(name, address, phone_number)
        self.birth_date = birth_date
    def out_info(self):
        return "[Класс друг]\nФИО: " + self.name + "\nAдрес: " + self.address + "\nНомер телефона: " + self.phone_number + "\nДата рождения: " + self.birth_date
