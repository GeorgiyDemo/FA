import datetime
class SoftwareClass:
    def __init__(self, name, manufacturer):
        self.name = name
        self.manufacturer = manufacturer
        self.date = datetime.datetime.now()
    def software_info(self):
        return "[Родительский класс ПО]\nНазвание: " + self.name + "\nПроизводитель: " + self.manufacturer
    def opportunity_detector(self):
        # Его все равно переопределят
        ...