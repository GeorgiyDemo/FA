from .phonedictionary_class import PhoneDictionaryClass
class PersonClass(PhoneDictionaryClass):
    def __init__(self, name, address, phone_number):
        super().__init__(name, address, phone_number)
    def out_info(self):
        return "[Класс персона]\nФИО: " + self.name + "\nAдрес: " + self.address + "\nНомер телефона: " + self.phone_number