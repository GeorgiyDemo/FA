import sqlite3

#
from main import StudentClass
#
class SQLiteClass:
    def __init__(self):
        
        self.dbname = "pract4.db"
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        #Студент
        c.execute("CREATE TABLE IF NOT EXISTS student (student_id integer primary key autoincrement, name text, groups text, course text, points real, mark integer)")
        #Экзамены
        c.execute("CREATE TABLE IF NOT EXISTS exam (student_id integer UNIQUE, name text, points real)")
        #Аттестация
        c.execute("CREATE TABLE IF NOT EXISTS certification (cert_id integer primary key autoincrement, student_id integer, name text, points real, date_begin text, date_end text)")
        #Работа
        c.execute("CREATE TABLE IF NOT EXISTS work (cert_id integer, student_id integer, name text, points real, work_type text, date_deadline text, date_completed text, date_protected text, work_completed integer, work_protected integer)")


        # Save (commit) the changes
        conn.commit()
        conn.close()

    #TODO
    def get_students(self):
        """Получение всех объектов студентов из таблицы"""
        pass

    def set_students(self, s_obj):
        """Запись всех данных с объекта студета в БД"""

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        #Запись данных студента
        r = c.execute("INSERT INTO student (name, groups, course, points, mark) VALUES ('{}','{}','{}',{},{})".format(s_obj.name, s_obj.group, s_obj.course, s_obj._points, s_obj.get_mark(True)))
        current_studentid = r.lastrowid

        #Запись экзамена, если он существует
        exam_obj = s_obj.exam_obj
        if exam_obj != None:
            c.execute("INSERT INTO exam VALUES ({},'{}',{})".format(current_studentid, exam_obj.name, exam_obj._points))
        
        #Запись аттестаций
        if len(s_obj.cert_obj_list) != 0:
            for cert in s_obj.cert_obj_list:
                r = c.execute("INSERT INTO certification (student_id, name, points, date_begin, date_end) VALUES ({},'{}',{},'{}','{}')".format(current_studentid, cert.name, cert._points, cert.date_begin.strftime("%d.%m.%Y"), cert.date_end.strftime("%d.%m.%Y")))
                current_certid = r.lastrowid
                
                #Запись работ
                for work in cert.work_obj_list:
                    
                    if work.date_protected != None:
                        date_protected = work.date_protected.strftime("%d.%m.%Y")
                    else:
                        date_protected = None

                    if work.date_completed != None:
                        date_completed = work.date_completed.strftime("%d.%m.%Y")
                    else:
                        date_completed = None

                    work_args_list = [current_certid, current_studentid, work.name, work.points, work.work_type, work.date_deadline.strftime("%d.%m.%Y"), date_completed, date_protected, work.work_completed, work.work_protected]
                    c.execute("INSERT INTO work VALUES ({},{},'{}',{},'{}','{}','{}','{}',{},{})".format(*work_args_list))

        conn.commit()
        conn.close()
        print("ВСЕ ЗАПИСАЛИ")

if __name__ == "__main__":
    sql_obj = SQLiteClass()
    s = StudentClass("Деменчук Георгий","ПИ19-4",1)
    
    sql_obj.set_students(s)