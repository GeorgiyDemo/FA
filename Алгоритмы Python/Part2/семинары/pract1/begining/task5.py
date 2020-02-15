"""
Задача 5. Создайте класс ПЕРСОНА с методами, позволяющими вывести на экран информацию о
персоне, а также определить ее возраст (в текущем году).

Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
СТУДЕНТ (фамилия, дата рождения, факультет, курс),
ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж), со
своими методами вывода информации на экран и определения возраста.

Создайте список из n персон, выведите полную информацию из базы на экран, а также организуйте поиск персон,
чей возраст попадает в заданный диапазон.
"""

from faker import Faker
from datetime import datetime
import random 

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

        year , _ , _ = map(int,self.birthday.split("-"))
        self.year = year_now-year

    def info(self):
        print("\n*Класс персона*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday)

    def years_old(self):
        print("Возраст: "+str(self.year))

    def years_old_int(self):
        return self.year

class Abiturient(Person):
    def __init__(self, name, birthday, way):
        super().__init__(name, birthday)
        self.way = way

    def info(self):
        print("\n*Класс абитуриента*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.way)

class Student(Person):
    def __init__(self, name, birthday, way, course):
        super().__init__(name, birthday)
        self.way = way
        self.course = str(course)
    
    def info(self):
        print("\n*Класс студента*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.way+\
            "\nКурс: "+self.course)

class Teacher(Person):
    def __init__(self, name, birthday, way, position, years):
        super().__init__(name, birthday)
        self.way = way
        self.job_position = position
        self.job_years = str(years)
    
    def info(self):
        print("\n*Класс учителя*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.way+\
            "\nДолжность: "+self.job_position+\
            "\nСтаж: "+self.job_years)


def main():
        try:
            n = int(input("Ведите количество персон -> "))
            person_range = list(map(int,input("Введите диапазон для поиска персон по возрасту\nПример: 36-40\n-> ").split("-")))
            min_age, max_age = sorted(person_range)

        except ValueError:
            print("Некорректный ввод данных !")
            return

        ways_list = [
            "Факультет анализа рисков и экономической безопасности им. профессора В.К. Сенчагова",
            "Государственное управление и финансовый контроль",
            "Менеджмент",
            "Международные экономические отношения​",
            "Международный туризм, спорт и гостиничный бизнес",
            "Международный финансовый",
            "Налоги и налогообложение",
            "Прикладная математика и информационные технологии",
            "Социология и политология",
            "Учет и аудит",
            "Финансово-экономический",
            "Финансовых рынков",
            "Юридический",
        ]

        jobs_list = [
            "Старший научный сотрудник",
            "Старший преподаватель",
            "Профессор",
            "Преподаватель",
            "Научный сотрудник",
            "Младший научный сотрудник",
            "Доцент",
            "Докторант",
            "Главный научный сотрудник",
            "Ведущий научный сотрудник",
            "Ассистент"
        ]

        fake = Faker(['ru_RU'])
        all_obj_list = []

        d = {
            1: Person,
            2: Abiturient,
            3: Student,
            4: Teacher,
        }
        
        for _ in range(n):
            d_args = {
                1: [fake.name(), fake.date()],
                2: [fake.name(), fake.date(), random.choice(ways_list)],
                3: [fake.name(), fake.date(), random.choice(ways_list), random.randint(1,4)],
                4: [fake.name(), fake.date(), random.choice(ways_list), random.choice(jobs_list), random.randint(5,35)],
            }

            r = random.randint(1,4)
            all_obj_list.append(d[r](*d_args[r]))
            all_obj_list.sort(key=lambda e: e.years_old_int())
        
        for obj in all_obj_list:
            obj.info()
            obj.years_old()
            if obj.years_old_int() in range(min_age,max_age+1):
                print("[Попадает в диапазон]")
        

if __name__ == "__main__":
    main()
    