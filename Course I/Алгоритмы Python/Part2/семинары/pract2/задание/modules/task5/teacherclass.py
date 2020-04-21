from .baseclass import Person


class Teacher(Person):
    def __init__(self, name, birthday, way, position, years):
        super().__init__(name, birthday)
        self.way = way
        self.job_position = position
        self.job_years = str(years)

    def info(self):
        print("\n*Класс учителя*\nФИО: " + self.name + \
              "\n" + "Дата рождения: " + self.birthday + \
              "\nФакультет: " + self.way + \
              "\nДолжность: " + self.job_position + \
              "\nСтаж: " + self.job_years)
