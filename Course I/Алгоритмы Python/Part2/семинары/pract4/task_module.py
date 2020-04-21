import datetime

from texttable import Texttable


class UtilClass:
    boolean_dict = {
        "Да": True,
        "ДА": True,
        "Нет": False,
        "Не": False,
        "нет": False,
        "не": False,
    }

    @staticmethod
    def boolean_formater(flag):
        sub_d = {True: "✅", False: "❌", }
        return sub_d[flag]

    @staticmethod
    def is_digital(data):
        try:
            float(data)
            return True
        except ValueError:
            return False

    @staticmethod
    def converter(d_input):
        try:
            return d_input.strftime("%d.%m.%Y")
        except AttributeError:
            return "-"


class WorkClass:
    """
    Класс работы
    [!] К работе не относится экзамен
    """
    WORK_COUNT = 6  # рекомендуемое кол-во работ в полусеместре и учетом контрольной и тестирования

    def __init__(self, name, work_type, date_deadline, work_completed=False, date_completed=None, work_protected=False,
                 date_protected=None):
        """
        Поля конструктора:
        - name - название работы
        - work_type - тип работы
        - date_deadline - дата сдачи работы
        
        Необязательные:
        - work_completed - сдача работы (True/False)
        - date_completed - дата завершения сдачи работы
        - work_protected - защита работы (True/False)
        - date_protected - дата завершения защиты работы
        """

        # Фильтрация входных данных
        if work_type not in ["практика", "контрольная", "тестирование"]:
            raise ValueError("Некорректнй тип работы!")

        if not all(map(lambda x: type(x) == bool, [work_completed, work_protected])):
            raise ValueError("Некорректные значения work_completed/work_protected!")

        if work_completed:
            try:
                self.date_completed = datetime.datetime.strptime(date_completed, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Некорректный ввод даты сдачи работы!")
        else:
            self.date_completed = None
        if work_protected:
            try:
                self.date_protected = datetime.datetime.strptime(date_protected, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Некорректный ввод даты защиты работы!")
        else:
            self.date_protected = None
        try:
            self.date_deadline = datetime.datetime.strptime(date_deadline, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Некорректный срок сдачи работы!")

        # Выставление полей
        self.points = 0
        self.name = name
        self.work_type = work_type
        self.work_completed = work_completed
        self.work_protected = work_protected

        # Если есть все данные и можно считать, что работа уже сделана
        if all(map(lambda x: False if x == None else True, [self.date_completed, self.date_protected])):
            self.set_protection(self.date_protected.strftime("%d.%m.%Y"))

    def __str__(self):
        """Информация о работе"""
        d = {}
        d["Тип работы:"] = self.work_type
        d["Дедлайн:"] = self.date_deadline.strftime("%d.%m.%Y")
        d["Завершение работы:"] = UtilClass.boolean_formater(self.work_completed)
        d["Защита работы:"] = UtilClass.boolean_formater(self.work_protected)
        d["Дата завершения работы:"] = self.date_completed.strftime("%d.%m.%Y") if self.date_completed != None else "-"
        d["Дата защиты работы:"] = self.date_protected.strftime("%d.%m.%Y") if self.date_protected != None else "-"
        d["Количество баллов:"] = self.points
        return "\033[93m\n*" + self.name + "*\n\033[0m" + "\n".join(
            [key + " " + str(value) for key, value in d.items()])

    def get_list(self):
        """Отдача информации для вывода в Texttable"""
        c = UtilClass.converter
        return [self.name, self.work_type, c(self.date_deadline), c(self.date_completed), c(self.date_protected),
                self.points]

    def set_complete(self, date, info=False):
        """Осуществление сдачи работы"""

        # Проверка на валидные данные
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            print("Некорректная дата сдачи работы!")
            return

        self.work_completed = True
        self.date_completed = date

        if info:
            print("Успешно сдали работу")

    def set_protection(self, date, info=False):
        """"Осуществление защиты работы и выставление баллов за работу"""

        # Проверка на валидные данные
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            print("Некорректная дата защиты работы!")
            return

        if not self.work_completed:
            print("Невозможно защитить работу не сдав её!")
            return

        self.work_protected = True
        self.date_protected = date

        # Штрафные баллы
        penalty_points = 0
        # Балл за работу
        points = 20 / WorkClass.WORK_COUNT

        # Вычисление коэффа понижения кол-ва баллов. Каждая неделя - 1 балл
        if date > self.date_deadline:
            diff = date - self.date_deadline
            penalty_points = int(diff.days / 7)

            # Если принесли работу так поздно, что потеряли все, то 0 баллов
            if penalty_points > points:
                penalty_points = points

        self.points = round(points - penalty_points, 1)

        if info:
            print("Успешно защитили работу")


class CertificationClass:
    """
    Класс промежуточной аттестации
    """

    def __init__(self, name):
        # Название аттестации
        self.name = name
        # Динамическое изменение временных промежутков на основе объекта Work
        self.date_begin = None
        self.date_end = None
        self._points = 0
        self.work_obj_list = []

    def add(self, work_obj):
        """Метод для добавления работы к промежуточной аттестации"""
        if not isinstance(work_obj, WorkClass):
            raise ValueError("Объект не класса Work!")

        date_end, date_begin = self.date_end, self.date_begin

        # Добавление работы к промежуточной аттестации
        self.work_obj_list.append(work_obj)

        # Добавление баллов
        self._points += work_obj.points

        # Расширение диапазона дат
        if date_end == None or work_obj.date_deadline > date_end:
            date_end = work_obj.date_deadline

        if date_begin == None or work_obj.date_deadline < date_begin:
            date_begin = work_obj.date_deadline

        self.date_end, self.date_begin = date_end, date_begin

    def __str__(self):
        """Информация о промежуточной аттестации"""

        d = {}
        self.date_begin.strftime("%d.%m.%Y") if self.date_begin != None else "-"
        d["Дата начала:"] = self.date_begin.strftime("%d.%m.%Y") if self.date_begin != None else "-"
        d["Дата окончания:"] = self.date_end.strftime("%d.%m.%Y") if self.date_end != None else "-"
        d["Общее кол-во баллов:"] = round(self._points)
        d["Общее кол-во работ:"] = len(self.work_obj_list)
        out_str = "\033[93m\n*" + self.name + "*\n\033[0m" + "\n".join(
            [key + " " + str(value) for key, value in d.items()])

        return out_str

    @property
    def points(self):

        # Если кол-во работ != необходимому из логики подсчета баллов - ошибка получения
        if len(self.work_obj_list) != WorkClass.WORK_COUNT:
            print("\033[91mКоличество работ больше/меньше рекомендуемого ({} шт.)\033[0m".format(WorkClass.WORK_COUNT))
            # raise ValueError("Количество работ больше/меньше необходимого!")

        # Чтоб присутствовала контрольная и тестирование
        if len([e for e in self.work_obj_list if e.work_type == "контрольная"]) == 0 or len(
                [e for e in self.work_obj_list if e.work_type == "тестирование"]) == 0:
            print("\033[91mОтсутствие работ с типом 'контрольная'/'тестирование'. Рекомендуется внести!\033[0m")
            # Тут по-хорошему должен быть Exception
        return self._points


class ExamClass:
    """Класс экзамена"""

    def __init__(self, name, points):
        self.name = name
        if 0 <= points <= 60:
            self._points = points
        else:
            raise ValueError("Некорректные данные баллов по экзамену!")

    def __str__(self):
        """Информация об экзамене"""
        d = {}
        d["Название:"] = self.name
        d["Кол-во баллов:"] = self._points
        return "\033[93m\n*Информация об экзамене*\n\033[0m" + "\n".join(
            [key + " " + str(value) for key, value in d.items()])

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, p):
        if not isinstance(p, int) or 0 <= p <= 60:
            raise ValueError("Некорректные данные баллов по экзамену!")
        self._points = p


"""
Объект класса должен содержать поля для сохранения имени студента и
истории получения баллов (по практикам, контрольным и тестированиям) с учетом даты получения оценки по схеме: выполнено, защищено.
"""


class StudentClass:
    """
    Класс студент
    У студента есть:
    - 2 объекта полусеместра
    - экзамен
    
    Методы:
    - Добавление полусеместра
    - Добавление экзамена

    - Получение общего кол-ва баллов
    - Получение статистики по кол-ву работ
    - Получение итоговой оценки
    """

    def __init__(self, name, group, course):
        self.name = name
        self.group = group
        self.course = course
        self._points = 0

        self.datavalidator_flag = False
        self.exam_obj = None

        # Объекты аттестаций
        self.cert_obj_list = []

        # Словарь ассоциации кол-ва баллов и оценки
        self.mark_dict = {}
        [self.mark_dict.update(e) for e in [{v1: v for v1 in rrange} for rrange, v in
                                            zip([range(0, 51), range(51, 70), range(70, 85), range(85, 101)],
                                                [2, 3, 4, 5])]]

    def all_info(self):
        """Информация о всех подобъектах объекта класса студента"""

        # Студент
        print(self)
        # Аттестации
        for cert in self.cert_obj_list:
            print(cert)

            table = Texttable()
            table_list = [["№", "Название", "Тип", "Дата дедлайна", "Дата сдачи", "Дата защиты", "Баллы"]]

            for i in range(len(cert.work_obj_list)):
                buf_l = [str(i + 1)] + cert.work_obj_list[i].get_list()
                table_list.append(buf_l)

            table.add_rows(table_list)
            print("\n" + table.draw())

        # Экзамен
        if self.exam_obj != None:
            print(self.exam_obj)

    def __str__(self):
        """Информация о студенте"""
        d = {}
        d["ФИО:"] = self.name.replace("\n", "")
        d["Группа:"] = self.group
        d["Курс:"] = self.course
        d["Полные ли данные:"] = UtilClass.boolean_formater(self.datavalidator_flag)
        d["Количество баллов:"] = self._points
        d["Оценка:"] = self.get_mark(True)

        return "\033[93m\n*Информация о студенте*\n\033[0m" + "\n".join(
            [key + " " + str(value) for key, value in d.items()])

    def add_certification(self, cert_obj):
        """Метод добавления аттестации"""
        if not isinstance(cert_obj, CertificationClass):
            raise ValueError("Объект не класса Certification!")
        # Проверка на корректность валидации
        try:
            self._points += round(cert_obj.points)
            self.cert_obj_list.append(cert_obj)
        except ValueError as e:
            print(e)
            return

        if len(self.cert_obj_list) == 2:
            self.certification_patcher()
            self.data_validator()

    def certification_patcher(self):
        """Метод для синхрона дат двух аттестаций, чтоб они превратились в полноценный полусеместр"""
        cert1, cert2 = self.cert_obj_list
        if cert1.date_end > cert2.date_begin:
            cert2.date_begin = cert1.date_end
        elif cert1.date_end < cert2.date_begin:
            cert1.date_end = cert2.date_begin

    def data_validator(self):
        """Проверка на полноту всех данных текущего объекта класса"""
        if self.exam_obj != None and len(self.cert_obj_list) == 2:
            self.datavalidator_flag = True
        else:
            self.datavalidator_flag = False

    def add_exam(self, exam_obj):
        """Добавление баллов за экзамен"""
        if not isinstance(exam_obj, ExamClass):
            raise ValueError("Объект не класса ExamClass!")
        self._points += exam_obj.points
        self.exam_obj = exam_obj
        self.data_validator()

    def get_mark(self, ignore=False):
        """Получение оценки студента"""
        if not self.datavalidator_flag and ignore == False:
            raise ValueError("Невозможно получить итоговую оценку студента! Недостаточно данных")
        d = {}
        [d.update(e) for e in [{v1: v for v1 in rrange} for rrange, v in
                               zip([range(0, 51), range(51, 70), range(70, 85), range(85, 101)], [2, 3, 4, 5])]]
        return d[round(self._points)]

    @property
    def mark(self):
        return self.get_mark()

    @property
    def points(self):
        if not self.datavalidator_flag:
            raise ValueError("Невозможно получить итоговые баллы студента! Недостаточно данных")
        return self._points
