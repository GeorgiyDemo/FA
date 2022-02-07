from .software_class import SoftwareClass


class FreewareClass(SoftwareClass):
    def __init__(self, name, manufacturer):
        # Можно и через super, но в нашей жизни очень мало разнообразия
        self.name = name
        self.manufacturer = manufacturer

    def software_info(self):
        return (
            "[Свободное ПО]\nНазвание: "
            + self.name
            + "\nПроизводитель: "
            + self.manufacturer
        )

    def opportunity_detector(self):
        # Т.к. свободное ПО всегда можно использовать
        return True
