"""
ПИ19-4 Деменчук Георгий Практика 5
Подгруппа 3
"""

from sqlalchemy import select, create_engine, MetaData, Table, cast, String
from sqlalchemy.sql import expression, functions, func
from sqlalchemy import types

import warnings
warnings.filterwarnings('ignore')

engine = create_engine("sqlite:///Students.db")
metadata=MetaData()
connection=engine.connect()

#Объявляем все таблицы
exam_marks=Table('exam_marks', metadata, autoload=True, autoload_with=engine)
lecturer=Table('lecturer', metadata, autoload=True, autoload_with=engine)
student=Table('student', metadata, autoload=True, autoload_with=engine)
subj_lect =Table('subj_lect', metadata, autoload=True, autoload_with=engine)
subject=Table('subject', metadata, autoload=True, autoload_with=engine)
university=Table('university', metadata, autoload=True, autoload_with=engine)

#Пример
s = select([university])
rp = connection.execute(s)
results = rp.fetchall()

def task_1():
    """Задание 1"""

    s = select([
        cast(student.c.student_id, String(20))+";"+
        cast(student.c.surname, String(20))+";"+
        cast(student.c.name, String(20))+";"+
        cast(student.c.stipend, String(20))+";"+
        cast(student.c.kurs, String(20))+";"+
        cast(student.c.city, String(20))+";"+
        cast(func.strftime('%d/%m/%Y',student.c.birthday),  String(20))+";"+
        cast(student.c.univ_id, String(20))+"."
        ])

    rp = connection.execute(s)
    results = rp.fetchall()
    new = [item[0].upper() for item in results if item[0] is not None]
    return new

def task_2():
    """Задание 2"""
    s = select([
        cast(func.substr(student.c.name,1,1), String(20))+"."+
        cast(student.c.surname, String(20))+"; место жительства-"+
        cast(student.c.city, String(20))+"; родился - "+
        cast(func.strftime('%d/%m/%Y',student.c.birthday),  String(20))+"."
        ])

    rp = connection.execute(s)
    results = rp.fetchall()
    return results

def task_3():
    """Задание 3"""
    pass

def main():
    print(task_1())
    print(task_2())
    print(task_3())

if __name__ == "__main__":
    main()