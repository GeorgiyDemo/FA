"""
Что надо:
SELECT SUBJ_NAME, SURNAME, MARK
FROM STUDENT
JOIN SUBJECT
JOIN EXAM_MARKS ON STUDENT.STUDENT_ID = EXAM_MARKS.STUDENT_ID AND SUBJECT.SUBJ_ID = EXAM_MARKS.SUBJ_ID ANDEXAM_MARKS.MARK=2;
"""

"""
Что сделал:
SELECT
student.kurs,
AVG(exam_marks.mark),
exam_marks.subj_id
FROM student
INNER JOIN exam_marks ON student.student_id=exam_marks.student_id
GROUP BY student.kurs, exam_marks.subj_id
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


def task():
    """.join"""

    joined_exp = student.join(exam_marks, student.c.student_id==exam_marks.c.student_id)
    s = select([
        student.c.kurs,
        func.avg(exam_marks.c.mark),
        exam_marks.c.subj_id]
        ).select_from(joined_exp).group_by(student.c.kurs, exam_marks.c.subj_id)
   
    print(str(s))
    rp = connection.execute(s)
    return rp.fetchall()

def main():
    task()

if __name__ == "__main__":
    main()