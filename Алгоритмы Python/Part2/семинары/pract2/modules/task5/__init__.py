from .studentclass import Student
from .baseclass import Person
from .abiturientclass import Abiturient
from .teacherclass import Teacher
from .get_jobs_list import get as get_job
from .get_ways_list import get as get_way
from .get_userinfo import processing as input_proc
import random
from datetime import datetime
from faker import Faker
def main():
    n, min_age, max_age = input_proc()
    fake = Faker(['ru_RU'])
    all_obj_list = []
    d = {1: Person, 2: Abiturient, 3: Student, 4: Teacher,}
    for _ in range(n):
        d_args = {1: [fake.name(), fake.date()], 2: [fake.name(), fake.date(), get_way()],3: [fake.name(), fake.date(), get_way(), random.randint(1, 4)],4: [fake.name(), fake.date(), get_way(), get_job(), random.randint(5, 35)],}
        r = random.randint(1, 4)
        all_obj_list.append(d[r](*d_args[r]))
        all_obj_list.sort(key=lambda e: e.years_old_int())
    for obj in all_obj_list:
        obj.info()
        obj.years_old()
        if obj.years_old_int() in range(min_age, max_age + 1): print("[Попадает в диапазон]")