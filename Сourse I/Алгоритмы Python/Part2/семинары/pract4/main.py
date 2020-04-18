"""
Разработать программное средство с использованием ООП для представления успеваемости студентов по дисциплине:
1)	Промежуточная аттестация максимум 20 баллов, разбитые по количеству работ (практики, контрольная и тестирование в 1 половине семестра);
2)	Работа в семестре 20 баллов (практики, контрольная и тестирование во 2 половине семестра);
3)	Экзамен 60 баллов;
4)	Выставление итоговой оценки.
Объект класса должен содержать поля для сохранения имени студента и истории получения баллов (по практикам, контрольным и тестированиям) с учетом даты получения оценки по схеме: выполнено, защищено.
"""
from functools import reduce
import datetime

class Work:
    """
    Класс работы
    [!] К работе не относится экзамен
    """

    WORK_COUNT = 6 #кол-во работ в полусеместре + 1 контрольная + 1 тестирование

    def __init__(self, name, work_type, date_deadline, work_completed=False, date_completed=None, work_protected=False, date_protected=None):
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
        
        #Фильтрация входных данных
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

        #Выставление полей
        self.points = 0
        self.name = name
        self.work_type = work_type
        self.work_completed = work_completed
        self.work_protected = work_protected

        #Если есть все данные и можно считать, что работа уже сделана
        if all(map(lambda x: False if x == None else True, [self.date_completed, self.date_protected])):
            self.set_protection(self.date_protected.strftime("%d.%m.%Y"))
    
    def __str__(self):
        """Информация о работе"""

        sub_d = {True : "✅",False : "❌",}
        d = {}
        d["Название:"] = self.name
        d["Тип работы:"] = self.work_type
        d["Дедлайн:"] = self.date_deadline.strftime("%d.%m.%Y")
        d["Завершение работы:"] = sub_d[self.work_completed]
        d["Защита работы:"] = sub_d[self.work_protected]
        d["Дата завершения работы:"] = self.date_completed.strftime("%d.%m.%Y") if self.date_completed != None else "-"
        d["Дата защиты работы:"] = self.date_protected.strftime("%d.%m.%Y") if self.date_protected != None else "-"
        d["Количество баллов:"] = self.points
        return "*Класс работа*\n"+"\n".join([key+" "+str(value) for key, value in d.items()])

    def set_complete(self, date):
        """Осуществление сдачи работы"""

        #Проверка на валидные данные
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            print("Некорректная дата сдачи работы!")
            return

        self.work_completed = True
        self.date_completed = date

    def set_protection(self, date):
        """"Осуществление защиты работы и выставление баллов за работу"""
        
        #Проверка на валидные данные
        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            print("Некорректная дата защиты работы!")
            return

        self.work_protected = True
        self.date_protected = date

        #Штрафные баллы
        penalty_points = 0
        #Балл за работу
        points = 20/Work.WORK_COUNT

        #Вычисление коэффа понижения кол-ва баллов. Каждая неделя - 1 балл
        if date > self.date_deadline:
            diff = date-self.date_deadline
            penalty_points = int(diff.days/7)
            
            #Если принесли работу так поздно, что потеряли все, то 0 баллов
            if penalty_points > points:
                penalty_points = points

        self.points = points-penalty_points

class Certification:
    """
    Класс промежуточной аттестации
    """

    def __init__(self, name):
        #Название аттестации
        self.name = name
        #Динамическое изменение временных промежутков на основе объекта Work
        self.date_begin = None
        self.date_end = None
        self._points = 0
        self.work_obj_list = []

    def add(self, work_obj):
        """Метод для добавления работы к промежуточной аттестации"""
        if not isinstance(work_obj, Work):
            raise ValueError("Объект не класса Work!")

        date_end, date_begin = self.date_end, self.date_begin
        #Добавление работы к промежуточной аттестации
        self.work_obj_list.append(work_obj)
        
        #Расширение диапазона дат
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
        d["Общее кол-во баллов:"] = round(reduce(lambda x, y: x + y, [e.points for e in self.work_obj_list]),1) if len(self.work_obj_list) != 0 else 0
        d["Общее кол-во работ:"] = len(self.work_obj_list)
        out_str = "\n"+self.name+"\n"+"\n".join([key+" "+str(value) for key, value in d.items()])
        
        if len(self.work_obj_list) != 0:
            out_str += "\nНазвания работ, из которых состоит:\n"
            out_str += "\n".join([w.name for w in self.work_obj_list])

        return out_str
    
    @property
    def points(self):

        #Если кол-во работ != необходимому из логики подсчета баллов - ошибка получения
        if len(self.work_obj_list) != Work.WORK_COUNT:
            raise ValueError("Количество работ больше/меньше необходимого!")
        
        #Чтоб присутствовала контрольная и тестирование
        if len([e for e in self.work_obj_list if e.work_type == "контрольная"]) == 0 or len([e for e in self.work_obj_list if e.work_type == "тестирование"]) == 0:
            raise ValueError("Отсутствие работ с типом 'контрольная'/'тестирование'")

        return round(reduce(lambda x, y: x + y, [e.points for e in self.work_obj_list]),1)

class Student:
    """
    Класс студент
    У студента есть:
    - 2 объекта полусеместра
    - экзамен
    
    Методы:
    - Добавление полусеместра
    - Добавление второго полусеместра
    - Добавление экзамена

    - Добавление баллов по экзамену
    - Получение общего кол-ва баллов
    - Получение статистики по кол-ву работ
    - Получение итоговой оценки

    """
    def __init__(self, name, group, course):
        self.name = name
        self.group = group
        self.course = course
        #Объекты аттестаций
        self.cert_obj_list = []
        pass

    def __str__(self):
        """Информация о студенте"""
        #Имя
        #Группа
        #Курс
        pass
    
    def add_certification(self, cert_obj):
        """Метод добавления аттестации"""
        if not isinstance(cert_obj, Certification):
            raise ValueError("Объект не класса Certification!")
        self.cert_obj_list.append(cert_obj)

        #Если длинна 2, то вызов self.certification_patcher
    
    def certification_patcher(self):
        """Метод для валидации двух аттестаций, чтоб они превратились в нормальный такой полусеместр"""
        pass
    
    def add_exam(self, points):
        """Добавление баллов за экзамен"""
        if 0 < points < 60:
            pass
    
    def get_mark(self):
        """Получение оценки студента"""
        pass



def main():
    """
    Общий алгоритм
    - Генерим студента
    - Генерим промежуточную аттестацию/аттестацию
    - Генерим работу

    - Добавляем объект аттестации к студенту
    - В объект аттестации добавляем работы
    - Добавляем объект работы к промежуточной аттестации

    Повторяем сколько надо

    В конце, в методе получения итоговой оценки, надо понять, что 
    """
    l = []
    for i in range(4):
        l.append(Work("№"+str(i+1), "практика", "20.03.2020",True, "18.03.2020", True, "28.03.2020"))
    
    #[print(e) for e in l]
    certification_obj = Certification("Промежуточная аттестация 1")
    [certification_obj.add(work) for work in l]
    certification_obj.add(Work("КОНТРОЛЬНАЯ", "контрольная", "20.03.2020",True, "18.03.2020", True, "28.03.2020"))
    certification_obj.add(Work("тестирование", "тестирование", "20.03.2020",True, "18.03.2020", True, "28.03.2020"))
    print(certification_obj)
    print(certification_obj.points)
    #print(certification_obj.points)
    


if __name__ == "__main__":
    main()