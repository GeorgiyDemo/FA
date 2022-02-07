import sqlite3
from task_module import WorkClass, ExamClass, StudentClass, CertificationClass


class SQLiteClass:
    def __init__(self):

        self.dbname = "pract4.db"
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        # Студент
        c.execute(
            "CREATE TABLE IF NOT EXISTS student (student_id integer primary key autoincrement, name text, groups text, course text, points real, mark integer)"
        )
        # Экзамены
        c.execute(
            "CREATE TABLE IF NOT EXISTS exam (student_id integer UNIQUE, name text, points real)"
        )
        # Аттестация
        c.execute(
            "CREATE TABLE IF NOT EXISTS certification (cert_id integer primary key autoincrement, student_id integer, name text, points real, date_begin text, date_end text)"
        )
        # Работа
        c.execute(
            "CREATE TABLE IF NOT EXISTS work (cert_id integer, student_id integer, name text, points real, work_type text, date_deadline text, date_completed text, date_protected text, work_completed integer, work_protected integer)"
        )

        conn.commit()
        conn.close()

    def drop_tables(self):
        """Удаление всех данных с таблиц в БД"""

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        c.execute("DELETE FROM student")
        c.execute("DELETE FROM exam")
        c.execute("DELETE FROM certification")
        c.execute("DELETE FROM work")

        conn.commit()
        conn.close()

    def get_students(self):
        """Получение всех объектов студентов из таблицы"""

        student_obj_list = []
        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        # По каждому студенту цикл
        for student_args in list(
            c.execute("SELECT student_id, name, groups, course FROM student")
        ):
            current_studentid, *s = student_args
            student_obj = StudentClass(*s)

            # Получаем экзамены студента
            exam_args = list(
                c.execute(
                    "SELECT name, points FROM exam WHERE student_id="
                    + str(current_studentid)
                )
            )
            if len(exam_args) != 0:
                student_obj.add_exam(ExamClass(*exam_args[0]))

            cert_obj_list = []
            # Получаем аттестации студента
            for certification in list(
                c.execute(
                    "SELECT cert_id, name FROM certification WHERE student_id="
                    + str(current_studentid)
                )
            ):

                current_certid, name = certification
                cert_obj = CertificationClass(name)

                # Получаем работу студента
                for work in list(
                    c.execute("SELECT * FROM work WHERE cert_id=" + str(current_certid))
                ):
                    d = dict(
                        zip(
                            [
                                "cert_id",
                                "student_id",
                                "name",
                                "points",
                                "work_type",
                                "date_deadline",
                                "date_completed",
                                "date_protected",
                                "work_completed",
                                "work_protected",
                            ],
                            work,
                        )
                    )
                    work_obj = WorkClass(
                        d["name"],
                        d["work_type"],
                        d["date_deadline"],
                        bool(d["work_completed"]),
                        d["date_completed"],
                        bool(d["work_protected"]),
                        d["date_protected"],
                    )

                    # Добавляем работу к аттестации
                    cert_obj.add(work_obj)

                # Добавляем аттестации в список аттестаций
                cert_obj_list.append(cert_obj)

            # Добавляем аттестации для студента
            [student_obj.add_certification(cert) for cert in cert_obj_list]
            # Добавляем студента в список студентов
            student_obj_list.append(student_obj)

        conn.close()
        return student_obj_list

    def set_students(self, s_obj):
        """Запись всех данных с объекта студета в БД"""

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        # Запись данных студента
        r = c.execute(
            "INSERT INTO student (name, groups, course, points, mark) VALUES ('{}','{}','{}',{},{})".format(
                s_obj.name,
                s_obj.group,
                s_obj.course,
                s_obj.points,
                s_obj.get_mark(True),
            )
        )
        current_studentid = r.lastrowid

        # Запись экзамена, если он существует
        exam_obj = s_obj.exam_obj
        if exam_obj != None:
            c.execute(
                "INSERT INTO exam VALUES ({},'{}',{})".format(
                    current_studentid, exam_obj.name, exam_obj.points
                )
            )

        # Запись аттестаций
        if len(s_obj.cert_obj_list) != 0:
            for cert in s_obj.cert_obj_list:
                r = c.execute(
                    "INSERT INTO certification (student_id, name, points, date_begin, date_end) VALUES ({},'{}',{},'{}','{}')".format(
                        current_studentid,
                        cert.name,
                        cert.points,
                        cert.date_begin.strftime("%d.%m.%Y"),
                        cert.date_end.strftime("%d.%m.%Y"),
                    )
                )
                current_certid = r.lastrowid

                # Запись работ
                for work in cert.work_obj_list:

                    if work.date_protected != None:
                        date_protected = work.date_protected.strftime("%d.%m.%Y")
                    else:
                        date_protected = None

                    if work.date_completed != None:
                        date_completed = work.date_completed.strftime("%d.%m.%Y")
                    else:
                        date_completed = None

                    work_args_list = [
                        current_certid,
                        current_studentid,
                        work.name,
                        work.points,
                        work.work_type,
                        work.date_deadline.strftime("%d.%m.%Y"),
                        date_completed,
                        date_protected,
                        work.work_completed,
                        work.work_protected,
                    ]
                    c.execute(
                        "INSERT INTO work VALUES ({},{},'{}',{},'{}','{}','{}','{}',{},{})".format(
                            *work_args_list
                        )
                    )

        conn.commit()
        conn.close()

    def remove_students(self, s_obj):
        """Удлаение объекта студента из БД"""

        conn = sqlite3.connect(self.dbname)
        c = conn.cursor()

        # Получение id студента и последующее удаление
        r = c.execute(
            "SELECT student_id FROM student WHERE (name='{}' AND groups='{}' AND course='{}')".format(
                s_obj.name, s_obj.group, s_obj.course
            )
        )
        current_studentid = list(r)[0][0]
        c.execute("DELETE FROM student WHERE student_id={}".format(current_studentid))
        # Удаление экзамена
        c.execute("DELETE FROM exam WHERE student_id={}".format(current_studentid))
        # Удаление аттестаций
        c.execute(
            "DELETE FROM certification WHERE student_id={}".format(current_studentid)
        )
        # Удаление работ
        c.execute("DELETE FROM work WHERE student_id={}".format(current_studentid))

        conn.commit()
        conn.close()
