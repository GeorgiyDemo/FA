from datetime import datetime


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.year_detector()

    def year_detector(self):
        """
        Метод определения возраста на основе полной даты рождения + datetime
        """
        now = datetime.now()
        year_now = int(now.strftime("%Y"))

        year, _, _ = map(int, self.birthday.split("-"))
        self.year = year_now - year

    def info(self):
        print("\n*Класс персона*\nФИО: " + self.name + \
              "\n" + "Дата рождения: " + self.birthday)

    def years_old(self):
        print("Возраст: " + str(self.year))

    def years_old_int(self):
        return self.year
