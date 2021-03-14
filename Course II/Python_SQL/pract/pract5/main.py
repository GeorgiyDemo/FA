"""
ПИ19-4 Деменчук Георгий Практика 5
Подгруппа 3
"""

from sqlalchemy import select, create_engine, MetaData, Table, cast, String, Numeric
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
    return [item[0].upper() for item in results if item[0] is not None]

def task_2():
    """Задание 2"""
    s = select([
        cast(func.substr(student.c.name,1,1), String(20))+"."+
        cast(student.c.surname, String(20))+"; место жительства-"+
        cast(student.c.city, String(20))+"; родился - "+
        cast(func.strftime('%d/%m/%Y',student.c.birthday),  String(20))+"."
        ])

    rp = connection.execute(s)
    return rp.fetchall()

def task_3():
    """Задание 3"""
    s = select([
        cast(func.substr(student.c.name,1,1), String(20))+"."+
        cast(student.c.surname, String(20))+"; место жительства-"+
        cast(student.c.city, String(20))+"; родился:"+
        cast(func.strftime('%d-%m-%Y',student.c.birthday),  String(20))+"."
        ])

    rp = connection.execute(s)
    results = rp.fetchall()
    return [item[0].lower() for item in results if item[0] is not None]

def task_4():
    """Задание 4"""
    s = select([
    cast(student.c.name, String(20))+" "+
    cast(student.c.surname, String(20))+" родился в "+
    cast(func.strftime('%Y',student.c.birthday),  String(20))+" году" +"."
    ]).where(student.c.student_id == 10)

    rp = connection.execute(s)
    return rp.fetchone()

def task_5():
    """Задание 5"""
    s = select([
        student.c.name,
        student.c.surname,
        cast((student.c.stipend * 100), Numeric)
    ])
    rp = connection.execute(s)
    return rp.fetchall()

def task_6():
    """Задание 6"""
    s = select([
        cast(student.c.name, String(20))+" "+
        cast(student.c.surname, String(20))+" родился в "+
        cast(func.strftime('%Y',student.c.birthday),  String(20))+" году" +"."
    ]).where(student.c.kurs.in_((1,2,4)))
    rp = connection.execute(s)
    return rp.fetchall()

def task_7():
    """Задание 7"""
    s = select([
        "Код-"+cast(university.c.univ_id, String(20))+"; "+
        cast(university.c.univ_name, String(20))+"-г."+
        cast(university.c.city, String(20)) +"; Рейтинг="+
        cast(university.c.rating, String(20)) +"."
    ])
    rp = connection.execute(s)
    return rp.fetchall()

def task_8():
    """Задание 8"""
    s = select([
        "Код-"+cast(university.c.univ_id, String(20))+"; "+
        cast(university.c.univ_name, String(20))+"-г."+
        cast(university.c.city, String(20)) +"; Рейтинг="+
        cast(func.round(university.c.rating, -2), String(20)) +"."
    ])
    rp = connection.execute(s)
    return rp.fetchall()

def task_9():
    """Задание 9"""
    s = select([
        func.count(exam_marks.c.student_id)
        ]).where(exam_marks.c.subj_id == 20)
    rp = connection.execute(s)
    return rp.fetchall()


def task_10():
    """Задание 10"""
    s = select([
        func.count(func.distinct(exam_marks.c.subj_id))
        ])
    rp = connection.execute(s)
    return rp.fetchall()



def main():

    tasks_list = [task_1,task_2,task_3, task_4, task_5, task_6, task_7, task_8, task_9, task_10]
    for i in range(len(tasks_list)):
        print(f"\nЗадание №{i+1}")
        r = tasks_list[i]()
        print(r)


if __name__ == "__main__":
    main()