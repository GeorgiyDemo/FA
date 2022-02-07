"""
ПИ19-4 Деменчук Георгий Практика 5
Подгруппа 3
"""

from sqlalchemy import select, create_engine, MetaData, Table, cast, String, Integer
from sqlalchemy.sql import func

import warnings

warnings.filterwarnings('ignore')

#Соединяемся с СУБД
engine = create_engine("sqlite:///Students.db")
metadata=MetaData()
connection=engine.connect()

#Объявляем все таблицы, с которыми будем работать
exam_marks=Table('exam_marks', metadata, autoload=True, autoload_with=engine)
lecturer=Table('lecturer', metadata, autoload=True, autoload_with=engine)
student=Table('student', metadata, autoload=True, autoload_with=engine)
subj_lect =Table('subj_lect', metadata, autoload=True, autoload_with=engine)
subject=Table('subject', metadata, autoload=True, autoload_with=engine)
university=Table('university', metadata, autoload=True, autoload_with=engine)

def task_1():
    """Задание 1"""

    s = select([
        cast(student.c.student_id, String(20))+";"+
        cast(student.c.surname, String(20))+";"+
        cast(student.c.name, String(20))+";"+
        cast(student.c.stipend, String(20))+";"+
        cast(student.c.city, String(20))+";"+
        cast(func.strftime('%d/%m/%Y',student.c.birthday),  String(20))+";"+
        cast(student.c.univ_id, String(20))+"."
        ])

    print(str(s))
    rp = connection.execute(s)
    results = rp.fetchall()
    return [item[0].upper() for item in results if item[0] is not None]

def task_2():
    """Задание 2"""
    s = select([
        cast(func.substr(student.c.name,1,1), String(20))+"."+
        cast(student.c.surname, String(20))+"; место жительства-"+
        cast(student.c.city, String(20))+"; родился - "+
        cast(func.strftime('%d.%m.%Y.',student.c.birthday),  String(20))
        ])

    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_3():
    """Задание 3"""
    s = select([
        cast(func.substr(student.c.name,1,1), String(20))+"."+
        cast(student.c.surname, String(20))+"; место жительства-"+
        cast(student.c.city, String(20))+"; родился: "+
        cast(func.strftime('%d-%m-%Y',student.c.birthday),  String(20))+"."
        ])

    print(str(s))
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

    print(str(s))
    rp = connection.execute(s)
    return rp.fetchone()

def task_5():
    """Задание 5"""
    s = select([
        student.c.name,
        student.c.surname,
        cast((student.c.stipend * 100), Integer)
    ])
    
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_6():
    """Задание 6"""
    s = select([
        cast(student.c.name, String(20))+" "+
        cast(student.c.surname, String(20))+" родился в "+
        cast(func.strftime('%Y',student.c.birthday),  String(20))+" году" +"."
    ]).where(student.c.kurs.in_((1,2,4)))

    print(str(s))
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

    print(str(s))
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
    
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_9():
    """Задание 9"""
    s = select([
        func.count(exam_marks.c.student_id)
        ]).where(exam_marks.c.subj_id == 20)
    
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()


def task_10():
    """Задание 10"""
    s = select([
        func.count(func.distinct(exam_marks.c.subj_id))
        ])
    
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_11():
    """Задание 11"""
    s = select([
        exam_marks.c.student_id, 
        func.min(exam_marks.c.mark)
        ]).group_by(exam_marks.c.student_id)
    
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_12():
    """Задание 12"""
    s = select([
        exam_marks.c.student_id, 
        func.max(exam_marks.c.mark)
        ]).group_by(exam_marks.c.student_id)
    
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_13():
    """Задание 13"""
    s = select([
        student.c.surname, 
        ]).where(student.c.surname.like("И%")).limit(1)

    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_14():
    """Задание 14"""
    s = select([
        subject.c.subj_name, 
        func.max(subject.c.semester.label("max_semester"))
        ]).group_by(subject.c.subj_name)

    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_15():
    """Задание 15"""
    s = select([
        func.count(func.distinct(exam_marks.c.student_id)).label("Кол-во студентов"),
        exam_marks.c.exam_date.label("Дата экзамена"),
        exam_marks.c.exam_id.label("id экзамена")
        ]).group_by(exam_marks.c.exam_date)
 
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_16():
    """Задание 16"""

    joined_tables = student.join(exam_marks, student.c.student_id==exam_marks.c.student_id)
    s = select([
        student.c.kurs,
        func.avg(exam_marks.c.mark),
        exam_marks.c.subj_id]
        ).select_from(joined_tables).group_by(student.c.kurs, exam_marks.c.subj_id)
   
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_17():
    """Задание 17"""
    s = select([
        exam_marks.c.student_id,
        func.avg(exam_marks.c.mark)
        ]).group_by(exam_marks.c.student_id)
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_18():
    """Задание 18"""
    s = select([
        exam_marks.c.exam_id,
        func.avg(exam_marks.c.mark)
        ]).group_by(exam_marks.c.exam_id)
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_19():
    """Задание 19"""
    s = select([
        exam_marks.c.exam_id,
        func.count(exam_marks.c.student_id).label("Кол-во студентов")
        ]).group_by(exam_marks.c.exam_id)
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def task_20():
    """Задание 20"""
    s = select([
        cast(((subject.c.semester +1)/ 2 ), Integer).label("kurs"),
        func.count().label("Кол-во предметов")
        ]).group_by("kurs")
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def main():

    tasks_list = [task_1,task_2,task_3, task_4, task_5, \
        task_6, task_7, task_8, task_9, task_10, task_11, \
        task_12, task_13, task_14, task_15, task_16, task_17, \
        task_18, task_19, task_20]

    for i in range(len(tasks_list)):
        print(f"\nЗадание №{i+1}")
        [print(r) for r in tasks_list[i]()]

if __name__ == "__main__":
    main()