"""
Задача 5. Создайте класс ПЕРСОНА с методами, позволяющими вывести на экран информацию о
персоне, а также определить ее возраст (в текущем году).

Создайте дочерние классы: АБИТУРИЕНТ (фамилия, дата рождения, факультет),
СТУДЕНТ (фамилия, дата рождения,
факультет, курс),

ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж), со
своими методами вывода информации на экран и определения возраста.

Создайте список из n
персон, выведите полную информацию из базы на экран, а также организуйте поиск персон,
чей возраст попадает в заданный диапазон. Комментарий. В родительском классе Persona()
определим, в соответствии с условием задачи, метод vozrast(), служащий для определения
возраста и метод info(), позволяющий вывести информацию о персоне. Далее создаем три
дочерних класса: Abiturient(Persona), Student(Persona), Prepodavatel(Persona), основанные
на классе Persona(). Соответственно, все дочерние классы будут наследовать методы
родительского класса. Чтобы вызвать конструктор базового класса, можно использовать
функцию Python - super(). Заметим, что при использовании функции super() можно не
передавать в явном виде параметр self.
"""
from datetime import datetime

class Persona:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.year_detector()
    
    def year_detector(self):
        now = datetime.now() # current date and time
        year_now = int(now.strftime("%Y"))

        _ , _ , year = map(int,self.birthday.split("."))
        self.year = year_now-year

    def info(self):
        print("*Класс персона*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday)

    def vozrast(self):
        print("Возраст: "+str(self.year))

class Abiturient(Persona):
    def __init__(self, name, birthday, way):
        super().__init__(name, birthday)
        self.way = way

    def info(self):
        print("*Класс абитуриента*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.way)

class Student(Persona):
    def __init__(self, name, birthday, way, course):
        super().__init__(name, birthday)
        self.way = way
        self.course = course
    
    def info(self):
        print("*Класс студента*\nФИО: "+self.name+\
            "\n"+"Дата рождения: "+self.birthday+\
            "\nФакультет: "+self.way+"\nКУРС"

class Prepodavatel(Persona):
    pass

if __name__ == "__main__":
    person_obj = Persona("КОТ","01.01.2001")
    person_obj.info()
    person_obj.vozrast()

    ab_obj = Abiturient("КОТ","03.12.2019","ПМИИТ")
    ab_obj.info()
    ab_obj.vozrast()