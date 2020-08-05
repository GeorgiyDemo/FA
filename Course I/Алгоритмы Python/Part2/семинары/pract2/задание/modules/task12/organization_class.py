from .phonedictionary_class import PhoneDictionaryClass


class OrganizationClass(PhoneDictionaryClass):
    def __init__(self, name, address, phone_number, fax, contact_person):
        super().__init__(name, address, phone_number)
        self.fax = fax
        self.contact_person = contact_person

    def out_info(self):
        return (
            "[Класс организация]\nНазвание: "
            + self.name
            + "\nAдрес: "
            + self.address
            + "\nНомер телефона: "
            + self.phone_number
            + "\nФакс: "
            + self.fax
            + "\nКонтактое лицо: "
            + self.contact_person
        )

    def search(self, input_name):
        if input_name in self.contact_person:
            return True
        return False
