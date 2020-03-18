class PhoneDictionaryClass:
    def __init__(self, name, address, phone_number):
        self.name = name
        self.address = address
        self.phone_number = phone_number
    def search(self, input_name):
        if input_name in self.name:
            return True
        return False
    def out_info(self):
        ...