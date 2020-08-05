from .baseclass import Person


class Student(Person):
    def __init__(self, name, birthday, way, course):
        super().__init__(name, birthday)
        self.way = way
        self.course = str(course)

    def info(self):
        print(
            "\n*Класс студента*\nФИО: "
            + self.name
            + "\n"
            + "Дата рождения: "
            + self.birthday
            + "\nФакультет: "
            + self.way
            + "\nКурс: "
            + self.course
        )
