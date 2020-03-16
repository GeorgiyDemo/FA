from _baseclass import Person
class Abiturient(Person):
    def __init__(self, name, birthday, way):
        super().__init__(name, birthday)
        self.way = way

    def info(self):
        print("\n*Класс абитуриента*\nФИО: " + self.name + \
              "\n" + "Дата рождения: " + self.birthday + \
              "\nФакультет: " + self.way)