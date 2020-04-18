"""
Разработать программное средство с использованием ООП для представления успеваемости студентов по дисциплине:
1)	Промежуточная аттестация максимум 20 баллов, разбитые по количеству работ (практики, контрольная и тестирование в 1 половине семестра);
2)	Работа в семестре 20 баллов (практики, контрольная и тестирование во 2 половине семестра);
3)	Экзамен 60 баллов;
4)	Выставление итоговой оценки.
Объект класса должен содержать поля для сохранения имени студента и истории получения баллов (по практикам, контрольным и тестированиям) с учетом даты получения оценки по схеме: выполнено, защищено.
"""
import datetime

class Work:
    """
    Класс работы
    
    При создании работы уже подразумевается то, что она выполнена
    !! К работе не относится экзамен
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
    
    def info(self):
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

        try:
            date = datetime.datetime.strptime(date, "%d.%m.%Y")
        except ValueError:
            print("Некорректная дата сдачи работы!")
            return

        #Проверка на валидные данные
        self.work_completed = True
        self.date_completed = date

    def set_protection(self, date):
        """"Осуществление защиты работы и выставление баллов за работу"""
        
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
            diff = self.date_deadline-date
            penalty_points = int(diff.days/7)
            
            #Если принесли работу так поздно, что потеряли все, то 0 баллов
            if penalty_points > points:
                penalty_points = points

        self.points = points-penalty_points

class Certification:
    """
    Класс промежуточной аттестации (по логике 2 промежуточных = полная аттестация за семестр)
    
    - Добавление баллов по практической        <- это все один метод, который в зависимости от типа, добавляет объект работы в list
    - Добавление баллов по контрольной
    - Добавление баллов по тестированию
    """
    points_counter = 0

    def __init__(self, name):
        self.work_obj_list = []

    
    def work_add(self, work_obj):
        """Метод для добавления работы к промежуточной аттестации"""
        if not isinstance(work_obj, Work):
            raise ValueError("Объект не класса Work!")
        #Добавление работы к промежуточной аттестации
        self.work_obj_list.append(work_obj)



class Student:
    """
    Класс студент
    У студента есть:
    - практические
    - контрольные
    - тестирование (тесты)
    
    Методы:
    - Добавление полусеместра
    - Добавление второго полусеместра
    - Добавление экзамена

    - Добавление баллов по экзамену
    - Получение общего кол-ва баллов
    - Получение статиситка по кол-ву работ
    - Получение итоговой оценки

    """
    def __init__(self, name, group, course):
        pass

    def info(self):
        """Информация о студенте"""
        pass

    def add_certification(self):
        """Метод добавления аттестации"""
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
    obj = Work("№1 Рекурсия", "практика", "20.03.2020")
    print(obj.info())
    obj.set_complete("19.03.2020")
    print(obj.info())
    obj.set_protection("21.03.2020")
    print(obj.info())


if __name__ == "__main__":
    main()