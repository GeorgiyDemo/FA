from .studentclass import Student
from .baseclass import Person
from .abiturientclass import Abiturient
from .teacherclass import Teacher

import random
from datetime import datetime

from faker import Faker


def main():
    try:
        n = int(input("Ведите количество персон -> "))
        person_range = list(
            map(int, input("Введите диапазон для поиска персон по возрасту\nПример: 36-40\n-> ").split("-")))
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
            3: [fake.name(), fake.date(), random.choice(ways_list), random.randint(1, 4)],
            4: [fake.name(), fake.date(), random.choice(ways_list), random.choice(jobs_list), random.randint(5, 35)],
        }

        r = random.randint(1, 4)
        all_obj_list.append(d[r](*d_args[r]))
        all_obj_list.sort(key=lambda e: e.years_old_int())

    for obj in all_obj_list:
        obj.info()
        obj.years_old()
        if obj.years_old_int() in range(min_age, max_age + 1):
            print("[Попадает в диапазон]")

main()
